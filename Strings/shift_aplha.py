def shift_characters(s,n):

    result = []
    for char in s:
        if char.isalpha():

            base = ord('A') if char.isupper() else ord('a')

            new_char = chr((ord(char)-base + n)%26 + base)

            result.append(new_char)
        else:
            result.append(char)
        
    return ''.join(result)

if __name__ == '__main__': 
    res = shift_characters('Sidharth',3)

    print(res)