# 创建一个包含水果及其颜色的字典
fruit_colors = {
    'apple': 'red',
    'banana': 'yellow',
    'cherry': 'red'
}
# 获取 'apple' 的颜色
apple_color = fruit_colors['apple']
print(apple_color)
# 添加 'orange' 及其颜色
fruit_colors['orange'] = 'orange'
print(fruit_colors)
# 删除 'cherry'
del fruit_colors['cherry']
print(fruit_colors)
# 修改 'banana' 的颜色
fruit_colors['banana'] = 'green'
print(fruit_colors)
# 检查 'apple' 是否在字典中
is_apple_in_dict = 'apple' in fruit_colors
print(is_apple_in_dict)  # 输出: True
# 遍历字典中的键值对
for fruit, color in fruit_colors.items():
    print(fruit, color)

