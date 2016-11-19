from __future__ import print_function
from models.tweet import Tweet
from models.person import Person
from lemmas.lemmatizer import Lemmatizer

tweets = Person.where('name', 'Luis Suarez').first().tweets.all()
# tweets = [i for i in Tweet.all() if "@LuisSuarez9" in i.data['text']]

l = Lemmatizer('/Users/federico/proyecto_grado/tweets-clustering/src/training/corpora/lemmas/lemmatization-es-no-numbers.txt')

for candidate in tweets:
    tokens = candidate.tokenize_and_clean()
    tokens = l.lemmatize(tokens)
    print("TWEET: " + candidate.data['text'] + " ===> " + str(tokens))
    print("---------------------------------------------------------")
