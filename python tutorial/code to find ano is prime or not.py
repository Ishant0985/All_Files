n = int(input())
if n>1:
    for i in range(2,(n//2)+1):
        if n%i==0:
            print(f"The number {n} is not Prime")
            break
    else:
        print(f"The number {n} is Prime")
else:
    print(f"The number {n} is not Prime")
