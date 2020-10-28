#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
import glob
import os


all_files = glob.glob(os.path.join("*.csv"))    
all_data_frame = []
if(os.path.exists("MergedCompanies.csv")):
    os.remove("MergedCompanies.csv")
row_count = 0
for file in all_files:
    data_frame = pd.read_csv(file)
    if(data_frame.columns[0]=="Unnamed: 0"):
        data_frame=data_frame.drop(["Unnamed: 0"],axis=1)
    data_frame.columns = ['Company','Purpose']
    all_data_frame.append(data_frame)
data_frame_concat = pd.concat(all_data_frame, axis=0, ignore_index=True, sort=True)
data_frame_concat = data_frame_concat.drop_duplicates()
data_frame_concat.to_csv("MergedCompanies.csv", index=False, encoding="utf-8")     