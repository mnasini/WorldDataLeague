from typing import List
import random
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import graphviz 
from IPython.display import Image, display
from graphviz import Source


def connect_routes(lab, lst): 
    links = list(lst.linkid) 
    if len(links) > 1: 
        for i in range(len(links)-1):
                if((G.edges.get((links[i],links[i+1],0)))!=dict({'label': lab.iloc[0]})):
    
                    G.add_edge(links[i], links[i+1], label=lab.iloc[0])

def rem(g: nx.Graph):
    nodes = list(g.nodes)
    for node in nodes:
        if g.degree(node)==2:
            neigh=list(g.neighbors(node))
            if len(neigh)==2:
                lab1 = g.get_edge_data(node, neigh[0])[0]["label"]
                lab2 = g.get_edge_data(node, neigh[1])[0]["label"]
                if lab1==lab2:
                    g.remove_node(node)
                    g.add_edge(neigh[0], neigh[1], label=lab1)
                 
             
G = nx.MultiGraph()
pos = nx.spring_layout(G)
df_routes = pd.read_csv('data/BusRoutes.txt', encoding= 'unicode_escape',sep="|")
df_routes=df_routes.set_index('IDRoute').loc[1:20].reset_index()

G.add_nodes_from(df_routes.linkid.unique())
df_routes.groupby('IDRoute').apply(lambda x: connect_routes(x.IDRoute, x))

rem(G)

#pos = nx.drawing.nx_pydot.graphviz_layout(G)
##nx.draw(G, pos, node_size=1, edge_color=list(labels.values()),connectionstyle="arc3,rad=3")
#graph_labels = nx.get_edge_attributes(G,'label')

#edges_label = nx.draw_networkx_edge_labels(G, pos, edge_labels = graph_labels)

def color_list():
    rand=[random.randint(0,16777215) for i in range(90)]
    hexrand=list(map(str,list(map(hex,rand))))
    hexrand=list(map(lambda x: '#'+ x[2:],hexrand))
    return hexrand 
    
    
    
p=nx.drawing.nx_pydot.to_pydot(G)


colors=color_list()
for i, edge in enumerate(p.get_edges()):
   edge.set_color(colors[int(edge.get("label"))])





p.write_png('multi.png')
Image(filename='multi.png')