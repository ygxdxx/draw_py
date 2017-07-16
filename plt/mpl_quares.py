import matplotlib.pyplot as plt

# 输入结果
input_values = [1, 2, 3, 4, 5]
# 输出结果
squares = [1, 4, 9, 16, 25]
# plt.plot(squares)
# 线条宽度
plt.plot(input_values, squares, linewidth=5)
# 标题
plt.title('square of numbers')
# x轴标签
plt.xlabel('value', fontsize=14)
# y轴标签
plt.ylabel('square of value', fontsize=14)
# 刻度标记大小 默认 x y 都修改
plt.tick_params(labelsize=14)
# 显示
plt.show()

