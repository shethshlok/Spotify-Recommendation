# -*- coding: utf-8 -*-
"""Project#14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gwt7XREDFNTszDi4kcetJSrkFH8tR8ZX

Project #14
BAN 501
Created By: Shlok Sheth
Project Description: Recomendation Systems
"""

import pandas as pd

data = pd.read_csv('/content/show_rec_data.csv')

data.describe()

# given code
import numpy as np

def dot_product(vector1,vector2):
  thedotproduct=np.sum([vector1[k]*vector2[k] for k in range(0,len(vector1))])
  return thedotproduct

def vector_norm(vector):
  thenorm=np.sqrt(dot_product(vector,vector))
  return thenorm

def cosine_similarity(vector1,vector2):
  thedotproduct=dot_product(vector1,vector2)
  thecosine=thedotproduct/(vector_norm(vector1)*vector_norm(vector2))
  thecosine=np.round(thecosine,4)
  return thecosine

def get_show_recommendations(interaction, artist_name):
  otherrows=[rowname for rowname in interaction.index if rowname!=artist_name]
  otherartists=interaction.loc[otherrows,:]
  theartist=list(interaction.loc[artist_name,:])
  similarities=[]
  for artists in otherartists.index:
    similarities.append(cosine_similarity(theartist,list(otherartists.loc[artists,:])))
  otherartists['similarities']=similarities
  return list(otherartists.sort_values(by='similarities',ascending=False).index)

def get_similar_artists(interaction, user):
  othercolumns=[columnname for columnname in interaction.columns if columnname!=user]
  otherusers=interaction[othercolumns]
  theuser=list(interaction[user])
  similarities=[]
  for users in otherusers.columns:
    similarities.append(cosine_similarity(theuser,list(otherusers.loc[:,users])))
  otherusers.loc['similarities',:]=similarities
  return list(otherusers.sort_values(by='similarities',axis=1,ascending=False).columns)

def get_user_recommendations(interaction,user):
  similar_users=get_similar_artists(interaction,user)
  listening_history=interaction[similar_users[0]]
  listened=list(listening_history.loc[listening_history==1].index)
  listened2=list(interaction.loc[interaction[user]==1,:].index)
  recs=sorted(list(set(listened) - set(listened2)))
  return recs

# transpose the data
data_t = data.T

# Get Similar Show Recommendations

# Show Recomendations based on the users who watch show_1
print(f"Show recommendation based on users who watch show_1 {get_show_recommendations(data_t,'show_1')[0:4]}.")
print()
# This is the result it gave: ['show_4', 'show_5', 'show_3', 'show_2']
# Here we can see that most recommended show would be show_4 and least being show_2
# Streaming Businesses can use this to recommend show_4 to the user who
# watch show_1 and should not recommend any content from show_2

# Show recommendations based on the user who watch show_5
print(f"Show recommendation based on users who watch show_1 {get_show_recommendations(data_t,'show_5')[0:4]}.")
print()
# This is the result it gave me: ['show_2', 'show_4', 'show_1', 'show_3']
# This means that streaming businesses should recommend show_2 the most
# We can also conclude that show_5 and show_1 have complete different genres
# In a way, show_5 is more different than show_1 than show_1 from show_5
# because, show_5 is show_1's users 2nd recommendation but show_1 is show_5's user 4th recommendation

# Get New Show Recommendation

print(f"New show recommendation for user 2 {get_user_recommendations(data_t,2)[0:4]}.")
print()
# This is what it gave me: ['show_2', 'show_4']
# This means that user 2 can see these shows which it has not seen
# Given that show_2 is the first choice

print(f"New show recommendation for user 100 {get_user_recommendations(data_t,100)[0:4]}.")
print()
# This gave me: []
# That means that user 100 has seen all the shows that it should be recomended,
# Here the streaming business should recommend other shows that are form another genre