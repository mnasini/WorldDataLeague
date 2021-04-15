# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 22:47:31 2021

@author: michele
"""
from typing import List
import random
import requests
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import graphviz
from IPython.display import Image, display
from graphviz import Source

df_senior = pd.read_csv('data/Senior_TIM_v1.txt', encoding= 'unicode_escape',sep="|")


def pos(linkid):
  # print(",".join(linkids.astype(str)))
   res=requests.get("https://s.fleet.ls.hereapi.com/1/index.json?layer=ROAD_GEOM_FCn&attributes=LINK_ID&values="+str(linkid)+"&apiKey=__M4jTOKfFKNfDLlFxF1ZtMv8YeR4XVTKx7RgQR0_oE")
  
   json=res.json()
  
   return (json["Layers"][0]["tileXYs"][0]["x"], json["Layers"][0]["tileXYs"][0]["y"])

unique_ids = df_senior.linkid.unique()

coords = []
for i in range(len(unique_ids)):
    try:
        ids = unique_ids[i]   
        coords.append(pos(ids)) 
    except:
        coords.append(None)

x, y = zip(*coords)

new_df = pd.DataFrame({"linkid": unique_ids, "x": x, "y": y})
new_df.to_csv("geospatial_data.csv")
