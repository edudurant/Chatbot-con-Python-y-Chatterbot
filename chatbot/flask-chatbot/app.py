from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response
from flask import Flask, render_template, request
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

bot = ChatBot('HAL3000',
    logic_adapters=[
        {
            'import_path':'chatterbot.logic.BestMatch',
            'maximum_similarity_threshold': 0.65,
            'default_response':'Perdoname, pero no logro entenderte',
            'response_selection_method': get_random_response,
        },
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    read_only=True
)

trainer = ChatterBotCorpusTrainer(bot)
# trainer.train('chatterbot.corpus.spanish')
docs = ['ai.yml','chisme.yml','ciencia.yml','comida.yml','computadoras.yml','deporte.yml','dinero.yml','emocion.yml','historia.yml','humor.yml','literatura.yml','personalidad.yml','politica.yml','salud.yml']
for doc in docs:
    trainer.train(f'./corpus/{doc}')

@app.get('/')
def home():
    return render_template('home.html')

@app.get('/get')
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

if __name__ == '__main__':
    app.run()