#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import glob
import os


All_Key_Words=[]
if(os.path.exists("MergedCompanies.csv")):
    data_frame = pd.read_csv("MergedCompanies.csv")
else:
    print("File not Found, please run MergeAllCSV.py first!")
    os._exit()

all_Descrption = data_frame["Purpose"].values

for items in all_Descrption:
    All_Key_Words = All_Key_Words + [x for x in items.split(" ") if x!=""]

Grouped_keys =dict()
for item in All_Key_Words:
    Grouped_keys[item] = Grouped_keys.setdefault(item, 0) + 1

Grouped_keys = sorted(Grouped_keys.items(),key=lambda x:x[1],reverse=True) 

print("The 10 most common key words are:")

Counter = 1
for k,v in Grouped_keys:
    if (Counter>10):
        break
    print(k," ",v,"times")
    Counter+=1

