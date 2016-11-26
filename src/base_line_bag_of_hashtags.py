from models.person import Person

tweets = Person.find(5).tweets.take(500)

clusters = {}
clusters_tweets = {}

for tweet in tweets:
    hashtags = tweet.hashtags()

    assigned_cluster = False

    for cluster in clusters:
        cluster_hashes = clusters.get(cluster)

        if set(hashtags) == set(cluster_hashes):
            clusters_tweets[cluster].append(tweet)
            assigned_cluster = True
            break

    if not assigned_cluster:
        clusters[str(hashtags)] = hashtags
        clusters_tweets[str(hashtags)] = [tweet]

print('Cantidad de clusters: ' + str(len(clusters)))

for cluster in clusters_tweets:
    print('Cluster id: ' + str(cluster))
    tweets_for_cluster = clusters_tweets.get(cluster)

    for tweet in tweets_for_cluster:
        print('\t' + tweet.data['text'])
    print('------------------------------------------------------------------------------------------------')



