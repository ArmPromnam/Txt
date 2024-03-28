import streamlit as st
import pandas as pd
import random

st.title("Website Devalope using Python")
st.header("Website Devalope using Python")
st.subheader("ArmPromnam")
st.image("12.gif")

dt=pd.read_csv('iris.csv')

st.subheader("ข้อมูลดอกไม้ Iris")
st.write(dt.head(10))

st.subheader("สถิติข้อมูลดอกไม้ Iris")
st.write('ผลรวม')
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['sepal.length'].sum())
cl2.write(dt['sepal.width'].sum())
cl3.write(dt['petal.length'].sum())
cl4.write(dt['petal.width'].sum())

st.write("กราฟแท่ง")
a=dt['sepal.length'].sum()
b=dt['sepal.width'].sum()
c=dt['petal.length'].sum()
d=dt['petal.width'].sum()
dx=[a,b,c,d]
cx=pd.DataFrame(dx,index=["sepal.length", "sepal.width", "petal.length","petal.width"])
st.bar_chart(cx)

st.write('ค่าเฉลี่ย')
cl11,cl12,cl13,cl14=st.columns(4)
cl11.write(dt['sepal.length'].mean())
cl12.write(dt['sepal.width'].mean())
cl13.write(dt['petal.length'].mean())
cl14.write(dt['petal.width'].mean())

st.write("Area_Chart")
a=dt['sepal.length'].mean()
b=dt['sepal.width'].mean()
c=dt['petal.length'].mean()
d=dt['petal.width'].mean()
dxt=[a,b,c,d]
cxx=pd.DataFrame(dxt,index=["sepal.length", "sepal.width", "petal.length","petal.width"])
st.area_chart(cxx)


st.write('ค่ามากที่สุด')
cl21,cl22,cl23,cl24=st.columns(4)
cl21.write(dt['sepal.length'].max())
cl22.write(dt['sepal.width'].max())
cl23.write(dt['petal.length'].max())
cl24.write(dt['petal.width'].max())

import numpy as np
import matplotlib.pyplot as plt
labels = ['Men', 'Women','','']
sizes = [35,25,15,25]
explode = (0, 0.1,0,0) 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
st.pyplot(fig1)


st.write('ค่าน้อยที่สุด')
cl31,cl32,cl33,cl34=st.columns(4)
cl31.write(dt['sepal.length'].min())
cl32.write(dt['sepal.width'].min())
cl33.write(dt['petal.length'].min())
cl34.write(dt['petal.width'].min())

st.write("Line_Chart")
cc=[3,8,1,10]
st.line_chart(cc)

# ตั้งค่าเริ่มต้น
WIDTH = 400  # ความกว้างของหน้าจอ
HEIGHT = 300  # ความสูงของหน้าจอ
DELAY = 100  # ความเร็วของเกม (หน่วยมิลลิวินาที)

# ตัวแปรสำหรับเกม
head_x = 100  # ตำแหน่งเริ่มต้น X ของหัวงู
head_y = 100  # ตำแหน่งเริ่มต้น Y ของหัวงู
body = [(head_x - 10, head_y), (head_x - 20, head_y)]  # ลำตัวของงู
direction = 0  # ทิศทางของงู (0: ขวา, 1: ลง, 2: ซ้าย, 3: ขึ้น)
food_x = random.randint(0, WIDTH - 10)  # ตำแหน่ง X ของอาหาร
food_y = random.randint(0, HEIGHT - 10)  # ตำแหน่ง Y ของอาหาร

# ฟังก์ชั่นสำหรับวาดหน้าจอ
def draw():
  global head_x, head_y, body, direction, food_x, food_y

  # ล้างหน้าจอ
  fill(0, 0, 0)

  # วาดตัวงู
  for segment in body:
    rect(segment[0], segment[1], 10, 10)

  # วาดหัวงู
  rect(head_x, head_y, 10, 10, fill=(255, 0, 0))

  # วาดอาหาร
  rect(food_x, food_y, 10, 10, fill=(0, 255, 0))

# ฟังก์ชั่นสำหรับอัปเดตเกม
def update():
  global head_x, head_y, body, direction, food_x, food_y

  # อัปเดตตำแหน่งหัวงู
  if direction == 0:
    head_x += 10
  elif direction == 1:
    head_y += 10
  elif direction == 2:
    head_x -= 10
  elif direction == 3:
    head_y -= 10

  # ตรวจสอบว่าหัวงูชนกับอาหาร
  if head_x == food_x and head_y == food_y:
    # กินอาหาร
    body.append((head_x, head_y))
    food_x = random.randint(0, WIDTH - 10)
    food_y = random.randint(0, HEIGHT - 10)
  else:
    # ลบส่วนหางของงู
    body.pop(0)

  # ตรวจสอบว่าหัวงูชนกับตัวเองหรือขอบหน้าจอ
  if head_x < 0 or head_x > WIDTH - 10 or head_y < 0 or head_y > HEIGHT - 10 or (head_x, head_y) in body:
    # เกมโอเวอร์
    print("Game Over!")
    exit()

# ฟังก์ชั่นสำหรับรับ input จากผู้ใช้
def on_key_press(key):
  global direction

  if key == "right":
    direction = 0
  elif key == "down":
    direction = 1
  elif key == "left":
    direction = 2
  elif key == "up":
    direction = 3

# เริ่มเกม
setup(WIDTH, HEIGHT, DELAY)
draw()

# ลูปหลักของเกม
while True:
  update()
  draw()
  on_key_press(get_key_press())