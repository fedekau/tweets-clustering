import word2vec
import pdb
from models.tweet import Tweet

print "Iniciando"
model = word2vec.load('/Users/federico/proyecto_grado/corpora/clean_corpus/spanish_billion_words/all.bin')
print "Modelo cargado"

def expandir_a_parecidos(tweet):
    tokens = tweet.tokenize_and_clean()
    tweet_expandido = set()

    for t in tokens:
	t = t.encode('utf8')
	if model.__contains__(t):
	    indexes, metrics = model.cosine(t)
	    parecidos_t = model.vocab[indexes][:3]
	    tweet_expandido |= set(parecidos_t)

    return tweet_expandido

tweets = Tweet.all()[:110]
target_tweet = tweets[100]

print "Target tweet text"
print target_tweet.data['text']

target_tweet_expandido = expandir_a_parecidos(target_tweet)

print "Target tweet expandido"
print target_tweet_expandido

closest_tweet = None
max_palabras_iguales = 0

for candidate in tweets:
    candidate_expandido = expandir_a_parecidos(candidate)
    palabras_iguales = len(candidate_expandido.intersection(target_tweet_expandido))
    if palabras_iguales > max_palabras_iguales:
	max_palabras_iguales = palabras_iguales
	closest_tweet = candidate
	print "Nuevo tweet cercano"
	print candidate_expandido

