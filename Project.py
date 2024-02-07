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

dt.pd.read_excel('data/opendata-rtddi-54-66-9month.xlsx')

#st.write
Nummale=dt[dt['Sex']=='ชาย'].mode()
NumFemale=dt[dt['Sex']=='หญิง'].mode()

dtSex=[NumM,NumF]
dtSexd=pd.DataFrame(dtSex)
st.bar_chart(dtSexb)