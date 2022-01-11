from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

kai = ChatBot(name='KAI', logic_adapters=
['chatterbot.logic.MathematicalEvaluation',
 'chatterbot.logic.BestMatch'])

small_talk = ['hi there!',
              'how is your day?',
              'what are you doing?',
              'always!',
              'all fine thanks',
              'i\'m created by Liam',
              'superb!',
              'oh...i \'m sorry  to hear that',
              'Wha\'s your name?',
              'nah not today',
              'i\'m fantastic!']

math_talk = ['law of cosines',
             'c**2 = a**2 + b**2 - 2 * a *b * cos(gamma)']

list_trainer = ListTrainer(kai)

for item in (small_talk, math_talk):
    list_trainer.train(item)

print(kai.get_response("Hello"))
