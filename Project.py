import streamlit as st
import pandas as pd

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


#st.write กราฟแท่ง
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
labels = 'Male', 'Female'
sizes = [NumM[1],NumF[1]]
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
st.pyplot(fig1)


import matplotlib.pyplot as plt


# เรียงลำดับข้อมูลตามจำนวนผู้เสียชีวิต
dt = df.sort_values("จ.ที่เสียชีวิต", ascending=False)

# แสดงกราฟแท่ง
plt.bar(df["จ.ที่เสียชีวิต"], df["จำนวนผู้เสียชีวิต"])
plt.xlabel("จังหวัด")
plt.ylabel("จำนวนผู้เสียชีวิต")
plt.title("อัตราการเสียชีวิตในจังหวัดต่างๆ ของประเทศไทย")

# แสดงค่าตัวเลขบนแท่ง
for i in range(len(dt)):
    plt.text(i, dt["จำนวนผู้เสียชีวิต"][i], dt["จำนวนผู้เสียชีวิต"][i], ha="center", va="bottom")

# แสดงกราฟ
plt.show()
