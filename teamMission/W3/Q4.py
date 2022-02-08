# weight와 bias값 정의하기
import numpy as np

xy = np.array([[1., 2., 3., 4., 5., 6.],
              [10., 20., 30., 40., 50., 60.]])

x_train = xy[0]
y_train = xy[1]

weight = np.random.rand(1)
bias = np.random.rand(1)

print(weight)
print(bias)
