p=1
while p<=10:
    a = int(input("Enter 1st Number :-  "))
    b = int(input("Enter 2nd Number :-  "))
    c=a+b
    if c>0:
        print(f"The Sum of two Numbers are :- {a+b}")
    else:
        print(f"The product of two numbers are :- {a*b}")
        p=p+1