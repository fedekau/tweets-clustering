from models.person import Person

person = Person.find(5)
tweets = person.tweets.take(100)

print('Person name: ' + str(person.name))
print('Number of tweets: ' + str(len(tweets)))

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

cluster_sizes = list(map(len, clusters_tweets.values()))
average = sum(cluster_sizes) / len(clusters_tweets.values())
smallest_cluster = min(cluster_sizes)
biggest_cluster = max(cluster_sizes)

print('Number of clusters: ' + str(len(clusters)))
print('Average number of tweets per cluster: ' + str(average))
print('Smallest cluster: ' + str(smallest_cluster))
print('Biggest cluster: ' + str(biggest_cluster) + '\n')

for cluster in clusters_tweets:
    print('Cluster id: ' + str(cluster))
    tweets_for_cluster = clusters_tweets.get(cluster)

    print('Number of tweets in cluster: ' + str(len(tweets_for_cluster)))

    for tweet in tweets_for_cluster:
        print('\t' + tweet.data['text'])
    print('------------------------------------------------------------------------------------------------')



