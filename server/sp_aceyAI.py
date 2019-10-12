import spacy

nlp = spacy.load('en_core_web_sm')
# txt = nlp('This is Karan')

tokens = nlp("dog cat banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))