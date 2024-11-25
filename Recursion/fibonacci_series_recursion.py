def fib_series(num):

    if num <= 1:
        return num
    else:
        return (fib_series(num-1) + fib_series(num-2))
    
if __name__ == '__main__':

    num = 20
    result = []
    for i in range(num):
        result.append(fib_series(i))        
    print(result)