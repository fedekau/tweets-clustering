import re

class Lemmatizer(object):

    def __init__(self, lemma_file):
        with open(lemma_file) as f:
            lines = f.readlines()

        self.lemmas = {}

        for l in lines:
           mapping = l.strip('\n').split('\t');
           self.lemmas[mapping[1]] = mapping[0]

    def find_lemma(self, word):
        return self.lemmas.get(word, word)

    def lemmatize(self, words):
        lemmas = []

        for w in words:
            lemmas.append(self.find_lemma(w))

        return lemmas
