from models.tweet import Tweet
import random

# compile documents
doc_complete = [i for i in Tweet.all() if "mujica" in i.data['text'].lower()]

from nltk.stem import SnowballStemmer
lemma = SnowballStemmer("spanish")

def clean(tweet):
    return ' '.join(tweet.tokenize_and_clean())

doc_clean = [clean(tweet).split() for tweet in doc_complete]

# Importing Gensim
import gensim
from gensim import corpora

# Creating the term dictionary of our courpus, where every unique term is assigned an index.
dictionary = corpora.Dictionary(doc_clean)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=5, id2word = dictionary, passes=100)

print(ldamodel.print_topics(num_topics=5, num_words=4))
