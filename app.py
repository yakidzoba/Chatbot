from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

chatbot = ChatBot("Rocket", storage_adapter="chatterbot.storage.SQLStorageAdapter")

chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("./training/")

########################################################################################################################

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    botResponse = chatbot.get_response(userText)

    if botResponse.confidence > 0.5:
        return str(botResponse) + ' Confidence level: ' + str(botResponse.confidence)
    else:
        return ' I do not know what you mean.' + ' Confidence level: ' + str(botResponse.confidence)

########################################################################################################################

if __name__ == "__main__":
    app.run()