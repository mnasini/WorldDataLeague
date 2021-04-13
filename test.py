import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import graphviz as vz
from IPython.display import Image, display
def fun(lab,lst): 
         links = list(lst.linkid) 
         if len(links) > 1: 
             for i in range(len(links)-1): 
                 
                 G.add_edge(links[i], links[i+1],label=lab.iloc[0])
def rem(g):
    for i in list(g.nodes):
        if g.degree(i)==2:
            neigh=list(g.neighbors(i))
            g.remove_node(i)
            g.add_edge(neigh[0],neigh[1])
    pass
                 
             
G = nx.Graph()
df_routes = pd.read_csv('BusRoutes.txt', encoding= 'unicode_escape',sep="|")
G.add_nodes_from(df_routes.iloc[:500].linkid.unique())
df_routes.iloc[:500].groupby('IDRoute').apply(lambda x: fun(x.IDRoute, x))

pos = nx.spring_layout(G, scale=2,seed=266)
rem(G)
nx.draw(G,pos)
graph_labels = nx.get_edge_attributes(G,'label')

edges_label = nx.draw_networkx_edge_labels(G, pos, edge_labels = graph_labels)


#plt.show(block=False)
plt.savefig("Graph.svg", format="SVG")
deg=G.degree
print(deg)
sorted(G.degree, key=lambda x: x[1], reverse=True)
def view_pydot(pdot):
    plt = Image(pdot.create_png())
    display(plt)
    
to_pdot = nx.drawing.nx_pydot.to_pydot
pdot = to_pdot(G)
view_pydot(pdot)


