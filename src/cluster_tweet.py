import word2vec
import random
from models.tweet import Tweet

print ("Iniciando")
model = word2vec.load('/Users/federico/proyecto_grado/corpora/clean_corpus/spanish_billion_words/all_no_phrase.bin')
print ("Modelo cargado")

def jaccard_distance(set1, set2):
    distance = 1.0 - ((1.0 * len(set1.intersection(set2))) / len(set1.union(set2)))

    print ("JACCARD DISTANCE: " + str(distance))

    return distance

def expandir_a_parecidos(tweet):
    tokens = tweet.tokenize_and_clean()
    tweet_expandido = set()

    for t in tokens:
	t = t.encode('utf8')
	tweet_expandido.add(t)
	if model.__contains__(t):
	    indexes, metrics = model.cosine(t)
	    parecidos_t = model.vocab[indexes][:2]
	    tweet_expandido |= set(parecidos_t)

    return tweet_expandido

def get_tweets(palabras):
    tweets = Tweet.all()
    tweets_encontrados = set()

    for t in tweets:
	for p in palabras:
	    if p.lower() in t.data['text'].lower():
		tweets_encontrados.add(t)

    return tweets_encontrados

tweets = [i for i in Tweet.all() if "@LuisSuarez9" in i.data['text']]
# tweets = get_tweets(['@LuisSuarez9', 'luisito', 'pistolero', 'luis suarez'])
target_tweet = random.sample(tweets, 1)[0]

print ("---------------------------------------------")
print ("TARGET TWEET TEXT")
print (target_tweet.data['text'])

target_tweet_expandido = expandir_a_parecidos(target_tweet)

print ("TARGET TWEET EXPANDIDO")
print target_tweet_expandido
print ("---------------------------------------------")

closest_tweet = None
closest_tweets = list()

for candidate in tweets:
    candidate_expandido = expandir_a_parecidos(candidate)
    distancia = jaccard_distance(target_tweet_expandido, candidate_expandido)
    if distancia < 0.90 and candidate.tweet_id != target_tweet.tweet_id:
	closest_tweet = candidate
	print ("NUEVO TWEET CERCANO")
	print (candidate.data['text'])
	print (candidate_expandido)
	closest_tweets.append(candidate)
	print ("---------------------------------------------")

print ("CLUSTER DE TWEETS")
for c in closest_tweets:
    print (c.data['text'])

