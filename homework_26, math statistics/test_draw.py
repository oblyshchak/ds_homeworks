import matplotlib.pyplot as plt

x = [0, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#w = [0.025, 0.075, 0.15, 0.2, 0.15, 0.15, 0.125, 0.075, 0.05]
# {6: 1, 7: 3, 8: 6, 9: 8, 10: 6, 11: 6, 12: 5, 13: 3, 14: 2}
n = [0, 1, 3, 6, 8, 6, 6, 5, 3, 2, 0]
plt.plot(x, n, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)

plt.ylim(0)
plt.xlim(0)
plt.xlabel('Xi - axis')
plt.ylabel('Ni - axis')
plt.title('Frequency polygons')
plt.show()