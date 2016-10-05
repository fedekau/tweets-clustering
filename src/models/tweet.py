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
	punctuation = ['¡', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '¿', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

	return [word for word in tokens if word not in punctuation]
