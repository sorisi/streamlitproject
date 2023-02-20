import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import time
from PIL import Image
import numpy as np



#st.header("Savings or Investment ")

plt.style.use("ggplot")


data = {
  "num":[x for x in range(1, 11)],
  "square":[x**2 for x in range(1, 11)],
  "twice":[x*2 for x in range(1, 11)],
  "thrice":[x*3 for x in range(1, 11)],
}

rad = st.sidebar.radio("Navigation",["Home", "About", "Investment", "Register"])

if rad == "Home":

  
  df = pd.DataFrame(data = data)

  col = st.sidebar.multiselect("Select a column ", df.columns)

  st.set_option('deprecation.showPyplotGlobalUse', False)

  plt.plot(df['num'], df [col])

  st.pyplot()


if rad == "About":

    st.title('Savings or Investment')
    map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
    st.map(map_data)

    st.markdown(
    """
    We have invested money in stocks to generate more return then bank savings.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [Savings Or Investment](http://savingsorinvestment.com/)
    - Jump into our [Financial News](https://finance.yahoo.com/)
    - Ask a question in our [Register](http://savingsorinvestment.com/log.html)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
 
if rad == "Investment":

  col1, col2, col3 = st.columns(3)

  with col1:
   st.header("Finance")
   st.image("https://www.investopedia.com/thmb/TH8-Yt7GdB9TnJgo0RfsynjxbOQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/personalfinance_definition_final_0915-Final-977bed881e134785b4e75338d86dd463.jpg")

  with col2:
   st.header("Crypto")
   st.image("https://image.cnbcfm.com/api/v1/image/107164807-1670871271402-gettyimages-1303634450-bitcoin_05.jpeg?v=1673513871")

  with col3:
   st.header("News")
   st.image("https://cdn.corporatefinanceinstitute.com/assets/finance-definition.jpg")

  df = pd.DataFrame(
   np.random.randn(30, 20),
   columns=('col %d' % i for i in range(20)))

  st.dataframe(df)

  col1, col2 = st.columns([3, 1])
  data = np.random.randn(10, 1)

  col1.subheader("Main chart")
  col1.line_chart(data)

  col2.subheader("Data")
  col2.write(data)
 # Same as st.write(df)



   #progress = st.progress(0)
   #for i in range(100):
   #time.sleep(0.1)
   # progress.progress(i+1)

   #st.balloons()

if rad == "Register":

  st.header("Please Register ")
  first,last = st.columns(2)

  first.text_input("First Name")
  last.text_input("Last Name")


  email, mob = st.columns([3,1])
  email.text_input("Email ID")
  mob.text_input("Phone Number")

  user,pw,pw2 = st.columns(3)
  user.text_input("Username")
  pw.text_input("Password", type = "password")
  pw2.text_input("Retype your password", type = "password")


  ch,bl,sub = st.columns(3)
  ch.checkbox("I Agree")
  sub.button("Submit")
  



  st.balloons()




