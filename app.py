from flask import Flask, render_template, request , session, redirect, url_for, jsonify ,Response, send_file,flash
import spacy

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
# @login_required
def index():
  return render_template("index.html")


ner_list = {"PERSON": ["Hi how are you?"],
        "BATHROOM ISSUE": "We will help you to fix your issue.",
        "APPOINTMENT": "Can I book an appointment for you?",
        "AUTHORITY": "Do you want to talk to the higher authority?",
        "ORG": "Welcome to our orgazination.",
        "PLACE": "Is this the city you live in.",
        "PEST": "We will fix these pest.",
        "ADDRESS": "I have saved your address.",
        "TIME": "I have noted the time to send our technicial to your address."}


@app.route("/get")
def get_bot_response():
  userText = request.args.get('msg')
  # nlp = spacy.load("en_core_web_sm")
  # # nlp = spacy.load("en_core_web_md")

  # doc = nlp(userText)
  # result_list = []
  # for entity in doc.ents:
  #   resp = entity.text + " | " + entity.label_
  #   result_list.append(resp)
  ## Code to Load the Best Model (Give the path to the Best Model directory)
  model_path = 'model-best'
  nlp_ner = spacy.load(model_path)

  ## Put the Text in the Qoutes Which you want to predict.
  doc = nlp_ner(userText)
  
  # print(ner_list.keys())

  for entity in doc.ents:
    # print(entity.text + " | " + entity.label_)
    if entity.label_ in ner_list.keys():
      # print(entity.label_)
      # print(ner_list[entity.label_])
      result = ner_list[entity.label_]




  ## Code to display the predicted NER on text (This is in jupyter)
  # result = spacy.displacy.render(doc, style="ent")  # display in jupyter
  return result



# @app.route("/get")
# def get_bot_response():
#   userText = request.args.get('msg')
#   nlp = spacy.load("en_core_web_sm")
#   # nlp = spacy.load("en_core_web_md")

#   doc = nlp(userText)
#   result_list = []
#   for entity in doc.ents:
#     resp = entity.text + " | " + entity.label_
#     result_list.append(resp)

  return result_list




if __name__ == '__main__':
  app.run(debug=True)
