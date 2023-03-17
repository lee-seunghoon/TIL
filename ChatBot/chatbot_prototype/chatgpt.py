import re
import os
import openai
import pandas as pd
import tiktoken
from preprocess_text import Preprocessing
from chatbot import QnAchatbot

preprocessor = Preprocessing()
chatbot = QnAchatbot()

def num_tokens_from_messages(messages, model="gpt-3.5-turbo"):
  """Returns the number of tokens used by a list of messages."""
  try:
      encoding = tiktoken.encoding_for_model(model)
  except KeyError:
      encoding = tiktoken.get_encoding("cl100k_base")
  if model == "gpt-3.5-turbo":  # note: future models may deviate from this
      num_tokens = 0
      for message in messages:
          num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
          for key, value in message.items():
              num_tokens += len(encoding.encode(value))
              if key == "name":  # if there's a name, the role is omitted
                  num_tokens += -1  # role is always required and always 1 token
      num_tokens += 2  # every reply is primed with <im_start>assistant
      return num_tokens
  else:
      raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.
  See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")

def chatGptSample(api_key: str, embedding_list: list, filter_words_list: list, ref_df: pd.DataFrame):
    openai.api_key = api_key
    user_content = re.sub(" +", ' ', input("Question: ")).lower()

    for word in filter_words_list:
        if word.lower() in user_content.replace(' ', ''):
            prepro_text = preprocessor.preprocess_text(user_content)
            extract_question, extract_answer, extract_sim, extract_ref_url = \
                chatbot.extract_answer_by_cosine_simmility(prepro_text, embedding_list, ref_df)
            result = f"{extract_answer}\n\n자세한 내용은 다음 url 링크를 통해 확인해주세요 → {extract_ref_url}"
            return result

    input_message = [{
        "role": "user",
        "content": f"{user_content}"
    }]
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=input_message
    )
    assistant_content = (completion.choices[0].message['content'].strip())
    return assistant_content

if __name__ == '__main__':
    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
    data_file_name = "data.csv"
    info_df = chatbot.load_data(data_file_name)
    embedding_list = [chatbot.embedding_sentence(prepro_q)[0].tolist() for prepro_q in
                      info_df['prepro_question']]
    filter_words = ['Test']
    while True:
        chatbot_answer = chatGptSample(OPENAI_API_KEY, embedding_list, filter_words)
        print(f"GPT:\n{chatbot_answer}\n")