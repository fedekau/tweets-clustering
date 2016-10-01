from orator import Model
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords

class Tweet(Model):
    pass

    def tokens(self):
	tknzr = TweetTokenizer()
	return tknzr.tokenize(self.data['text'])

    def without_stopwords(self):
	return [word for word in self.tokens() if word not in stopwords.words('spanish')]
