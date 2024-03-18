import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# โหลดข้อมูลอุบัติเหตุ
accident_df = pd.read_excel("data/DATA.xlsx")

# แสดงชื่อเว็บแอปพลิเคชัน
st.title("การวิเคราะห์ข้อมูลอุบัติเหตุในประเทศไทย")

# แสดงภาพรวมเกี่ยวกับอุบัติเหตุ
st.markdown("""
ข้อมูลชุดนี้ประกอบด้วยข้อมูลเกี่ยวกับอุบัติเหตุในประเทศไทย 
ข้อมูลนี้สามารถใช้เพื่อวิเคราะห์สาเหตุ 
ประเภทของอุบัติเหตุ สถานที่ 
และจำนวนผู้เสียชีวิตจากอุบัติเหตุ

""")

# แสดงจำนวนผู้เสียชีวิต
col1, col2 = st.columns(2)

with col1:
    st.subheader("จำนวนผู้เสียชีวิต")
    st.write(accident_df["เสียชีวิต"].sum())

with col2:
    st.subheader("จำนวนผู้บาดเจ็บ")
    st.write(accident_df["บาดเจ็บ"].sum())

# แสดงข้อมูลอุบัติเหตุแยกตามเพศ
st.header("ข้อมูลอุบัติเหตุแยกตามเพศ")

male_df = accident_df[accident_df["เพศ"] == "ชาย"]
female_df = accident_df[accident_df["เพศ"] == "หญิง"]

st.dataframe(male_df.head(1))

# แสดงกราฟแท่งแสดงจำนวนผู้เสียชีวิตแยกตามเพศ
st.subheader("จำนวนผู้เสียชีวิตแยกตามเพศ")

male_deaths = male_df["เสียชีวิต"].sum()
female_deaths = female_df["เสียชีวิต"].sum()

sex_data = [male_deaths, female_deaths]
sex_labels = ["ชาย", "หญิง"]

st.bar_chart(sex_data, labels=sex_labels)

# แสดงกราฟวงกลมแสดงจำนวนผู้เสียชีวิตแยกตามเพศ
st.subheader("สัดส่วนจำนวนผู้เสียชีวิตแยกตามเพศ")

fig1, ax1 = plt.subplots()
ax1.pie(sex_data, labels=sex_labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
st.pyplot(fig1)

# เพิ่มตัวเลือกสำหรับผู้ใช้ในการกรองข้อมูล
st.sidebar.header("ตัวกรองข้อมูล")

year_option = st.sidebar.selectbox("เลือกปี", accident_df["ปี"].unique())
month_option = st.sidebar.selectbox("เลือกเดือน", accident_df["เดือน"].unique())

filtered_df = accident_df[(accident_df["ปี"] == year_option) & (accident_df["เดือน"] == month_option)]

st.dataframe(filtered_df)
