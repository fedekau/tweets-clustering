#!/usr/bin/python
# -*- coding: utf-8 -*-

from orator import Model
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import re

class Tweet(Model):
    pass

    def tokenize(self):
	tknzr = TweetTokenizer()
	return tknzr.tokenize(self.data['text'])

    def hashtags(self):
	hashtags = []
	for hashtag in self.data['entities']['hashtags']:
	    hashtags.append(hashtag['text'])
	return hashtags


    def mentions(self):
	mentions = []
	for mention in self.data['entities']['user_mentions']:
	    mentions.append(mention['screen_name'])
	return mentions

    @staticmethod
    def remove_stopwords(tokens):
	return [word for word in tokens if word not in stopwords.words('spanish')]

    @staticmethod
    def remove_links(tokens):
	words = list()
	for token in tokens:
	   urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', token)
	   if len(urls) == 0:
	       words.append(token)
	return words

    @staticmethod
    def remove_punctuation(tokens):
	punctuation = ['¡', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '¿', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', "'"]

	return [word for word in tokens if word not in punctuation]

    def matching_words_distance(self, other):
	self_tokens = self.tokenize_and_clean()
	other_tokens = other.tokenize_and_clean()
	print str(self_tokens)
	print str(other_tokens)

	return 1.0 / (len(set(self_tokens).intersection(other_tokens)) or 1)


    def tokenize_and_clean(self):
      tokens = self.tokenize()
      tokens = Tweet.remove_stopwords(tokens)
      tokens = Tweet.remove_links(tokens)
      tokens = Tweet.remove_punctuation(tokens)
      return tokens

