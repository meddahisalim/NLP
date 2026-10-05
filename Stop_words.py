import nltk
# nltk.download("stopwords")

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

print(stopwords.words("english"))

text = "During tokenization, the parser identifies sequences of characters which represent words and other elements, such as punctuation, which are represented by numeric codes, some of which are non-printing control characters"

words = word_tokenize(text)

stopwords = set(stopwords.words("english"))

filiter_words = [word for word in words if not word in stopwords]

filiter_text = ' '.join(filiter_words)

print(text)
print(5*'#')
print(filiter_text)
