import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.header("stock price prediction")

name = st.text_input("enter the symbol of company you want to predict on.")
start = st.date_input("start Date")
end = st.date_input("end Date")

# btn = st.button("search")


data = yf.download(name, start=start, end=end)
data = data.reset_index()
data = data.drop(['Date'], axis = 1)


sl = st.slider("weighted moving average gamma.", 1, 500, 100)

# ma100 = data.High.rolling(100).mean()
ma200c = data.Close.rolling(sl).mean()
ma200h = data.High.rolling(sl).mean()
ma200o = data.Open.rolling(sl).mean()
ma200l = data.Low.rolling(sl).mean()
plt.figure(figsize = (12,6))
plt.plot(data.High)
plt.plot(ma200c , 'r')
plt.plot(ma200h, 'g')
plt.plot(ma200o, 'b')
plt.plot(ma200l, 'black')
st.pyplot(plt)

import keras

from keras.models import load_model # type: ignore# model = load_model('stock_model.keras')
st.success("model loaded")
data_procesed_array = pd.DataFrame(data['Close'])

# # from sklearn.preprocessing  import MinMaxScaler
# # scaler = MinMaxScaler(feature_range=(0,1))

# # data_procesed_array = scaler.fit_transform(data_procesed)

# import numpy as np
# data_procesed_array = np.array(data_procesed_array)

# y_predicted = model.predict(data_procesed_array)

# # scale_factor = 1/0.00701864
# # y_predicted = scaler.inverse_transform(y_predicted)
# y_test = data_procesed_array

# plt.figure(figsize=(12,6))
# plt.plot(y_test, 'b' , label = 'original price')
# plt.plot(y_predicted, 'r' , label = 'predicted price')
# plt.xlabel('Time')
# plt.ylabel('price')
# plt.legend()
# plt.show()

# st.pyplot(plt)
