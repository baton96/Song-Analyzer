from collections import Counter
from time import time
import re
from nltk.util import ngrams


with open(artist) as songsFile:
    count = Counter(word for line in songsFile for word in line.split())
    print(count.most_common(10))
with open(artist) as songsFile:
    input_list = songsFile.read().split(' ')
    count = Counter(zip(input_list, input_list[1:]))
    print(count.most_common(10))

import gensim
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from time import time
import nltk

stemmer = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()
artist = 'billie_eilish.txt'
en_stop = set(nltk.corpus.stopwords.words('english'))
from sklearn.decomposition import LatentDirichletAllocation, NMF
def preprocess(text):           
    return ' '.join([stemmer.stem(lemmatizer.lemmatize(token, pos='v')) for token in gensim.utils.simple_preprocess(text) if token not in gensim.parsing.preprocessing.STOPWORDS])
with open(artist) as songsFile:
    processed_docs = [preprocess(line[:-1]) for line in songsFile if len(line)>150]
    with open("preprocessed.txt", "w") as preprocessedFile:
        for line in processed_docs:
            preprocessedFile.write(line+'\n')
