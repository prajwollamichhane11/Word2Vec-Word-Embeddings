#!/usr/bin/env python
# coding: utf-8

# In[95]:


import numpy as np
import pandas as pd


df = pd.read_csv("SATAN.csv")


df["News Article"].replace(r"७ चैत,","",regex=True,inplace=True)
df["News Article"].replace(r"६ चैत,","",regex=True,inplace=True)
df["News Article"].replace(r"५ चैत,","",regex=True,inplace=True)
df["News Article"].replace(r"४ चैत,","",regex=True,inplace=True)
df["News Article"].replace(r"३ चैत,","",regex=True,inplace=True)


df["News Article"].replace(["।",'"',",","'","‘","’","\n","\xa0"],"",regex=True,inplace=True)


news = []
for i in range(len(df)):
    currentNews = df["News Article"].iloc[i]
    news.append(currentNews)

news = list(map(str, news))


news = ''.join(news)


news = news.replace('\u200d'," ")
news = news.replace('\u202f'," ")


f = open("corpus.txt", "a")
f.write(news)
f.close()