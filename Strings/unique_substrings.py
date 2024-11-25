def unique_string(string):
    char_count = {}
    for s in string:
        if s in char_count:
            char_count[s] += 1
        else:
            char_count[s] = 1
    return ''.join([ch for ch in string if char_count[ch] == 1])

string = 'hello world'

print(unique_string(string))