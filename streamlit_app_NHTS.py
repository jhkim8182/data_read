# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:58:14 2024

@author: jhkim
"""

import streamlit as st
import pandas as pd
import numpy as np
from zipfile import ZipFile
from io import BytesIO
from urllib.request import urlopen

st.title('NHTS 2022 statistics by stratum')

#DATE_COLUMN = 'date/time'
#DATA_URL = ('https://nhts.ornl.gov/'
#            'assets/2022/download/csv.zip')

DATA_URL = urlopen('https://nhts.ornl.gov/assets/2022/download/csv.zip')

with ZipFile(BytesIO(DATA_URL.read())) as myzip:
    myzip.printdir()
    
    print('Extracting all the files now...')
    myzip.extractall()
    print('Done')
    
    hhpub = pd.read_csv(myzip.open('hhpub.csv'))
    
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(hhpub)
    
st.subheader('Number of pickups by hour')
hist_values = np.histogram(hhpub['HHFAMINC'])[0]
st.bar_chart(hist_values)
    
    
    