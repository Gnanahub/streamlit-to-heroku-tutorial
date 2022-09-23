import streamlit as st
import pickle
import sklearn
import pandas as pd 
import numpy as np
from PIL import Image

model = pickle.load(open('diamondpredict.sav', 'rb'))

st.title('Diamond Price Prediction')
st.sidebar.header('Diamond Data')
image = Image.open('Diamonds-org-siz-6000x4000-shutterstock_325627796.jpg')
st.image(image,'')

#function 
def prediction(carat,cut,color,clarity,x,y,z,depth,table):
    prediction = model.predict(
        [[carat,cut,color,clarity,x,y,z,depth,table]])
    print(prediction)
    return prediction

#main function
def main():
#title
   #st.title("Predict the diamond price")

#bg color
    html_temp = """
    <div style ="background-color:steelblue;padding:8px">
    <h1 style ="color:blue morning glory;text-align:center;"> Predicting the Diamond price </h1>
    </div>
    <h2> Enter the details of your Diamond to know the Price </h2>
    
    """

    st.markdown(html_temp, unsafe_allow_html=True)

#def user_report():

carat = st.text_input("Weight of the diamond")
cut = st.text_input("Quality of the cut on  diamond")
color = st.text_input("Color of the diamond")
clarity = st.text_input("Clarity of the diamond")
length = st.text_input("Length of diamond in mm")
width = st.text_input("Width of diamond in mm")
depth = st.text_input("Depth of diamond in mm")
depth_1 = st.text_input("Total depth percentage")
table = st.text_input("width of top of diamond relative to widest point")
result = ""


btn_click = st.button("Predict Price")

if btn_click == True:
    if carat and cut and color and clarity and length and width and depth and depth_1 :
        label_cut = {'Ideal':2, 'Premium':3, 'Very Good':4, 'Good':1, 'Fair':0}
        label_color = {'G':3, 'E':1, 'F':2, 'H':4, 'D':0, 'I':5, 'J':6}
        label_clarity = {'SI1':2, 'VS2':5, 'SI2':3, 'VS1': 4, 'VVS2':7, 'VVS1':6, 'IF':1, 'I1':0}

    
    if st.button("Predict"):
        result = prediction(carat,cut,color,clarity,length, width, depth,depth_1,table)
    st.success('The price of your diamond is  {}'.format(result))
    st.balloons()
else:
    st.error("Enter the values properly!")
    st.snow()


if __name__ == '__main__':
    main()
    