import matplotlib.pyplot as plt

# 输入数据
x_values = list(range(1, 1001))
# 输出数据
y_values = [value ** 2 for value in x_values]
# 绘制一个点
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=20, edgecolors='none')
# 添加标题
plt.title('Square Numbers', fontsize=14)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)
plt.tick_params(labelsize=14, which='major')
plt.axis([0, 1100, 0, 1100000])

plt.show()
