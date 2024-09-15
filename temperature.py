import requests
import json

# 发送 GET 请求以获取天气数据
result = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en')

# 将 JSON 响应保存到文件中
with open('weather.json', 'w') as f:
    output_json = json.dumps(result.json(), indent=4, sort_keys=True)
    f.write(output_json)

# 解析 JSON 数据
result_dict = json.loads(result.text)

# 打印状态码
print(result.status_code)

# 提取并打印不同位置的温度信息
if "temperature" in result_dict:
    temperature_data = result_dict["temperature"]["data"]
    for location in temperature_data:
        print(f"Location: {location['place']}, Temperature: {location['value']}°C")
else:
    print("Temperature data not found in the JSON response.")