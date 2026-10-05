import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


text = "During tokenization, the parser identifies sequences of characters which represent words and other elements, such as punctuation, which are represented by numeric codes, some of which are non-printing control characters"

words = word_tokenize(text)

stopwords = set(stopwords.words("english"))

filiter_words = [word for word in words if not word in stopwords]

words= filiter_words

#Stemming
stemmer = PorterStemmer()
stemmer_words = [stemmer.stem(word) for word in words]
print(stemmer_words)

#Lemmatization
Lemmatizer = WordNetLemmatizer()
Lemmatizer_words = [Lemmatizer.lemmatize(word) for word in words]
print(Lemmatizer_words)