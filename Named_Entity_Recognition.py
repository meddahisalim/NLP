import spacy 

nlp = spacy.load("en_core_web_sm")
# print(nlp.pipe_names)

# doc = nlp("Tesla Inc is going to acquire x.com for $45 billion")
# #doc.ents contient les entités nommées détectées par spaCy.
# print(doc.ents)

# for ent in doc.ents:
#     print(ent.text, " | ", ent.label_, " | ", spacy.explain(ent.label_))
    
    
# from spacy import displacy

# print(displacy.render(doc, style="dep"))

# #List down all the entities

# print(nlp.pipe_labels['ner'])

# doc = nlp("Michael Bloomberg founded Bloomberg in 1982")
# print(doc.ents)

# doc = nlp("Michael Bloomberg founded Bloomberg in 1982")
# for ent in doc.ents:
#     print(ent.text, "|", ent.label_, "|", spacy.explain(ent.label_))
    

# doc = nlp("Tesla Inc is going to acquire Twitter Inc for $45 billion")
# for ent in doc.ents:
#     print(ent.text, " | ", ent.label_, " | ", ent.start_char, "|", ent.end_char)

# doc = nlp("Tesla is going to acquire Twitter for $45 billion")
# for ent in doc.ents:
#     print(ent.text, " | ", ent.label_)

# s = doc[2:5]
# print(s)
# print(type(s))

# from spacy.tokens import Span

# s1 = Span(doc, 0, 1, label="ORG")
# s2 = Span(doc, 5, 6, label="ORG")

# doc.set_ents([s1, s2], default="unmodified")
# for ent in doc.ents:
#     print(ent.text, " | ", ent.label_)

import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# Define input text
input_text = "Steve Jobs was the CEO of Apple Corp. in California."

# Tokenize input text
tokens = word_tokenize(input_text)

# Perform Part-of-Speech (POS) tagging
pos_tags = pos_tag(tokens)
print('pos_tags',pos_tags)

# Perform Named Entity Recognition (NER)
ne_tree = ne_chunk(pos_tags)
print('ne_tree',ne_tree)

# Extract named entities and their labels
named_entities = []
for subtree in ne_tree.subtrees():
    if subtree.label() in ['PERSON', 'ORGANIZATION', 'LOCATION']:
        named_entity = ' '.join(word for word, tag in subtree.leaves())
        print(named_entity)
        named_entities.append((named_entity, subtree.label()))

# Print named entities and their labels
print(named_entities)

for subtree in ne_tree.subtrees():
    print(subtree)
    

for word, tag in subtree.leaves():
    print(word)