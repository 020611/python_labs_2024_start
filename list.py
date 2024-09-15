
print ('hello world')

# 创建一个包含水果名称的列表
fruits = ['apple', 'banana', 'cherry']
# 访问列表中的第一个元素
first_fruit = fruits[0]
print(first_fruit)
# 修改列表中的第二个元素
fruits[1] = 'blueberry'
print(fruits)
# 添加新元素到列表末尾
fruits.append('orange')
print(fruits)
# 删除列表中的指定元素
fruits.remove('cherry')
print(fruits)
# 获取列表的长度
length = len(fruits)
print(length)
# 遍历列表中的所有元素
for fruit in fruits:
    print(fruit)