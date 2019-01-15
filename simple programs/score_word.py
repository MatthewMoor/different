def sum_word(string):
    #But it was possible in one line :/
    digits = [i for i in range(1, 27)]
    letters = ['a', 'b', 'c', 'd', 'e', 'f',
               'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            
    dic = dict(zip(letters, digits))
    score_word = []
    word = []
    
    a = string.lower().split()
    for words in a:
        score = 0
        word.append(words)
        for letter in words:    
            score += dic.get(letter.lower(), 0)  
        score_word.append(score)
        
    dic2 = dict(zip(word, score_word))
    return max(dic2, key = dic2.get)
    
best_word = sum_word(str(input('Write message without digits --------> ')))
print(best_word)
