#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import nltk
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

Data = pd.read_csv('MergedCompanies.csv')
analyser = SentimentIntensityAnalyzer()
def sentiment_analysis(text):
    return analyser.polarity_scores(text)

for sen in Data:
    print(sen)
    ss = analyser.polarity_scores(sen)
    for k in ss:
        print('{0}:{1},'.format(k, ss[k]), end='')
    print()

