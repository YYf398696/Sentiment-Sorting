#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import glob
import os
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

if(os.path.exists("MergedCompanies.csv")):
    data_frame = pd.read_csv("MergedCompanies.csv")
else:
    print("File not Found, please run MergeAllCSV.py first!")
    os._exit()

all_Descrption = data_frame["Purpose"].values
grader = SentimentIntensityAnalyzer()
best_grade = float('-inf') 
best_idea = ""
worst_grade = float('-inf') 
worst_idea = ""
for items in all_Descrption:
    current_grade = grader.polarity_scores(items)["compound"]
    if worst_grade == float('-inf') :
        worst_grade = current_grade
        worst_idea = items
    if current_grade>best_grade :
        best_grade = current_grade
        best_idea = items
    elif current_grade< worst_grade:
        worst_grade = current_grade
        worst_idea = items
print ("Best idea: "+best_idea)
print ("Worst idea: "+worst_idea)
    
    

