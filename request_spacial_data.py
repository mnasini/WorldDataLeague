# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 22:47:31 2021

@author: michele
"""
from typing import List
import random
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import graphviz
from IPython.display import Image, display
from graphviz import Source

df_senior = pd.read_csv('data/Senior_TIM_v1.txt', encoding= 'unicode_escape',sep="|")
df_senior=df_senior.groupby("linkid")

def pos(linkids):
   res=requests.get("https://s.fleet.ls.hereapi.com/1/index.json?layer=ROAD_GEOM_FCn&attributes=LINK_ID&values=&"+",".join(linkids)+apiKey=poqpzod8l70ttWkLZ1N9CJjbex7lpWc3G2JVTEClgjY")
   json=res.json()
   return [(json["Layers"][i]["tileXYs"][0], json["Layers"][i]["tileXYs"][1]) for i in range(len(linkids))]

unique_ids = df_senior.linkids.unique()

coords = []
for i in range(0, len(unique_ids), 10):
   try:
      ids = unique_ids[i:(i+10)]
   except:
      ids = unique_ids[i:]   
   coords += pos(ids)

x, y = *coords

new_df = pd.DataFrame({"linkid": unique_ids, "x": x, "y": y})
