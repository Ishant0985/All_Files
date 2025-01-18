i=0 
n = int(input("Enter the of which you want the table of :"))
while True:
    print(f"{n} X {i+1} = {(i+1)*n}")
    i = i+1
    if i==10:
        break