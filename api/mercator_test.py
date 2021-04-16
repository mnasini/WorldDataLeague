# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 17:48:59 2021

@author: michele
"""

from pyproj import Proj, transform

inProj = Proj(init='epsg:3857')
outProj = Proj(init='epsg:4326')
x1,y1 = 194900,149200
x2,y2 = transform(inProj,outProj,x1,y1)
print (x2,y2)