import os

class IterableCorpus(object):
    def __init__(self, path):
        self.path = path

    def sentences(self):
	if os.path.isfile(self.path):
	    return self.IterableSingleFileCorpus(self.path)
	else:
	    return self.IterableMultifileCorpus(self.path)

    class IterableMultifileCorpus(object):
	def __init__(self, dirname):
	    self.dirname = dirname

	def __iter__(self):
	    for fname in os.listdir(self.dirname):
		fname = os.path.join(self.dirname, fname)
		if not os.path.isfile(fname):
		    continue
		with open(fname) as FileObj:
		    for lines in FileObj:
			yield lines

    class IterableSingleFileCorpus(object):
	def __init__(self, fname):
	    self.fname = fname

	def __iter__(self):
	    with open(self.fname) as FileObj:
		for lines in FileObj:
		    yield lines

