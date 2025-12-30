import numpy as np
import time
import matplotlib.pyplot as plt

def DFT(x):
    x = np.asarray(x, dtype=complex)
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)
    return X

# Các kích thước dữ liệu thử nghiệm
Ns = [32, 64, 128, 256, 512]
times = []

for N in Ns:
    x = np.random.rand(N)
    start = time.time()
    DFT(x)
    end = time.time()
    times.append(end - start)
plt.figure()
plt.plot(Ns, times, marker='o')
plt.xlabel("kich thuoc N")
plt.ylabel("thoi gian chay (giay)")
plt.title("thoi gian chay cua thuat toan DFT theo kich thuoc du lieu")
plt.show()