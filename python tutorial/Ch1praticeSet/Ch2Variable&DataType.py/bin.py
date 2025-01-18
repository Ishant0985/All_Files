if __name__ == '__main__':
    n = int(input().strip())
    new = bin(n)[2:]
    print(new)
    new.count(1)
    print(new)