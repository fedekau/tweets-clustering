#!/usr/bin/python

class Distance():

    def __init__(self, model):
	self.model = model

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

