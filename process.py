#from sklearn.decomposition import LatentDirichletAllocation, NMF
from sklearn.feature_extraction.text import TfidfVectorizer
from time import time
import numpy as np
'''
from collections import Counter
with open(artist) as songsFile:
    count = Counter(word for line in songsFile for word in line.split())
    print(count.most_common(10))
with open(artist) as songsFile:
    input_list = songsFile.read().split(' ')
    count = Counter(zip(input_list, input_list[1:]))
    print(count.most_common(10))
'''

#def display_topics(model, feature_names, no_top_words):
#    for topic in model.components_:
#        print(" ".join([feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]]))
#from sklearn.metrics.pairwise import linear_kernel
with open("preprocessed.txt") as songsFile:
    processed_docs = list(songsFile)
    '''    
    vectorizer = TfidfVectorizer()
    #vectorizer = CountVectorizer(max_df=0.9, min_df=25, token_pattern='\w+|\$[\d\.]+|\S+')
    tf = vectorizer.fit_transform(processed_docs)
    tf_feature_names = vectorizer.get_feature_names()
    #model = LatentDirichletAllocation(n_components=1, random_state=0)
    start = time()
    nmf = NMF(n_components=1).fit(tf)
    print(time()-start)
    start = time()
    lda = LatentDirichletAllocation(n_components=1).fit(tf)
    print(time()-start)
    no_top_words = 10
    display_topics(nmf, tf_feature_names, no_top_words)
    display_topics(lda, tf_feature_names, no_top_words)
    '''    
    tfidf = TfidfVectorizer().fit_transform(processed_docs)
    pairwiseSim = (tfidf * tfidf.T).A
    #pairwiseSim = linear_kernel(tfidf, tfidf)
    pairwiseSim[pairwiseSim>0.9] = 0
    print(np.unravel_index(
        np.argmax(np.triu(pairwiseSim, 1), axis=None),
        pairwiseSim.shape))
    mean = np.mean(tfidf, axis=0)
    howRepr = (mean * tfidf.T).A
    #howRepr = linear_kernel(mean, tfidf)
    print(np.argmax(howRepr))
