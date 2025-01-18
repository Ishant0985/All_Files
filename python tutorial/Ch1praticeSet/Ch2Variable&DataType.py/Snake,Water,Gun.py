import random as r

def start_game():
    c=r.randint(1,3 )
    print("Snake, Water & Gun game")
    l1 = ["Snake"," Water", "Gun "]
    print(f"1. {l1[0]} 2. {l1[1]} 3. {l1[2]}" )
    user = int(input("Choose any one option. 1, 2 or 3 :\n"))
    try:
        if 0 < user < 4:
            if c == user:
                print(f"Bot and You Both Choose {l1[c-1]}\n Tie")
            elif c == 1 and c==2:
                print(f"Bot Choose {l1[c-1]} , Bot Win ")
            
            elif c == 1 and user != c and c==3:
                print(f"Bot Choose {l1[c-1]} , You Win ")
            
            elif c == 2 and user != c and c==1:
                print(f"Bot Choose {l1[c-1]} , You Win ")
            
            elif c == 2 and user != c and c==3:
                print(f"Bot Choose {l1[c-1]} , Bot Win ")
            
            elif c == 3 and user != c and c==2:
                print(f"Bot Choose {l1[c-1]} , You Win ")
            
            elif c == 3 and user != c and c==1:
                print(f"Bot Choose {l1[c-1]} , Bot Win ")
    except Exception as e:
        print(e)
    
for i in range(5):
    start_game()