import numpy as np

data = np.array([1000, 2500, 1400, 1800, 900, 4200, 2200, 1900, 3500])
#add new arrey
a = int(input())
add = np.append(data,a)

#sort the array

sorted = np.sort(add)
print(sorted)