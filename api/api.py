# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 22:03:07 2021

@author: michele
"""

import requests

res=requests.get("https://s.fleet.ls.hereapi.com/1/index.json?layer=ROAD_GEOM_FCn&attributes=LINK_ID&values=537277300&apiKey=__M4jTOKfFKNfDLlFxF1ZtMv8YeR4XVTKx7RgQR0_oE")
json=res.json()

