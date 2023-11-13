import numpy as np

s_1 = list(map(lambda x, y: pow(pow(x, 2)+pow(y, 2), 1/2), (range(1, 5, 1)), (range(1, 5, 1))))
print(s_1)

s_2 = list(map(lambda x: pow(x, 2), (range(1, 5, 1))))
print(s_2)

s_3 = np.square((range(1, 5, 1)))
print(s_3)
