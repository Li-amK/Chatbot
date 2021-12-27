from chatterbot import ChatBot

bot = ChatBot(
              "Kai's Child",
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              database_uri='sqlite:///database.sqlite3'
              )

from chatterbot import ChatBot

bot = ChatBot(
              "Kai's Child",
              logic_adapters=[
              'chatterbot.logic.BestMatch',
              'chatterbot.logic.TimeLogicAdapter']
              )

from chatterbot import ListTrainer

trainer = ListTrainer(bot)

trainer.train([
'Hi',
'Hello',
'I need help with my order',
'Please let me know your order ID',
'I have an issue.',
'Please explain your concern.',
'Can I change the ordered items?',
'You can return the products and purchase new items in your next order.',
'Thanks',
'You’re welcome! Have a great day!'
])

response = bot.get_response('I have a Issue')
#replace parameter with input

print("Bot Response):", response)

name=input('Enter your Name: ')
print("Hi! I am Kais's Child!")

while True:
    request=input(name+':')
    if request=='Bye' or request=='bye':
        print("Kai's Child: Bye!")
        break
    else:
        response=bot.get_response(request)
        print("Kai's Child: ", response)
