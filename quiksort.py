def quicksort(arr):
  if len(arr) < 2:
    return arr
  else:
    piv = arr[0]
    smaller = [i for i in arr[1:] if i <= piv]
    greater = [i for i in arr[1:] if i > piv]
    return quicksort(smaller) + [piv] + quicksort(greater)

array = [321, 45, 1, 52, -2, 4]
print(quicksort(array))