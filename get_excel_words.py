from collections import defaultdict
from janome.tokenizer import Tokenizer
import pandas as pd
import pprint
import re

from config import EXCEL_NAME, SHEET_NAMES


def is_number(wordx):
    return re.search('[a-zA-Z0-9-－%()【】「」　]+', wordx)

df = pd.read_excel(EXCEL_NAME, sheet_name = None , header = None)

excel_words = []
for sheet_name in SHEET_NAMES:
    for index, row in df[sheet_name].iterrows():
        for cell in row:
            if type(cell) is str:
                excel_words.append(cell)
    excel_words.append(sheet_name)

excel_words = list(set(excel_words))
#print(words)
#print(words[0])

t = Tokenizer(mmap=True)

# 分かち書きして特定の品詞除く方法
wakati_words = []
for word in excel_words:
    for token in t.tokenize(word):
        if "記号" in token.part_of_speech or "記号" in token.part_of_speech:#  or "助" in token.part_of_speech
            continue
        if is_number(token.surface):#  or len(token.surface) < 2
            continue
        """
        if "名" in token.part_of_speech:
            wakati_words.append(token.surface)"""
        wakati_words.append(token.surface)
wakati_words = list(set(wakati_words))
pprint.pprint(wakati_words)


# 数で並べ替える
wakati_dict = defaultdict(int)
for word in excel_words:
    for token in t.tokenize(word):
        if "記号" in token.part_of_speech or "記号" in token.part_of_speech:# or "助" in token.part_of_speech
            continue
        if is_number(token.surface):# or len(token.surface) < 2
            continue
        """
        if "名" in token.part_of_speech:
            wakati_dict[token.surface] += 1"""
        wakati_dict[token.surface] += 1

pprint.pprint(wakati_dict)
print(len(wakati_words))
print(len(wakati_dict))
