import word2vec
import random
from models.tweet import Tweet

print "Iniciando"
model = word2vec.load('/Users/federico/proyecto_grado/corpora/clean_corpus/spanish_billion_words/all.bin')
print "Modelo cargado"

def expandir_a_parecidos(tweet):
    tokens = tweet.tokenize_and_clean()
    tweet_expandido = set()

    for t in tokens:
	t = t.encode('utf8')
	tweet_expandido.add(t)
	if model.__contains__(t):
	    indexes, metrics = model.cosine(t)
	    parecidos_t = model.vocab[indexes][:1]
	    tweet_expandido |= set(parecidos_t)

    return tweet_expandido

tweets = [i for i in Tweet.all() if "@ECavaniOfficial" in i.data['text']]
target_tweet = random.sample(tweets, 1)[0]

print "Target tweet text"
print target_tweet.data['text']

target_tweet_expandido = expandir_a_parecidos(target_tweet)

print "Target tweet expandido"
print target_tweet_expandido

closest_tweet = None
max_palabras_iguales = 0
closest_tweets = list()

for candidate in tweets:
    candidate_expandido = expandir_a_parecidos(candidate)
    palabras_iguales = len(candidate_expandido.intersection(target_tweet_expandido))
    if palabras_iguales > 1 and candidate.tweet_id != target_tweet.tweet_id:
	max_palabras_iguales = palabras_iguales
	closest_tweet = candidate
	print "Nuevo tweet cercano"
	print candidate.data['text']
	print max_palabras_iguales
	print candidate_expandido
	closest_tweets.append(candidate)
for c in closest_tweets:
    print c.data['text']

