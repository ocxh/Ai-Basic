# 경사하강법을 통한 학습
import numpy as np

xy = np.array([[1., 2., 3., 4., 5., 6.],
              [10., 20., 30., 40., 50., 60.]])

x_train = xy[0]
y_train = xy[1]

weight = np.random.rand(1)  # 직선의 기울기
bias = np.random.rand(1)  # y절편

learning_rate = 0.001

for i in range(1000):
    pred = (x_train * weight) + bias
    error = ((pred - y_train) ** 2).mean()

    gd_w = ((pred - y_train) * 2 * x_train).mean()
    gd_b = ((pred - y_train) * 2).mean()

    weight -= learning_rate * gd_w
    bias -= learning_rate * gd_b

    if i % 100 == 0:
        print("Epoch ({:10d}/1000) error: {:10f}, weight: {:10f}, bias:{:10f}".format(
            i, error, weight.item(), bias.item()))
