def palindrome_chain_length(n):
    count = 0
    while n != int(str(n)[::-1]):
        n += int(str(n)[::-1])
        count += 1
    else:
        return count
        
palindrome_chain_length(921)
