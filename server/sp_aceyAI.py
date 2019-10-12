import spacy

nlp = spacy.load('en_core_web_sm')
txt = nlp('This is Karan')

print([(w.text, w.pos_) for w in txt])