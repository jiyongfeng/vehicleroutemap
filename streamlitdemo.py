#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
   * @Author: Ji Yongfeng
   * @Date: 2022-09-18 11:05:33
   * @LastEditTime: 2022-09-18 11:24:24
   * @LastEditor: Ji Yongfeng
   * @Description: streamlit demo 
 '''
import streamlit as st
import pandas as pd
import numpy as np
import os
import altair as alt

df = pd.DataFrame(np.random.randn(200, 3),columns=['a', 'b', 'c'])
c = alt.Chart(df).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
