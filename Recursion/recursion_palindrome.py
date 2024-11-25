def check_palindrome(word):
 
 if len(word) <= 1: #Base case , we need to reach until a single character for a string to be palindrome using recursion
  return True
 
 if word[0] != word[-1]: #The false case whenever a situation arise where the start character is not equal to end character
  return False
 
 return check_palindrome(word[1:-1]) #Recursive case , always pass the string to same funtion by removing first and last characters

word = 'malayalam'

if check_palindrome(word):
 print(f"{word} is palindrome")
else:
 print(f"{word} is not palindrome")