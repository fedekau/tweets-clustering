import os

class IterableCorpus(object):
    def __init__(self, path, preprocessor=None):
        self.path = path
        self.preprocessor = preprocessor

    def sentences(self):
	if os.path.isfile(self.path):
	    return self.IterableSingleFileCorpus(self.path, self.preprocessor)
	else:
	    return self.IterableMultifileCorpus(self.path, self.preprocessor)

    class IterableMultifileCorpus(object):
	def __init__(self, dirname, preprocessor=None):
	    self.dirname = dirname
            self.preprocessor = preprocessor

	def __iter__(self):
	    for fname in os.listdir(self.dirname):
		fname = os.path.join(self.dirname, fname)
		if not os.path.isfile(fname):
		    continue
		for line in open(fname):
		    if self.preprocessor:
			line = self.preprocessor.process(line)
		    yield line.split()

    class IterableSingleFileCorpus(object):
	def __init__(self, fname, preprocessor=None):
	    self.fname = fname
            self.preprocessor = preprocessor

	def __iter__(self):
	    for line in open(self.fname):
		if self.preprocessor:
		   line = self.preprocessor.process(line)
	        yield line.split()

