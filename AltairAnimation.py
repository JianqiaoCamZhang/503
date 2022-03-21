#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 13:53:34 2022

@author: zhangjianqiao
"""

import pandas as pd
import altair as alt
import streamlit as st
import time
data_04 = pd.read_csv('/Users/zhangjianqiao/Documents/ANLY503/hw4/data_04_melt.csv')
data_05 = pd.read_csv('/Users/zhangjianqiao/Documents/ANLY503/hw4/data_05_melt.csv')
data_06 = pd.read_csv('/Users/zhangjianqiao/Documents/ANLY503/hw4/data_06_melt.csv')

data_04['date'] = pd.to_datetime(data_04['Date'])
data_05['date'] = pd.to_datetime(data_05['Date'])
data_06['date'] = pd.to_datetime(data_06['Date'])


lines = alt.Chart(data_04).mark_line().encode(
     x=alt.X('1:T',axis=alt.Axis(title='date')),
     y=alt.Y('0:Q',axis=alt.Axis(title='value'))
).properties(
    width=600,
    height=300
)
    
def plot_animation(df):
    lines = alt.Chart(df).mark_line().encode(
       x=alt.X('Date:T', axis=alt.Axis(title='date')),
       y=alt.Y('value:Q',axis=alt.Axis(title='work_hour_per_day')),
    color='variable',
    strokeDash='variable'
     ).properties(
       width=600,
       height=300
     ) 
    return lines
N = data_04.shape[0] # number of elements in the dataframe
burst = 8       # number of elements (months) to add to the plot
size = burst 
line_plot = st.altair_chart(lines)
start_btn = st.button('Start')
if start_btn:
   for i in range(1,N):
      step_df = data_04.iloc[0:size]
      lines = plot_animation(step_df)
      line_plot = line_plot.altair_chart(lines)
      size = i + burst
      if size >= N: 
         size = N - 1
      time.sleep(0.08)
      

      
 

    