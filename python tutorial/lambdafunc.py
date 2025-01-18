cube = lambda x: x**3


def fibonacci(n):
    if n<=1 or n==0:
        return 1
    else:
        return n*fibonacci(n-1)

if __name__ == '__main__':
    n = int(input())
    #print(fibonacci(n))
    
    print(list(map(cube, fibonacci(n))))