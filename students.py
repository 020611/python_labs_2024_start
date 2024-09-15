import json

# 读取 JSON 文件
with open('students.json', 'r') as file:
    data = json.load(file)

# 获取学生列表
students = data.get('students', [])

# 打印每个学生的信息
for student in students:
    print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")

#print the second student's name
print(f"Second student's name:{students[1]['name']}")
print(f"Second student's age:{students[1]['age']}")