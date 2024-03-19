import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#st.image('')
st.header("สถิติการเกิดอุบัติเหตุในประเทศไทย")

col1,col2=st.columns(2)

with col1:
    st.subheader("จำนวนผู้เสียชีวิต")
    st.write("2,5600")
with col2:
    st.subheader("จำนวนผู้เสียชีวิต")
    st.write("2,5600")

dt=pd.read_excel('data/DATA.xlsx')

st.write(dt.head(10))

if(st.button("แสดงข้อมูลตัวอย่าง")):
    st.write(dt.head(100))
    st.button("ปิดข้อมูล")

else:
    st.button("ปิดข้อมูล")

# เพิ่มตัวเลือกสำหรับผู้ใช้ในการกรองข้อมูล
gender_option = st.sidebar.selectbox("เลือกเพศ", ["ชาย", "หญิง"])

filtered_df = dt[dt["Sex"] == gender_option]

# แสดงจำนวนผู้เสียชีวิตและบาดเจ็บแยกตามเพศ
col1, col2 = st.columns(2)

with col1:
    st.subheader("จำนวนผู้เสียชีวิต")
    st.write(filtered_df["เสียชีวิต"].sum())

with col2:
    st.subheader("จำนวนผู้บาดเจ็บ")
    st.write(filtered_df["บาดเจ็บ"].sum())


#st.write
NumM=dt[dt['Sex']=='ชาย'].count()
NumF=dt[dt['Sex']=='หญิง'].count()

st.subheader('ชาย')
st.subheader(NumM[1])
st.subheader('หญิง')
st.subheader(NumM[1])
dtSex=[NumM[1],NumF[1]]
dtSexb=pd.DataFrame(dtSex,index=["ชาย","หญิง"])
st.bar_chart(dtSexb)

import matplotlib.pyplot as plt #PIE
labels = 'Men', 'Wumen'
sizes = [NumM[1],NumF[1]]
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
st.pyplot(fig1)

