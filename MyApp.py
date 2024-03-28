import streamlit as st
import pandast as pd

st.title("website Devalope using Python")
st.header("website Devalope using Python")
st.subheader("ArmPromnam")
st.image("12.jpg")

dt=pd.read_csv('./data/iris.csv')
dt.head(10)