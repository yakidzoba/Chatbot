''' 
This is the primary flask app that srves up the data for the chatbot.
This is also the application that serves up the html page which is most of what the users will hit against.
'''

from flask import Flask, render_template, request, url_for, redirect
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)


# Read only. Use this to test the trainings. WILL NOT TRAIN HERE.

#chatterbot = ChatBot("Chatterbot", read_only=True)

# Use this to TRAIN the chatbot
chatte = ChatBot("Chatterbot")

# Training
#chatterbot = ChatBot("Rocket", storage_adapter="chatterbot.storage.SQLStorageAdapter")

########################################################################################################################
'''
chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train(
    "chatterbot.corpus.english.greetings"
)
'''
########################################################################################################################

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/get')
def get_bot_reponse():
    '''userText = request.args.get('msg')'''
    return str('hi')

'''
    if botResponse.confidence > 0.5:
        return str(botResponse) + str(botResponse.confidence)
    else:
        return ' I do not know what you mean'
'''
########################################################################################################################

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8080)