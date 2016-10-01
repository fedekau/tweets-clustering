from orator import Model
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import re

class Tweet(Model):
    pass

    def tokens(self):
	tknzr = TweetTokenizer()
	return tknzr.tokenize(self.data['text'])

    def without_stopwords(self):
	return [word for word in self.tokens() if word not in stopwords.words('spanish')]

    def remove_links(self):
	words = list()
	for token in self.tokens():
	   urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', token)
	   if len(urls) == 0:
	       words.append(token)
	return words
