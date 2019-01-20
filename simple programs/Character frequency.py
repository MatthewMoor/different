def letter_frequency(text):
    arr = []
    low = text.lower()
    signs = [' ', '!', ':', ';', '?', '.', ',']
    
    for i in signs:
        if i in low:
            low = low.replace(i, '')
        
    variety = set(low)
    
    for i in variety:
        count = 0
        if type(i) is str:
            for j in low:
                if i == j:    
                    count += 1
            arr.append(tuple((i, count)))
    print(sorted(arr, key=lambda tup: (-tup[1], tup[0])))
   
