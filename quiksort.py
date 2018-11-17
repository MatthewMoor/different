import random

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
#______________________________________________________________________________________

def quicksort_two(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q]
 
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksort_two(l_nums) + e_nums + quicksort_two(b_nums)

print(quicksort_two(array))