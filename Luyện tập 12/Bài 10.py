import matplotlib.pyplot as plt

x = list(range(-10, 11))

y1 = [i**2 for i in x]
y2 = [i**3 for i in x]

plt.plot(x, y1, label="y = x^2")
plt.plot(x, y2, label="y = x^3")

plt.legend()
plt.title("Đồ thị hàm số")

plt.show()