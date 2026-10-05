import nltk
from nltk.stem import PorterStemmer
()
stemmer = PorterStemmer()

words = ['walking','jumps','jumped','jumping']
for word in words:
    stemmer_word = stemmer.stem(word)
    print(f'{word} -> {stemmer_word}')