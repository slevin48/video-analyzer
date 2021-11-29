import streamlit as st
import pyautogui

st.title("ImageGraber📷")

sz = pyautogui.size()
# st.write(sz)
x0 = st.slider("x0",max_value=sz.width)
y0 = st.slider("y0",max_value=sz.height)

x = st.slider("x",max_value=sz.width,value=sz.width)
y = st.slider("y",max_value=sz.height,value=sz.height)

img = pyautogui.screenshot(region=(x0,y0,x-x0,y-y0))
st.image(img)

st.write([x0,y0,x-x0,y-y0])