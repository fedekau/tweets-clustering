from models.tweet import Tweet

# compile documents
doc_complete = [i.data['text'] for i in Tweet.all() if "@LuisSuarez9" in i.data['text']]


from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import string
stop = set(stopwords.words('spanish'))
exclude = set(string.punctuation)
lemma = SnowballStemmer("spanish")

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    # normalized = " ".join(lemma.stem(word) for word in punc_free.split())
    return punc_free

doc_clean = [clean(doc).split() for doc in doc_complete]

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
ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=100)

print(ldamodel.print_topics(num_topics=3, num_words=3))
