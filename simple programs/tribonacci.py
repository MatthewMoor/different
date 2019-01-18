def tribonacci(signature, n):
    a, b, c = signature[0], signature[1], signature[2]
    array = []
    array.append(a)
    array.append(b)
    while len(array) != n:
        array.append(c)
        a, b, c = b, c, c+a+b
    return array

tribonacci([1, 1, 1], 10)
