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

dx=pd.DataFrame(
    {
        "col1":dt['sepat.length'].sum()
        "col1":dt['sepat.width'].sum()
    }
)
st.bar_chart(dx,x='col1',y='col2',color='col3')

st.write('ค่าเฉลี่ย')
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['sepal.length'].mean())
cl2.write(dt['sepal.width'].mean())
cl3.write(dt['sepal.length'].mean())
cl4.write(dt['sepal.width'].mean())

