import math
import numpy as np

x_list = [1, 2, 3, 4]
y_list = [1, 2, 3, 4]
s = map(lambda x, y: math.sqrt(x**2+y**2), x_list, y_list)
print(list(s))

arr_x = np.square(x_list)
print(arr_x)

b = [x**2 for x in x_list]
print(b)

def square(number):
    return number ** 2
squared = map(square, x_list)
print(list(squared))
