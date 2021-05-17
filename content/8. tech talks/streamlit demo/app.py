#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 09:10:49 2021

@author: shoerasels
"""
from os import listdir
from os.path import isfile, join, isdir
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st

"""
First I will define some functions to work with.
"""

def load_data():
    path_origin = 'bbc/'
    
    categories = [f for f in listdir(path_origin) if isdir(join(path_origin, f))]
    
    X = []
    y = []
    for cat in categories:
        mypath = path_origin+cat+'/'
        files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        for file in files:
            with open(mypath+file, encoding="utf8", errors='ignore') as f:
                text = f.read()
                X+=[text]
                y+=[cat]

                
    
    y = pd.DataFrame(y)
    return X,y,categories

def tfidf_features(txt, flag):
    if flag == "train":
        x = tfidf.fit_transform(txt)
    else:
        x = tfidf.transform(txt)
    return x 

def matrix_to_pandas(X, tfidf):
    """
    Transform the sparse tfidf matrix in a pandas dataframe in order to see the column names above the features.
    At this stage you don't need to understand what is happening here. Is is only for visualisation purposes.
    """
    X = X.toarray()
    df = pd.DataFrame(X, columns = tfidf.get_feature_names())
    return df


############################### SCRIPT
""" From here on we will intereact with the streamlit app."""

X,y,categories = load_data()
num_features = 10000

#Define streamlit parameters
st.title("Extracting key-words by using tf-idf")
option2 = st.checkbox('remove stopwords')
option4 = st.selectbox('N-grams', (1, 2, 3, 4, 5))

#Initialize tfidf
if option2:
    tfidf = TfidfVectorizer(max_features= num_features, stop_words='english', ngram_range=(option4,option4))
else:
    tfidf = TfidfVectorizer(max_features= num_features, ngram_range=(option4,option4))


#transform your data
X_trans = tfidf_features(X, flag="train")
df = matrix_to_pandas(X_trans, tfidf)
df['y'] = y



option = st.selectbox('Domain', categories)
option3 = st.selectbox('Number of words to show', (5,10,15))

#extract only documents for the chosen category
df_small = df[df.y == option]
df_small.pop('y')
#compute most important words for a categroy
sol = df_small.sum(axis = 0, skipna = True).nlargest(option3)

st.write(sol)



