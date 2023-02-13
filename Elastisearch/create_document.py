"""

This script creates documents in the required format for
indexing.

"""

import json
import re
from pandas import read_csv
from argparse import ArgumentParser

PATTERN = '[^\w\s]'
PATTERN_MULTI_SPACE = ' +'
REPL = " "

def isNaN(string):
    return string != string

def create_document(doc, index_name):
    return {
        '_op_type': 'index',
        '_index': index_name,
        'title': doc['title'],
        'purpose': doc['purpose'],
    }


def load_dataset(path):
    docs = []
    df = read_csv(path)
    df.columns = df.columns.str.lower()
    for row in df.iterrows():
        series = row[1]
        title = series.title
        purpose = series.purpose
        if title or purpose :
            if isNaN(title) : title = REPL
            if isNaN(purpose) : purpose = REPL
            qu = re.sub(pattern=PATTERN, repl=REPL, string=str(title))
            qu = re.sub(pattern=PATTERN_MULTI_SPACE, repl=REPL, string=qu)
            if qu!=REPL :
               qu=str(qu).strip()
            doc = {
              'title': qu,
              'purpose': purpose
            }
            docs.append(doc)
    return docs


def main(args):
    docs = load_dataset(args.csv)
    with open(args.output, 'w') as f:
        for doc in docs:
            d = create_document(doc, args.index)
            f.write(json.dumps(d) + '\n')

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument('--index', required=True, help='name of the ES index')
    parser.add_argument('--csv', required=True, help='path to the input csv file')
    parser.add_argument('--output', required=False, help='name of the output file (example.json1)')
    args = parser.parse_args()
    main(args)

