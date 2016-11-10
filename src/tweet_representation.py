from __future__ import print_function
from models.tweet import Tweet

tweets = [i for i in Tweet.all() if "@LuisSuarez9" in i.data['text']]

for candidate in tweets:
    tokens = candidate.tokenize_and_clean()
    print("TWEET: " + candidate.data['text'] + " ===> " + str(tokens))
    print("---------------------------------------------------------")
