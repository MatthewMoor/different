# How i solved
def odd(n):
	first_num = n * (n-1) + 1
	value = 0
	for i in range(n):
		value += first_num
		first_num += 2
	return value
	
# How was it possible
def odd_new(n):
	return n ** 3
	
_ = odd(5)
print(_)
_ = odd_new(6)
print(_)
