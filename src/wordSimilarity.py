#takes in a keyword and returns the most similar of 8 words
import logging
import os
import json
import re

from gensim import corpora, models, similarities
class wordSim:

    def get_sim_percent(self):
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        return



    def find_best_answer(texts, processed_question):
        dictionary = corpora.Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]
        tfidf = models.TfidfModel(corpus, normalize=True)

        corpus_tfidf = tfidf[corpus]
        lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=300)

        question_vector_bow = dictionary.doc2bow(processed_question)
        question_vector_lsi = lsi[question_vector_bow]

        index = similarities.MatrixSimilarity(lsi[corpus])

        simularity_scores = index[question_vector_lsi]
        simularity_scores = sorted(enumerate(simularity_scores), key=lambda item: -item[1])

        return simularity_scores