#      * 
#      **
#     ****
#    ******
#   ******** 
#  **********   
# ************
row = int(input())
for i in range(1,row+1):
    print(" "* int(row-i), end=" ")
    print(" *"*i)
    