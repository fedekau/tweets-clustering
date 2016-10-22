import word2vec
import random
from models.tweet import Tweet
from distance.distance import Distance

print ("Iniciando")
model = word2vec.load('/Users/federico/proyecto_grado/corpora/clean_corpus/spanish_billion_words/all_no_phrase.bin')
print ("Modelo cargado")

# def get_tweets(palabras):
#     tweets = Tweet.all()
#     tweets_encontrados = set()

#     for t in tweets:
# 	for p in palabras:
# 	    if p.lower() in t.data['text'].lower():
# 		tweets_encontrados.add(t)

#     return tweets_encontrados

# tweets = get_tweets(['@LuisSuarez9', 'luisito', 'pistolero', 'luis suarez'])

tweets = [i for i in Tweet.all() if "@LuisSuarez9" in i.data['text']]
target_tweet = random.sample(tweets, 1)[0]

print ("---------------------------------------------")
print ("TARGET TWEET TEXT")
print (target_tweet.data['text'])

closest_tweet = None
closest_tweets = list()

distance = Distance(model)

for candidate in tweets:
    if distance.jaccard(candidate, target_tweet) < 0.90 and candidate.tweet_id != target_tweet.tweet_id:
	closest_tweet = candidate
	print ("NUEVO TWEET CERCANO")
	print (candidate.data['text'])
	closest_tweets.append(candidate)
	print ("---------------------------------------------")

print ("CLUSTER DE TWEETS")
for c in closest_tweets:
    print (c.data['text'])

