import discord
from discord.ext import commands
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import string

client = commands.Bot(command_prefix=commands.when_mentioned_or("*"))
client.remove_command("help")


@client.event
async def on_ready():
    activity = discord.Activity(name='Menschen', type=discord.ActivityType.listening)
    await client.change_presence(activity=activity)
    print('Ich bin erfolgreich eingeloggt. Mein Name ist {}.'.format(client.user.name))


@client.event
async def on_message(message):
    if message.author.bot:
        pass
    if message.content.startswith('*Credits'):
        await message.channel.send('**KAI** wurde von Li-amK unter der Verwendung von `nltk`, `sklearn` und `discord.py` entwickelt.')
    else:
        if message.channel.id == 829696828685418536: # SPecify a Channel for Learning
            if message.content.startswith('*'):
                pass
            if message.author.bot:
                pass
            else:
                file_write = open('brain.txt', 'a', errors='ignore')
                file_write.write(message.content + '.\n')
                file_write.close()
        if message.channel.id == 829696281638207488: # Specify a Channel in wich to use Commands with KAI (in this case the same as wich to talk)
            if message.content.startswith('*dict'):
                dict_file = discord.File('brain.txt', filename='Dictionary of KAI.txt')
                await message.channel.send(file=dict_file)
        if message.channel.id == 829696281638207488: # Specify a Channel in wich to talk with KAI
            if message.content.startswith('*'):
                pass
            if message.author.bot:
                pass
            else:
                async with message.channel.typing():
                    file_process = open('brain.txt', 'r', errors='ignore')
                    raw = file_process.read()
                    raw = raw.lower()
                    sent_tokens = nltk.sent_tokenize(raw)
                    word_tokens = nltk.word_tokenize(raw)

                    lemmer = nltk.stem.WordNetLemmatizer()

                    def lemtokens(tokens):
                        return [lemmer.lemmatize(token) for token in tokens]

                    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

                    def lemnormalize(text):
                        return lemtokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

                    greeting_inputs = ('hallo', 'hi')

                    greeting_responses = ['hi', 'hey', 'hello there', 'hello', 'Yay! Jemand redet mit mir!']

                    def greeting(sentence):
                        for word in sentence.split():
                            if word.lower() in greeting_inputs:
                                return random.choice(greeting_responses)

                    def response(user_response):
                        kai_response = ''

                        TfidfVec = TfidfVectorizer(tokenizer=lemnormalize, stop_words='english')
                        tfidf = TfidfVec.fit_transform(sent_tokens)
                        vals = cosine_similarity(tfidf[-1], tfidf)
                        idx = vals.argsort()[0][-2]
                        flat = vals.flatten()
                        flat.sort()
                        req_tfidf = flat[-2]

                        if req_tfidf == 0:
                            kai_response = kai_response + "<:x:> Sorry! Das habe ich nicht verstanden!"
                            return kai_response
                        else:
                            kai_response = kai_response + sent_tokens[idx]
                            return kai_response

                    user_response = message.content
                    user_response = user_response.lower()
                    if greeting(user_response) is not None:
                        print("KAI: " + greeting(user_response))
                        await message.channel.send(greeting(user_response))
                    else:
                        sent_tokens.append(user_response)
                        word_tokens = word_tokens + nltk.word_tokenize(user_response)
                        print('KAI: ', end="")
                        print(response(user_response))
                        await message.channel.send(response(user_response))
                        sent_tokens.remove(user_response)
        else:
            pass


# ©Li-amK 2021
client.run("TOKEN")
