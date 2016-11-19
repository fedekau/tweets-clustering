import random

from distance.distance import Distance
from gensim.models import Word2Vec
from models.tweet import Tweet
from lemmas.lemmatizer import Lemmatizer

from models.person import Person
print ("Iniciando")
model = Word2Vec.load('/Users/federico/proyecto_grado/tweets-clustering/src/training/models/PY3-W2V-1B-ES-100.bin')
print ("Modelo cargado")

tweets = Person.where('name', 'Luis Suarez').first().tweets.all()
# tweets = Tweet.all()
# target_tweet = Tweet.where('tweet_id', '=', '789142606064324608').first()
target_tweet = tweets[0]

print ("---------------------------------------------")
print ("TARGET TWEET TEXT")
print (target_tweet.data['text'])

# l = Lemmatizer('/Users/federico/proyecto_grado/tweets-clustering/src/training/corpora/lemmas/lemmatization-es-no-numbers.txt')
distance = Distance(model, None, True)

tweet_ordered = []

for candidate in tweets:
    d = distance.cosine(candidate, target_tweet)
    tweet_ordered.append([d, candidate])

def getKey(item):
    return item[0]

tweet_ordered = sorted(tweet_ordered, key=getKey)

for t in tweet_ordered:
    print("DISTANCE: " + str(t[0]) + "ID: " + str(t[1].tweet_id) + " TWEET: " + t[1].data['text'] + ' ===> TOKENS: ' + str(t[1].tokenize_and_clean()))

