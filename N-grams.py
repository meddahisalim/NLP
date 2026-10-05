from sklearn.feature_extraction.text import CountVectorizer

v = CountVectorizer()
v.fit(["Thor Hathodawala is looking for a job"])
print(v.vocabulary_)

v = CountVectorizer(ngram_range=(1,1))
v.fit(["Thor Hathodawala is looking for a job"])
print(v.vocabulary_)

v = CountVectorizer(ngram_range=(1,2))
v.fit(["Thor Hathodawala is looking for a job"])
print(v.vocabulary_)

v = CountVectorizer(ngram_range=(1,3))
v.fit(["Thor Hathodawala is looking for a job"])
print(v.vocabulary_)

#We will take a simple collection of text documents, preprocess them to remove stop words, lemmatize etc and then generate bag of 1 grams and 2 grams from it

corpus = [
    "Thor ate pizza",
    "Loki is tall",
    "Loki is eating pizza"
]

import spacy

# load english language model and create nlp object from it
nlp = spacy.load("en_core_web_sm") 

def preprocess(text):
    # remove stop words and lemmatize the text
    doc = nlp(text)
    filtered_tokens = []
    for token in doc:
        if token.is_stop or token.is_punct:
            continue
        filtered_tokens.append(token.lemma_)
    
    return " ".join(filtered_tokens) 

print(preprocess("Loki is eating pizza"))

corpus_processed = [
    preprocess(text) for text in corpus
]
print(corpus_processed)

v.transform(["Thor eat pizza"]).toarray()
print(v)