import getopt
import sys
import os

from gensim.models import Word2Vec
from iterable_corpus import IterableCorpus

def main(argv):
    corpus_path = ''
    model_file = ''
    try:
	opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
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

    sentences = IterableCorpus(corpus_path).sentences()

    model = Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)

    model.save(model_file)

if __name__ == "__main__":
   main(sys.argv[1:])


