# t= int(input("Enter the number till for which you want to print the table: "))
T=5
for i in range(0,T+1):
    mark=(f"**** Table of {i} ****")
    for j in range(0, 10):
        sol = (f"{i}x{j+1} = {i*(j+1)}")    
        print(sol)
        with open("table.txt", "a+") as file:
            if j==0:
                file.write(f"\n{mark}\n")
            file.write(f"{sol}\n")

print(" end of table")