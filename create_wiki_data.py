import pathlib
import pickle
import pprint
import re

from config import N_INCLUDE_WORD
import get_excel_words as ge

def get_files_list():
    wiki_pathes = []
    for i in range(65, 68):
        for j in range(65, 91):
            wiki_pathes.extend( list(pathlib.Path('../wikipedia/' + chr(i) + chr(j)).glob('*')))
            if i == 67 and j == 75:
                break
    return wiki_pathes

def search_wiki_files(wiki_pathes, excel_words):
    wiki_sentences = []
    for wiki_path in wiki_pathes:
        with open(wiki_path, mode='r', encoding="utf-8") as f:
            wiki_text = f.read()
            if is_open_file(wiki_text, excel_words):
                print(reform_text(wiki_text))
                print("*********************")
                wiki_sentences.append(reform_text(wiki_text))
    return wiki_sentences

def is_open_file(wiki_text, excel_words):
    i = 0
    for excel_word in excel_words:
        if excel_word in wiki_text:
            i += 1
    if i >= N_INCLUDE_WORD:
        return True
    else:
        return False

def reform_text(textx):
    textx = re.sub('</doc>', '', textx)
    textx = re.sub('<doc.{1,}>', '', textx)
    textx = re.sub('.{1,}[^。]\n', '', textx)
    textx = re.sub('[※\n]', '', textx)
    return textx


if __name__ == '__main__':
    excel_words = ge.make_cell_list()
    excel_words = ge.make_words_list(excel_words)
    wiki_pathes = get_files_list()
    wiki_sentences = search_wiki_files(wiki_pathes, excel_words)
    #pprint.pprint(wiki_sentences)
    print(len(wiki_sentences))
    with open("../wiki_sentences_860.pickle", mode='wb') as f:
        pickle.dump(wiki_sentences, f)
