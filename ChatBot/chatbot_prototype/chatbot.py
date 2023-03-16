import os
import torch
import pandas as pd
import numpy as np
from sentence_transformers import util
from transformers import AutoModel, AutoTokenizer
from consts import DATA_DIR, MODEL_PATH
from preprocess_text import Preprocessing


class QnAchatbot:

    def __init__(self):
        self.model = AutoModel.from_pretrained(MODEL_PATH)
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

    def load_data(self, file_name: str):
        data_path = os.path.join(DATA_DIR, file_name)
        df = pd.read_csv(data_path, encoding='utf-8')
        return df

    def mean_pooling(self, model_output, attention_mask):
        """
        Mean Pooling - Take attention mask into account for correct averaging
        """
        token_embeddings = model_output[0]  # First element of model_output contains all token embeddings
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    def embedding_sentence(self, sentence: str):
        """
        KoSimCSE 활용하여 text embedding 로직
        """
        encoded_input = self.tokenizer(sentence, padding=True, truncation=True, return_tensors='pt')
        with torch.no_grad():
            model_output = self.model(**encoded_input)
        sentence_embeddings = self.mean_pooling(model_output, encoded_input['attention_mask'])
        return sentence_embeddings

    def extract_answer_by_cosine_simmility(self, prepro_input_question: str, embedded_questions: list,
                                           qna_df: pd.DataFrame):
        top_k = 1
        input_sentence_embedding = self.embedding_sentence(prepro_input_question)
        cos_sim_matrix = util.pytorch_cos_sim(input_sentence_embedding.tolist(), embedded_questions)[0].detach().numpy()
        max_idx = np.argpartition(-cos_sim_matrix, range(top_k))[:top_k][0]

        extract_question = qna_df['question'][max_idx]
        extract_answer = qna_df['answer'][max_idx]
        extract_sim = cos_sim_matrix[max_idx]
        extract_ref = qna_df['reference'][max_idx]

        return extract_question, extract_answer, extract_sim, extract_ref


if __name__ == "__main__":
    preprocessor = Preprocessing()
    chatbot = QnAchatbot()

    prepro_data_file_name = "prepro_qna_ver2.csv"
    qna_df = chatbot.load_data(prepro_data_file_name)
    embedding_list = [chatbot.embedding_sentence(prepro_q)[0].tolist() for prepro_q in qna_df['prepro_question']]

    while True:
        input_text = input("개인정보 보호와 관련하여 궁금하신 내용을 질문해주세요 : ")
        prepro_text = preprocessor.preprocess_text(input_text)
        extract_q, extract_a, extract_sim, extract_ref = chatbot.extract_answer_by_cosine_simmility(prepro_text,
                                                                                                   embedding_list,
                                                                                                    qna_df)
        if extract_sim > 0.8:
            print('\n[답변]')
            print(f'{extract_a}\n')
            print(f'관련 근거 : {extract_ref}\n\n')
            print('-' * 50)
            print(f'선택된 질문 : {extract_q}')
            print(f'유사도 : {extract_sim}')
            print('-' * 50)
            print()
        else:
            print('\n[답변]')
            print("입력 주신 질문은 개인정보와 관련 없거나 아직 학습이 부족한 영역으로 보입니다.\n부족한 부분은 추후 업그레이드 후 선보이겠습니다 감사합니다.\n\n")
            print('-' * 50)
            print(f'선택된 질문 : {extract_q}')
            print(f'유사도 : {extract_sim}')
            print('-' * 50)
