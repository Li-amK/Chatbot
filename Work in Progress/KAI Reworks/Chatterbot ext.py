from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("Kai's Child", read_only=True,
              logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                              'chatterbot.logic.BestMatch'])
trainer = ListTrainer(bot)

conversation = open('chats.txt', 'r').readline()

trainer.train(conversation)

while True:
    message = input('You:')
    if message.strip() != 'Bye':
        reply = bot.get_response(message)
    print("Kai's Child: ", reply)
    if message.strip() == 'Bye':
        print("Kai's Child: Bye!")
        break
