import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
from matplotlib import cm


df = pd.read_csv("coords_senior_data.csv", sep="|")
df["avg_senior"]
max_x = max(df.x)+1
max_y = max(df.y)+1

heatmap_buses = np.zeros((max_x, max_y))
heatmap_seniors = np.zeros((max_x, max_y))

for t in df.itertuples():
    heatmap_buses[t.x, t.y] = len(eval(t.bus_routes))
    heatmap_seniors[t.x, t.y] = t.avg_senior
heatmap_seniors_subset=heatmap_seniors[-30:,-30:]
heatmap_buses_subset=heatmap_buses[-30:,-30:]
heatmap_seniors_subset /= heatmap_seniors_subset.max()/255.0
heatmap_buses_subset /= heatmap_buses_subset.max()/255.0

im_senior = Image.fromarray(np.uint8(cm.gist_earth(heatmap_seniors_subset)*255))
plt.imshow(im_senior, cmap='hot', interpolation='nearest')
plt.show()
im_buses = Image.fromarray(np.uint8(cm.gist_earth(heatmap_buses_subset)*255))

