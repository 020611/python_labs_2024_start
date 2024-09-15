import streamlit as st # type: ignore

st.title("Simple Streamlit App")

# 创建输入框
user_input = st.text_input("请输入一些内容:")

# 创建提交按钮
if st.button("提交"):
# 显示用户输入的内容
   st.write("您输入的内容是:", user_input)