from janome.tokenizer import Tokenizer
import pickle
import pprint

from config import SELECT_DATA_PATH, SEPARATOR, TRAIN_DATA_PATH

t = Tokenizer()

def make_sentence_list():
    with open(SELECT_DATA_PATH, mode='rb') as f:
        select_data = pickle.load(f)

    data_sentences = []
    for data in select_data:
        data = data.split(SEPARATOR)
        data.pop()
        data = [data + SEPARATOR for data in data]
        data_sentences.extend(data)
    return data_sentences

def make_train_data(data_sentences):
    train_data = []
    for sentence in data_sentences:
        train_data.append(make_wakati_list(sentence))
    print(train_data)
    return train_data


def make_wakati_list(sentencex):
    return [ token.surface for token in t.tokenize(sentencex)]



if __name__ == "__main__":
    data_sentences = make_sentence_list()
    train_data = make_train_data(data_sentences)
    with open(TRAIN_DATA_PATH, mode='wb') as f:
        pickle.dump(train_data, f)
