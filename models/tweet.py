from orator import Model
from nltk.tokenize import TweetTokenizer

class Tweet(Model):
    pass

    def tokens(self):
	tknzr = TweetTokenizer()
	return tknzr.tokenize(self.data['text'])
