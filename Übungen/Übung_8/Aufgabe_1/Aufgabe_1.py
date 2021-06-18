from gensim.test.utils import datapath
from gensim import utils
import matplotlib.pyplot as plt
import gensim
model=gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary = True) 
print(model.wv.most_similar(positive=['key'], topn=10))
print(model.wv.doesnt_match(['orange', 'car', 'apple', 'banana', 'tomato', 'car']))
