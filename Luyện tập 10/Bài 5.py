import numpy as np
import matplotlib.pyplot as plt

# tạo dữ liệu
x1 = np.linspace(-10, 10, 100)   # cho y = x^2
x2 = np.linspace(0, 10, 100) # cho y = sqrt(x) (không âm)


y1 = x1 ** 2
y2 = np.sqrt(x2)


# tao figure với 1 hàng, 2 cột
plt.figure()

# Subplot bên trái
plt.subplot(1, 2, 1)
plt.plot(x1, y1)
plt.title("do thi y = x^2")
plt.xlabel("x")
plt.ylabel("y")

# Subplot bên phải
plt.subplot(1, 2, 2)
plt.plot(x2, y2)
plt.title("do thi y = sqrt(x)")
plt.xlabel("x")
plt.ylabel("y")

# hiển thị

plt.tight_layout()
plt.show()