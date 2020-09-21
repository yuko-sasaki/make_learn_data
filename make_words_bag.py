import pickle

from config import TRAIN_DATA_PATH, WORDS_BAG_PATH

def make_words_bag():
    with open(TRAIN_DATA_PATH, mode='rb') as f:
        train_data = pickle.load(f)
    train_words = []
    for sentence in train_data:
        train_words.extend(sentence)
    train_words = list(set(train_words))
    with open(WORDS_BAG_PATH, mode='wb') as f:
        pickle.dump(train_words, f)
    return train_words

if __name__ == "__main__":
    wb = make_words_bag()
    print(wb)
