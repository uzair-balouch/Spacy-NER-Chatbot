# ! pip install -U spacy -q ## To update the spacy with latest version

# ! python -m spacy info ## To get the latest version of sapcy info 



## Actual Code
import spacy
from spacy.tokens import DocBin
from tqdm import tqdm

nlp = spacy.blank("en") # load a new spacy model
db =  DocBin()


import json 
f = open("tarining_data.json")
TRAIN_DATA = json.load(f)



## Code to convert from json to spacy
for text, annot in tqdm(TRAIN_DATA['annotations']):
  doc = nlp.make_doc(text)
  ents = []
  for start, end, label, in annot["entities"]:
    span = doc.char_span(start, end, label=label, alignment_mode="contract")
    if span is None:
      print("Skipping entity")
    else:
      ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("./training_data.spacy") # save the docbin object


## Code to create a config file with CLI (For CPU)
# ! python -m spacy init config congif.cfg --lang en  --pipeline ner --optimize efficiency


## Training Command (On CPU)
# ! python -m spacy train config.cfg --output ./ --paths.train ./training_data.spacy --paths.dev ./training_data.spacy



## Code to Load the Best Model (Give the path to the Best Model directory)
nlp_ner = spacy.load("")

## Put the Text in the Qoutes Which you want to predict.
doc = nlp_ner("")

## Code to display the predicted NER on text (This is in jupyter)
spacy.display.render(doc, style="ent", jupyter=True)  # display in jupyter





## To download folder from Google Colab
# !zip -r /content/model-best.zip /content/model-best