from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('Feedbacker')


def get_feedback():
    text = input()

    if 'si' in text.lower():
        return True
    elif 'no' in text.lower():
        return False
    else:
        print('Por favor pon "si" o "no"')
        return get_feedback()

while True:
    try:
        texto_usuario = input()
        respuesta = bot.get_response(texto_usuario)

        print(f'¿Es {respuesta} una respuesta coherente a {texto_usuario}')

        if get_feedback() is False:
            print('Por favor pon la respuesta correcta')
            respuesta_correcta = input()
            
            with open('./corpus/feedbacker.yml','a',encoding='utf-8') as f:
                f.write(f'- - {texto_usuario}\n')
                f.write(f'  - {respuesta_correcta}\n')

            trainer = ChatterBotCorpusTrainer(bot)
            trainer.train('./corpus/feedbacker.yml')

            print('Respuesta añadida al bot!')
    except:
        pass