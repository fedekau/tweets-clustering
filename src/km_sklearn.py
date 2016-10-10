from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

sentence_list=['hello how are you', "I am doing great", "my name is abc"]

vectorizer=TfidfVectorizer(min_df=1, max_df=0.9, stop_words='english', decode_error='ignore')
vectorized=vectorizer.fit_transform(sentence_list)

km=KMeans(n_clusters=num_clusters, init='k-means++',n_init=10, verbose=1)
km.fit(vectorized)
