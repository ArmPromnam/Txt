import streamlit as st
import pandas as pd

st.title("website Devalope using Python")
st.header("website Devalope using Python")
st.subheader("ArmPromnam")
st.image("12.gif")

dt=pd.read_csv('./data/iris.csv')

st.subheader("ข้อมูลดอกไม้ Iris")
st.write(dt.head(10))

st.subheader("สถิติข้อฒุลดอกไม้ Iris")
st.write('ผลรวม')
cl1,cl2,cl3,cl4=st.colums(4)
cl1.wrte(dt['sepal.length'].sum()))
cl2.wrte(dt['sepal.width'].sum()))
cl3.wrte(dt['sepal.length'].sum()))
cl4.wrte(dt['sepal.width'].sum()))
st.write('ค่าเฉลี่ย')
st.write('ผลรวม')
st.write('ผลรวม')

