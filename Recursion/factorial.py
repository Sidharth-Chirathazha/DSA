def factorial(num):

    if num == 1 or num == 0:
        return num
    else:
        return num * factorial(num-1)
    
if __name__ == '__main__':
    num = 10
    print(f"Factorial of {num} is {factorial(num)}")