import getopt
import sys
import os

from gensim.models import Word2Vec
from iterable_corpus import IterableCorpus
from preprocessors import LowercasePreprocessor

def main(argv):
    corpus_path = ''
    model_file = ''
    size = 100
    try:
	opts, args = getopt.getopt(argv,"hi:o:s",["ifile=","ofile=","size="])
    except getopt.GetoptError:
	print 'python train_word2vec.py -i <inputfile> -o <outputfile>'
	sys.exit(2)
    for opt, arg in opts:
	if opt == '-h':
	    print 'python train_word2vec.py -i <inputfile> -o <outputfile>'
	    sys.exit()
	elif opt in ("-i", "--ifile"):
	    corpus_path = arg
	elif opt in ("-o", "--ofile"):
	    model_file = arg
	elif opt in ("-s", "--size"):
	    size = int(arg)

    sentences = IterableCorpus(corpus_path, preprocessor=LowercasePreprocessor()).sentences()

    model = Word2Vec(sentences, size=size, window=5, min_count=5, workers=4)

    model.save(model_file)

if __name__ == "__main__":
   main(sys.argv[1:])


