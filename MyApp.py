import streamlit as st
import pandas as pd

st.title("เว็บไซต์พัฒนาด้วย Python")
st.header("เว็บไซต์พัฒนาด้วย Python")
st.subheader("ArmPromnam")
st.image("12.gif")

dt = pd.read_csv("./data/iris.csv")

st.subheader("ข้อมูลดอกไม้ Iris")
st.write(dt.head(10))

st.subheader("สถิติข้อมูลดอกไม้ Iris")

cl1, cl2, cl3, cl4 = st.columns(4)

cl1.write("ผลรวม")
cl2.write("ค่าเฉลี่ย")
cl3.write("ผลรวม")
cl4.write("ผลรวม")

st.write(dt.sum(axis=0))
st.write(dt.mean(axis=0))
st.write(dt.sum(axis=0))

