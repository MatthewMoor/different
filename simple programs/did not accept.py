def square_digits(x):
    words = list(str(x))
    for word in words:
        print(int(word)**2, end='')
        
square_digits(98761)
