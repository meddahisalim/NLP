"""
Part-of-speech (POS) tagging is a fundamental task in natural language processing (NLP) that involves identifying the grammatical category of each word in a given text. There are several reasons why POS tagging is important in NLP:

Parsing: POS tagging is a crucial step in syntactic parsing, which involves analyzing the structure of a sentence to determine its meaning. By identifying the part of speech of each word in a sentence, we can construct a parse tree that represents the syntactic structure of the sentence.

Information retrieval: POS tagging can be used to improve the accuracy of information retrieval systems. By identifying the part of speech of a query term, we can narrow down the search space and retrieve only the relevant documents.

Machine translation: POS tagging can be used to improve the accuracy of machine translation systems. By identifying the part of speech of each word in a sentence, we can generate more accurate translations that preserve the grammatical structure of the original sentence.

Sentiment analysis: POS tagging can be used to improve the accuracy of sentiment analysis, which involves identifying the emotional tone of a piece of text. By identifying the part of speech of each word, we can identify words that are likely to carry sentiment and use them to predict the overall sentiment of the text.

Overall, POS tagging is an essential task in NLP that enables a wide range of applications, including parsing, information retrieval, machine translation, and sentiment analysis"""


import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Elon flew to mars yesterday. He carried biryani masala with him")

for token in doc:
    print(token," | ", token.pos_, " | ", spacy.explain(token.pos_))

doc = nlp("Wow! Dr. Strange made 265 million $ on the very first day")

for token in doc:
    print(token," | ", token.pos_, " | ", spacy.explain(token.pos_))


doc = nlp("Wow! Dr. Strange made 265 million $ on the very first day")

for token in doc:
    print(token," | ", token.pos_, " | ", spacy.explain(token.pos_), " | ", token.tag_, " | ", spacy.explain(token.tag_))
    
#In below sentences Spacy figures out the past vs present tense for quit

doc = nlp("He quits the job")

print(doc[1].text, "|", doc[1].tag_, "|", spacy.explain(doc[1].tag_))

doc = nlp("he quit the job")

print(doc[1].text, "|", doc[1].tag_, "|", spacy.explain(doc[1].tag_))

earnings_text="""Microsoft Corp. today announced the following results for the quarter ended December 31, 2021, as compared to the corresponding period of last fiscal year:

·         Revenue was $51.7 billion and increased 20%
·         Operating income was $22.2 billion and increased 24%
·         Net income was $18.8 billion and increased 21%
·         Diluted earnings per share was $2.48 and increased 22%
“Digital technology etc. is the most malleable resource at the world’s disposal to overcome constraints and reimagine everyday work and life,” said Satya Nadella, chairman and chief executive officer of Microsoft. “As tech as a percentage of global GDP continues to increase, we are innovating and investing across diverse and growing markets, with a common underlying technology stack and an operating model that reinforces a common strategy, culture, and sense of purpose.”
“Solid commercial execution, represented by strong bookings growth driven by long-term Azure commitments, increased Microsoft Cloud revenue to $22.1 billion, up 32% year over year” said Amy Hood, executive vice president and chief financial officer of Microsoft."""

doc = nlp(earnings_text)

for token in doc:
    print(token," | ", token.pos_, " | ", spacy.explain(token.pos_), " | ", token.tag_, " | ", spacy.explain(token.tag_))
    
    
earnings_text="""Microsoft Corp. today announced the following results for the quarter ended December 31, 2021, as compared to the corresponding period of last fiscal year:

·         Revenue was $51.7 billion and increased 20%
·         Operating income was $22.2 billion and increased 24%
·         Net income was $18.8 billion and increased 21%
·         Diluted earnings per share was $2.48 and increased 22%
“Digital technology is the most malleable resource at the world’s disposal to overcome constraints and reimagine everyday work and life,” said Satya Nadella, chairman and chief executive officer of Microsoft. “As tech as a percentage of global GDP continues to increase, we are innovating and investing across diverse and growing markets, with a common underlying technology stack and an operating model that reinforces a common strategy, culture, and sense of purpose.”
“Solid commercial execution, represented by strong bookings growth driven by long-term Azure commitments, increased Microsoft Cloud revenue to $22.1 billion, up 32% year over year” said Amy Hood, executive vice president and chief financial officer of Microsoft."""

doc = nlp(earnings_text)

filtered_tokens = []

for token in doc:
    if token.pos_ not in ["SPACE", "PUNCT", "X"]:
        filtered_tokens.append(token)


print(filtered_tokens[:10])

count = doc.count_by(spacy.attrs.POS)
print(count)

print(doc.vocab[96].text)

print(count.items())

for k,v in count.items():
    print(doc.vocab[k].text, "|",v)
    
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "The quick brown fox jumps over the lazy dog."

# Tokenize the text into individual words
words = nltk.word_tokenize(text)

# Perform POS tagging on the tokenized words
pos_tags = nltk.pos_tag(words)

# Print the POS tags for each word
for word, tag in pos_tags:
    print(word, tag)