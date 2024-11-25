

def remove_char(string,char):
    if string == '':
        return ''
    
    if string[0] == char:
        return remove_char(string[1:],char)
    else:
        return string[0] + remove_char(string[1:],char)
    
def remove_vowels(string,vwls):
    if string == '':
        return ''
    if string[0] in vwls:
        return remove_vowels(string[1:],vwls)
    else:
        return string[0] +  remove_vowels(string[1:],vwls)
    

string = 'Hello World'

res = remove_char(string,'l')
print(res)

vowels = ['a','e','i','o','u']
string_2 = 'appple gone'
res_2 = remove_vowels(string_2,vowels)
print(res_2)