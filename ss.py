import json
import nltk
dir = r'C:\Users\admin\Desktop\intents.json'

with open(dir) as file:
    data = json.load(file)

words = []
labels = []
doc_x = []
doc_y = []


for intent in data['intents']:
    for pattern in intent['patterns']:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        doc_y.append(intent['tage'])
        doc_x.append(pattern)



    if intent['tag'] not in labels:
        labels.append(intent['tag'])


