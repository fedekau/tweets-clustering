from models.person import Person

tweets = Person.where('name', 'Luis Suarez').first().tweets.all()[:1000]

hashtags_count = {}

for tweet in tweets:
    hashtags = tweet.hashtags()

    for h in hashtags:
        count = hashtags_count.get(h)

        if count is None:
            hashtags_count[h] = 1
        else:
            hashtags_count[h] = count + 1

most_common_hashtags = sorted(hashtags_count, key=hashtags_count.__getitem__, reverse=True)

print('Hashtag count')
print(hashtags_count)

print('Hashtags ordered by frequency')
print(most_common_hashtags)

tweets_bag_representation = []

top_hashtags = most_common_hashtags[:2]

def tweet_bag_representation(tweet):
    tweet_hashtags = tweet.hashtags()

    tweet_feature = []

    for hashtag in top_hashtags:
        tweet_feature.append(1 if hashtag in tweet_hashtags else 0)

    return tweet_feature

for tweet in tweets:
    tweets_bag_representation.append(tweet_bag_representation(tweet))


print('Tweet representation with bag of hashtags')
print(tweets_bag_representation)

import numpy as np

X = np.asarray(tweets_bag_representation)


from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

db = DBSCAN(eps=0.3, min_samples=10).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d' % n_clusters_)
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels))

import matplotlib.pyplot as plt

# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = 'k'

    class_member_mask = (labels == k)

    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=6)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()
