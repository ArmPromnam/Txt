import streamlit as st
import pandas as pd

st.title("Website Devalope using Python")
st.header("Website Devalope using Python")
st.subheader("ArmPromnam")
st.image("12.gif")

dt=pd.read_csv('iris.csv')

st.subheader("ข้อมูลดอกไม้ Iris")
st.write(dt.head(10))

st.subheader("สถิติข้อฒุลดอกไม้ Iris")
st.write('ผลรวม')
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['sepal.length'].sum())
cl2.write(dt['sepal.width'].sum())
cl3.write(dt['sepal.length'].sum())
cl4.write(dt['sepal.width'].sum())
cols=['sepat.length','sepal.width','sepat.length']
dx=dt[cols]
st.bar_chart(dx,x='sepat.length',y='sepal.width',color='sepat.length')

st.write('ค่าเฉลี่ย')
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['sepal.length'].mean())
cl2.write(dt['sepal.width'].mean())
cl3.write(dt['sepal.length'].mean())
cl4.write(dt['sepal.width'].mean())

