# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 19:11:25 2021

@author: michele
"""

df_routes = pd.read_csv('data/BusRoutes.txt', encoding= 'unicode_escape',sep="|")
df_senior = pd.read_csv('data/Senior_TIM_v1.txt', encoding= 'unicode_escape',sep="|")
df_loc = pd.read_csv("geospatial_data_bus.csv")
df_loc_anz=pd.read_csv("geospatial_data.csv")

df_aggreg=df_senior.groupby('linkid').apply(sum).drop(columns=['Region_of_Origin', 'District_of_Origin','County_of_Origin'])
df_aggreg=df_aggreg.rename_axis(None)
df_routes=df_routes.merge(df_aggreg,how='left',left_on='linkid',right_on='linkid')
df_routes=df_routes.merge(df_loc,how='left',left_on='linkid',right_on='linkid')
df_aggreg_nobus=df_aggreg[df_aggreg.Average_Daily_SeniorPopulation_Travelling>1000]
df_aggreg_nobus=df_aggreg_nobus[~df_aggreg_nobus.linkid.isin(df_routes.linkid)]
df_aggreg_nobus=df_aggreg_nobus.merge(df_loc_anz,how='inner',left_on='linkid',right_on='linkid')