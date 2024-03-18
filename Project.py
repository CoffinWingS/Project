import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# โหลดข้อมูล
data = pd.read_excel("data/DATA.xlsx")

# แสดงชื่อเว็บแอปพลิเคชัน
st.title("สถิติการเกิดอุบัติเหตุในประเทศไทย")

# แสดงข้อมูลภาพรวม
st.markdown("""
ข้อมูลสถิติการเกิดอุบัติเหตุในประเทศไทย 
ข้อมูลนี้ประกอบด้วยข้อมูลเกี่ยวกับจำนวนผู้เสียชีวิต 
และจำนวนผู้บาดเจ็บจากอุบัติเหตุ แยกตามเพศ
""")

# แสดงจำนวนผู้เสียชีวิตและบาดเจ็บ
col1, col2 = st.columns(2)

with col1:
    st.subheader("จำนวนผู้เสียชีวิต")
    st.write(data["เสียชีวิต"].sum())

with col2:
    st.subheader("จำนวนผู้บาดเจ็บ")
    st.write(data["บาดเจ็บ"].sum())

# แสดงข้อมูลแยกตามเพศ
st.header("ข้อมูลแยกตามเพศ")

# เพิ่มตัวเลือกสำหรับผู้ใช้ในการกรองข้อมูล
gender_option = st.sidebar.selectbox("เลือกเพศ", ["ชาย", "หญิง"])

filtered_df = data[data["Sex"] == gender_option]

# แสดงจำนวนผู้เสียชีวิตและบาดเจ็บแยกตามเพศ
col1, col2 = st.columns(2)

with col1:
    st.subheader("จำนวนผู้เสียชีวิต")
    st.write(filtered_df["เสียชีวิต"].sum())

with col2:
    st.subheader("จำนวนผู้บาดเจ็บ")
    st.write(filtered_df["บาดเจ็บ"].sum())

# แสดงกราฟวงกลม
fig1, ax1 = plt.subplots()
ax1.pie(filtered_df.groupby("Sex").size(), labels=["ชาย", "หญิง"], autopct='%1.1f%%', shadow=True, startangle=90)
st.pyplot(fig1)

# แสดงข้อมูลตาราง
st.dataframe(filtered_df)

