#!/usr/bin/python
import types

import numpy
import scipy
import gensim

class Distance():

    def __init__(self, model, lemmatizer=None, normalizeVector=False):
        self.model = model
        self.normalizeVector = normalizeVector
        self.lemmatizer = lemmatizer
        self.t1 = None
        self.t2 = None
        self.t1_changed = False

    def simple(self, t1, t2):
        t1_expandido = t1.expandir_a_parecidos(self.model)
        t2_expandido = t2.expandir_a_parecidos(self.model)

        palabras_interseccion = t1_expandido.intersection(t2_expandido)
        return len(palabras_interseccion)

    def jaccard(self, t1, t2):
        t1_expandido = t1.expandir_a_parecidos(self.model)
        t2_expandido = t2.expandir_a_parecidos(self.model)

        distance = 1.0 - ((1.0 * len(t1_expandido.intersection(t2_expandido))) / len(t1_expandido.union(t2_expandido)))

        return distance

    def vector(self, t1, t2):
        self.t1_changed = False
        self.t2_changed = False

        if self.t1 != t1:
            self.t1 = t1
            self.t1_changed = True

        if self.t2 != t2:
            self.t2 = t2
            self.t2_changed = True

        if self.t1_changed:
            t1_tokens = self.tokens(self.t1)
            self.t1_vector = [0] * self.model.vector_size
            for t in t1_tokens:
                if self.model.__contains__(t):
                    self.t1_vector = numpy.sum([self.t1_vector, self.model[t]], axis=0)

        if self.t2_changed:
            t2_tokens = self.tokens(self.t2)
            self.t2_vector = [0] * self.model.vector_size
            for t in t2_tokens:
                if self.model.__contains__(t):
                    self.t2_vector = numpy.sum([self.t2_vector, self.model[t]], axis=0)
        try:
            return scipy.spatial.distance.euclidean(self.t1_vector, self.t2_vector)
        except Exception:
            return 1000

    def cosine(self, t1, t2):
        self.t1_changed = False
        self.t2_changed = False

        self.customize_n_similarity()

        if self.t1 != t1:
            self.t1 = t1
            self.t1_changed = True

        if self.t2 != t2:
            self.t2 = t2
            self.t2_changed = True

        if self.t1_changed:
            t1_tokens = self.tokens(self.t1)
            self.t1_tokens = []
            for t in t1_tokens:
                if self.model.__contains__(t):
                    self.t1_tokens.append(t)

        if self.t2_changed:
            t2_tokens = self.tokens(self.t2)
            self.t2_tokens = []
            for t in t2_tokens:
                if self.model.__contains__(t):
                    self.t2_tokens.append(t)

        try:
            return 1 - self.model.n_similarity(self.t1_tokens, self.t2_tokens)
        except Exception:
            return 1000

    def tokens(self, tweet):
        tokens = tweet.tokenize_and_clean()

        if self.lemmatizer != None:
            tokens = self.lemmatizer.lemmatize(tokens)

        return tokens

    # def process_vector(self, vector):
    #     print(vector[0])
    #     if (self.normalizeVector):
    #         vector = normalize(vector)
    #         print(vector[0])
    #     return vector

    def customize_n_similarity(self):
        def n_similarity(self, ws1, ws2):
            def normalize(vec):
                norm = numpy.linalg.norm(vec)
                if norm != 0:
                    return vec / norm
                else:
                    return vec

            if not(len(ws1) and len(ws2)):
                raise ZeroDivisionError('Atleast one of the passed list is empty.')
            v1 = [normalize(self[word]) for word in ws1]
            v2 = [normalize(self[word]) for word in ws2]
            return numpy.dot(gensim.matutils.unitvec(numpy.array(v1).mean(axis=0)),
                   gensim.matutils.unitvec(numpy.array(v2).mean(axis=0)))

        self.model.n_similarity = types.MethodType(n_similarity, self.model)

