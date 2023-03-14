import re
import os
import pandas as pd
from konlpy.tag import Okt
from argparse import ArgumentParser
from consts import DATA_DIR

class Preprocessing:
    def __init__(self):
        self.okt = Okt()
        self.data_dir = DATA_DIR


    def preprocess_text(self, text: str):
        """
        전처리 함수
        - 2자리 이상 공백 제거
        - 특수기호 제거
        - 조사 제거
        """
        prepro_text = re.sub(" +", " ", re.sub(r"[^가-힣a-zA-Z0-9]", " ", text))
        remove_tag = ['Josa']
        tokens = []
        for token, tag in self.okt.pos(prepro_text):
            if tag not in remove_tag:
                tokens.append(token)
        result = ' '.join(tokens)
        return result


    def preprocess_data(self, file_name: str):
        """
        df -> 전처리 할 데이터프레임
        """
        data_path = os.path.join(self.data_dir, file_name)
        df = pd.read_csv(data_path, encoding='utf-8')
        try:
            df['prepro_question'] = df['question'].map(self.preprocess_text)
            print(f'{data_path} 데이터 전처리 완료')
            return df
        except:
            print('현재 전처리하려는 데이터의 column title을 다시 한 번 확인해주세요. question이 아니면 오류가 발생합니다.')


    def save_prepro_df(self, df: pd.DataFrame, file_name: str):
        """
        데이터프레임을 csv로 로컬 저장
        """
        save_file_path = os.path.join(self.data_dir, file_name)
        df.to_csv(save_file_path, index=False, encoding='utf-8')
        print('전처리 데이터 csv 파일 저장 완료 -> 경로 :', save_file_path)


if __name__ == "__main__":
    processor = Preprocessing()

    parser = ArgumentParser()
    parser.add_argument('--data', required=True, help='csv file name to preprocess question text')
    parser.add_argument('--save_data_name', required=True, help='new file name to save preprocessed data')
    args = parser.parse_args()

    # 새로운 question text 전처리
    prepro_df = processor.preprocess_data(args.data)
    # 전처리한 데이터 csv 파일로 저장
    processor.save_prepro_df(prepro_df, args.save_data_name)
