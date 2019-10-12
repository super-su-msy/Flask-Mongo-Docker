# import spacy

# nlp = spacy.load('en_core_web_sm')
# txt = nlp('This is Karan')

import en_core_web_sm

nlp = en_core_web_sm.load()
doc = nlp("This is a sentence.")

print('just checking = {}', doc)