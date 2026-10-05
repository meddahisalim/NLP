import nltk
# nltk.download()

text = "hello! i'am meddahi salim?"
sentences = nltk.sent_tokenize(text)
tokens = nltk.word_tokenize(text)
print(sentences)
print(tokens)
