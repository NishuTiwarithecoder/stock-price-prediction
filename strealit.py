import numpy as np
import pandas as pd
import matplotlib.pyplot as  plt

import yfinance as yf
from datetime import datetime
from keras.models import load_
import streamlit as st

# Set the date range
start = '2012-01-01'
end = '2024-01-01'

st.tital("stoke treand prediction")
user_input = st.text_input('enter stock ticker', 'AAPL')

df = yf.download('AAPL',  start=start, end=end )

st.subheader('Data from 2012 - 2019')
st.write(df.describ())