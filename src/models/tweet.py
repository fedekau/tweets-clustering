#!/usr/bin/python
# -*- coding: utf-8 -*-

from orator import Model
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import re

class Tweet(Model):
    pass

    def remove_emojis(self):
        emojis = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
        return emojis.sub('', self.data['text'])

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
    def tokenize(text):
        tknzr = TweetTokenizer()
        return tknzr.tokenize(text)

    @staticmethod
    def remove_stopwords(tokens):
        return [word for word in tokens if word.lower() not in stopwords.words('spanish')]

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
        punctuation = ['¡', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '¿', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', "'", '..', '...']

        return [word for word in tokens if word not in punctuation]

    @staticmethod
    def remove_numbers(tokens):
        numbers = re.compile('^-?[0-9]+$')

        return [word for word in tokens if not numbers.match(word)]

    @staticmethod
    def remove_abbreviations(tokens):
        abbreviations = ['xq', 'd', 'c', 'q', 'x', 'desp']

        return [word for word in tokens if word not in abbreviations]

    @staticmethod
    def remove_mentions(tokens):
        mentions = re.compile('^@')

        return [word for word in tokens if not mentions.match(word)]

    @staticmethod
    def remove_hashtags(tokens):
        mentions = re.compile('^#')

        return [word for word in tokens if not mentions.match(word)]

    def matching_words_distance(self, other):
        self_tokens = self.tokenize_and_clean()
        other_tokens = other.tokenize_and_clean()

        return 1.0 - ((len(set(self_tokens).intersection(other_tokens)) or 1 / (len(self_tokens) + len(other_tokens))))

    @staticmethod
    def remove_laugh(tokens):
        laughs = re.compile(r"\b((j|a)+)\b|\b((j|e)+)\b|\b((j|i)+)\b|\b((j|o)+)\b|\b((j|u)+)\b")

        return [word for word in tokens if not laughs.match(word)]

    def tokenize_and_clean(self):
        text = self.remove_emojis()
        tokens = Tweet.tokenize(text.lower())
        tokens = Tweet.remove_stopwords(tokens)
        tokens = Tweet.remove_links(tokens)
        tokens = Tweet.remove_punctuation(tokens)
        tokens = Tweet.remove_numbers(tokens)
        tokens = Tweet.remove_abbreviations(tokens)
        tokens = Tweet.remove_laugh(tokens)
        tokens = Tweet.remove_mentions(tokens)
        tokens = Tweet.remove_hashtags(tokens)
        return tokens

    def expandir_a_parecidos(self, model):
        tokens = self.tokenize_and_clean()
        tweet_expandido = set()

        for t in tokens:
            t = t.encode('utf8')
            tweet_expandido.add(t)
            if model.__contains__(t):
                indexes, metrics = model.cosine(t)
                parecidos_t = model.vocab[indexes][:2]
                tweet_expandido |= set(parecidos_t)

        return tweet_expandido
