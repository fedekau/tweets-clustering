class Preprocessor(object):
    def process(self, sentence):
	    raise NotImplementedError("Method not implemented")

class LowercasePreprocessor(Preprocessor):
    def process(self, sentence):
	    return sentence.lower()


