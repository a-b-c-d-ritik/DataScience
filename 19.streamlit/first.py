import streamlit as st;

st.title("Hello World!!!")
st.subheader(" Ye sub Header h")
st.text("gags hsjhjsbsa bsabusabusa suagushsab hsaqhasb hsauhsuab s ")
st.write("fav choose karo")

var1=st.selectbox("options:",["c","c++","java","Python","JS"])
if var1:
    st.write(var1)

st.success(f"{var1} ,course liya h na apne, Badhiya..")

