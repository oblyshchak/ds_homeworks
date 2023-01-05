import numpy as np
import matplotlib.pyplot as plt

x = [6, 7, 8, 9, 10, 11, 12, 13, 14]

y = [0.025, 0.1, 0.25, 0.45, 0.6, 0.75, 0.875, 0.95, 1.0]
# ax = plt.subplot()
# data = [x, y]
# columns = ('F*(x)', 'x')
# rows = []
# for i in range(len(x)):
#     rows.append([x[i], y[i]])

# table = ax.table(cellText=rows, loc='lower right', )
# plt.table(rowLabels=rows)
# ax.add_table(plt.table(rowLabels=rows))
plt.style.use('seaborn')

plt.step(x, y)
plt.show()