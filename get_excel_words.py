
import pandas as pd
import re

from config import EXCEL_NAME, SHEET_NAMES


def remove_unwanted(wordx):
    return re.sub('[\s\R※　]', '',wordx)

def is_add_set(cellx):
    if type(cell) is str:
        return True
    else:
        return False


df = pd.read_excel(EXCEL_NAME, sheet_name = None , header = None)

words = set()
for sheet_name in SHEET_NAMES:
    for index, row in df[sheet_name].iterrows():
        for cell in row:
            if is_add_set(cell) :
                words.add(cell)
    words.add(sheet_name)

words = list(words)
print(words)
print(words[0])
