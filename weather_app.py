import streamlit as st
import requests
import json
import matplotlib.pyplot as plt

# 发送 GET 请求以获取天气数据
result = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en')

# 解析 JSON 数据
result_dict = json.loads(result.text)

# 设置 Streamlit 标题
st.title("实时天气温度")

# 打印状态码
st.write(f"状态码: {result.status_code}")

# 提取温度数据
if "temperature" in result_dict:
    temperature_data = result_dict["temperature"]["data"]
    
    # 创建一个字典来存储位置和温度
    locations = [location['place'] for location in temperature_data]
    temperatures = [location['value'] for location in temperature_data]
    
    # 在侧边栏中添加选择框
    selected_location = st.sidebar.selectbox("选择一个地点", locations)
    
    # 显示所选地点的温度
    selected_temp = next((location['value'] for location in temperature_data if location['place'] == selected_location), None)
    st.sidebar.write(f"{selected_location} 的温度: {selected_temp}°C")
    
    # 绘制条形图
    fig, ax = plt.subplots()
    ax.barh(locations, temperatures, color='skyblue')
    ax.set_xlabel('温度 (°C)')
    ax.set_title('不同地点的温度')
    
    st.pyplot(fig)
else:
    st.write("JSON 响应中未找到温度数据。")