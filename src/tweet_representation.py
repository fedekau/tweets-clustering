from __future__ import print_function
from models.tweet import Tweet
from lemmas.lemmatizer import Lemmatizer

tweets = [i for i in Tweet.all() if "@LuisSuarez9" in i.data['text']]
# tweets = [i for i in Tweet.all() if "@LuisSuarez9" in i.data['text']]

l = Lemmatizer('/Users/federico/proyecto_grado/tweets-clustering/src/training/corpora/lemmas/lemmatization-es-no-numbers.txt')

for candidate in tweets:
    tokens = candidate.tokenize_and_clean()
    tokens = l.lemmatize(tokens)
    print("TWEET: " + candidate.data['text'] + " ===> " + str(tokens))
    print("---------------------------------------------------------")
