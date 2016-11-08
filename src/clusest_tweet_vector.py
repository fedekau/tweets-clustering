import random

from distance.distance import Distance
from gensim.models import Word2Vec
from models.tweet import Tweet

print ("Iniciando")
model = Word2Vec.load('/Users/federico/proyecto_grado/tweets-clustering/src/training/models/trained_models/W2V-1B-ES-500.bin')
print ("Modelo cargado")

tweets = [i for i in Tweet.all() if "@LuisSuarez9" in i.data['text']]
# tweets = Tweet.all()
target_tweet = random.sample(tweets, 1)[0]

print ("---------------------------------------------")
print ("TARGET TWEET TEXT")
print (target_tweet.data['text'])

distance = Distance(model)

tweet_ordered = []

for candidate in tweets:
    d = distance.vector(candidate, target_tweet)
    tweet_ordered.append([d, candidate])

def getKey(item):
    return item[0]

tweet_ordered = sorted(tweet_ordered, key=getKey)

for t in tweet_ordered:
    print("DISTANCE: " + str(t[0]) + " TWEET: " + t[1].data['text'])
