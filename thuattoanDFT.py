import numpy as np
def DFT(x):
    # """
    # Tính biến đổi Fourier rời rạc (DFT) của dãy x
    # x: mảng 1 chiều (list hoặc numpy array), độ dài N
    # return: mảng X chứa kết quả DFT
    # """
    x = np.asarray(x, dtype=complex)
    N = x.shape[0]
    X = np.zeros(N, dtype=complex)

    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)

    return X
x = [1, 2, 3, 4]
X = DFT(x)
print("tin hieu x[n]:")
print(x)
print("DFT X[k]:")

print(X)
