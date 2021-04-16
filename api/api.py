# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 22:03:07 2021

@author: michele
"""

import requests

res=requests.get("https://s.fleet.ls.hereapi.com/1/tile.json?layer=LINK_ATTRIBUTE_FC3&level=11&tilex=1949&tiley=1491&apiKey=__M4jTOKfFKNfDLlFxF1ZtMv8YeR4XVTKx7RgQR0_oE")
json=res.json()


