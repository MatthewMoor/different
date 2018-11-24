import numpy as np

array = [int(i) for i in range(5)]
arr_copy = array.copy()
for i in array:
  for count, val in enumerate(arr_copy):
    if i != 0:
      arr_copy[count] = val * i
  print(arr_copy)
  arr_copy = array.copy()