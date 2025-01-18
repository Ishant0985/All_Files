# A
# B B
# C C C
# D D D D

n=ord(input("Enter Character Till To Make Pattern : \n"))
for i in range(65,n+1):
    for j in range(65,i+1):
        print(chr(i),end=" ")
    print("")
