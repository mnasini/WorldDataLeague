# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 22:03:07 2021

@author: michele
"""

import requests

res=requests.get("https://s.fleet.ls.hereapi.com/1/index.json?layer=ROAD_GEOM_FCn&attributes=LINK_ID&values=537277300&apiKey=poqpzod8l70ttWkLZ1N9CJjbex7lpWc3G2JVTEClgjY")
json=res.json()

res1=requests.get("https://s.fleet.ls.hereapi.com/1/tile.json?apiKey=poqpzod8l70ttWkLZ1N9CJjbex7lpWc3G2JVTEClgjY&layer=LINK_ATTRIBUTE_FC1&level=9&tilex=537&tiley=399")
json=res.json()