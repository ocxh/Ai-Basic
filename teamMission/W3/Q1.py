# 행열곱 연산
import numpy as np

arr1 = np.random.rand(5, 3)
arr2 = np.random.rand(3, 2)

result = np.dot(arr1, arr2)
print(result)
print("shape: ", result.shape)
