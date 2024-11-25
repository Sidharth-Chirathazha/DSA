def reverse_sen(strng):
    word = ""
    word_lst = []
    for i in strng:
        if i == " ":
            if word:
                word_lst.append(word)
                word = ""
        else:
            word += i
    if word:
        word_lst.append(word)
            
    return ' '.join(word_lst[::-1])
    
strng = 'hello world'

print(reverse_sen(strng))