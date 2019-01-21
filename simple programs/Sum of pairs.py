def observer(arr, n):
	# Error 137 because of loop
    if arr:    
        quantity = len(arr)
    if arr:    
        for i in range(quantity-1):
            plus = 0
            print(arr[i+1])
            plus = arr[i] + arr[i+1]
            if plus == n:
                return [arr[i], arr[i+1]]
                
        for i in range(quantity):
            plus = 0
            for j in range(quantity):
                plus = arr[i] + arr[j]
                if plus == n:
                    return [arr[i], arr[j]]
                plus = 0
        return None
    else:
        return None
        

observer([10, 5, 2, 3, 7, 5], 10)
