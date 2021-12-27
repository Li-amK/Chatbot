import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import string

print('Laila Awakes. Process 1 initialised...')

f = open('brain.txt', 'r', errors='ignore')

raw = f.read()

raw = raw.lower()

sent_tokens = nltk.sent_tokenize(raw)

word_tokens = nltk.word_tokenize(raw)

print('Process 1 Completed!')
print('All Tokens have been created!')
print('You can now talk to me!')
print('================================')

lemmer = nltk.stem.WordNetLemmatizer()


def lemtokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def lemnormalize(text):
    return lemtokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREETING_INPUTS = ('hello', 'hi', 'greetings', 'sup', 'sup?', "what's up", 'wassup?', 'hey', 'how are you?')

GREETING_RESPONSES = ['hi', 'hey', 'hello there', 'hello', 'Yay! Someone is talking to me']


def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


def response(user_response):
    laila_response = ''

    TfidfVec = TfidfVectorizer(tokenizer=lemnormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if req_tfidf == 0:
        laila_response = laila_response + "I am sorry! I don't understand you"
        return laila_response
    else:
        laila_response = laila_response + sent_tokens[idx]
        return laila_response


flag = True
print("LAIla: My name is Laila. I will try and talk to you as best i can. Please excuse me if i make mistakes. If you want to exit, type Bye!")

while flag:
    user_response = input()
    user_response = user_response.lower()
    if user_response != 'bye':
        if user_response == 'thanks' or user_response == 'thank you':
            flag = False
            print("LAIla: You're welcome.")
        else:
            if greeting(user_response) is not None:
                print("LAIla: " + greeting(user_response))
            else:
                sent_tokens.append(user_response)
                word_tokens = word_tokens + nltk.word_tokenize(user_response)
                final_words = list(set(word_tokens))
                print('LAIla: ', end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print('LAIla: Bye! See ya next time!')
