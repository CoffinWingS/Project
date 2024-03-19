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
    st.button("ไม่แสดงข้อมูลตัวอย่าง")

else:
    st.button("ไม่แสดงข้อมูลตัวอย่าง")


# เพิ่มตัวเลือกสำหรับผู้ใช้ในการเลือกปี
dt = st.sidebar.selectbox("เลือกปี", data["ปี"].unique())

# กรองข้อมูลตามปี
filtered_df = data[data["ปี"] == year_option]

# แสดงกราฟแท่ง
fig1, ax1 = plt.subplots()
ax1.bar(filtered_df.groupby("Sex").size().index, filtered_df.groupby("Sex").size())
ax1.set_xlabel("เพศ")
ax1.set_ylabel("จำนวนผู้เสียชีวิต")
st.pyplot(fig1)

# แสดงข้อมูลตาราง
st.dataframe(filtered_df.groupby("Sex").size().to_frame())

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

import matplotlib.pyplot as plt
labels = 'Men', 'Wumen'
sizes = [NumM[1],NumF[1]]
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
st.pyplot(fig1)

