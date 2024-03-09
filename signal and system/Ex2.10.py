#try0310
import numpy as np
import matplotlib.pyplot as plt

# 定義輸入信號 x 和系統響應 h
n = np.arange(-15, 15)
x1 = (2**(n.astype(float))) * (n <= 0) 
x2 = (0.5**n.astype(float)) * (n >= 0)
x =  x1 + x2
h = (n >= 0)

# 使用NumPy的卷積函數
y = np.convolve(x, h, mode="same")

# 繪製原始信號和系統響應
plt.subplot(3, 1, 1)
plt.stem(n, x, label='Input Signal')
plt.title('Input Signal')

plt.subplot(3, 1, 2)
plt.stem(n, h, label='System Response')
plt.title('System Response')

# 繪製卷積結果
plt.subplot(3, 1, 3)
plt.stem(n, y[:len(n)], label='Convolution Result')  # 修正此處以保持信號位置一致
plt.title('Convolution Result')

plt.tight_layout()
plt.show()
