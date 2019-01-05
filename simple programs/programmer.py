s = int(input())
a = 'программистов'
b = 'программиста'
c = 'программист'
if s % 10 == 1 and s % 100 != 11:
    print(str(s) + ' ' + c)
elif s % 10 >= 2 and s % 10 <= 4 and s % 10 != 12 and s % 10 != 13 and s % 10 != 14 and s % 100 != 12 and s % 100 != 13 and s % 100 != 14:
    print(str(s) + ' ' + b)
else:
    print(str(s) + ' ' + a)