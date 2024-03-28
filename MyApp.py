import streamlit as st
import pandas as pd

st.title("website Devalope using Python")
st.header("website Devalope using Python")
st.subheader("ArmPromnam")
st.image("12.gif")

dt=pd.read_csv('./data/iris.csv')

st.subheader("ข้อมูลดอกไม้ Iris")
st.write(dt.head(10))


