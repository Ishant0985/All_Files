import random as r

# Initialize score counters
player_score = 0
bot_score = 0

# ASCII art for options
snake_art = """
    ~~~~
  //     \\
 //       \\
\\        //
 \\______//
    ~~~~
"""
water_art = """
    ~~~~~~
   ~      ~
  ~        ~
  ~        ~
   ~      ~
    ~~~~~~
"""
gun_art = """
     ||
    ||||
    ||||
    ||||
    ||||
   | __ |
   |____|
"""

# Function to display the ASCII art
def display_ascii_art(choice):
    if choice == 1:
        print(snake_art)
    elif choice == 2:
        print(water_art)
    elif choice == 3:
        print(gun_art)

def play_game():
    global player_score, bot_score
    
    print("Snake, Water & Gun game")
    l1 = ["Snake", "Water", "Gun"]
    c = r.randint(1, 3)
    print(f"1. {l1[0]} 2. {l1[1]} 3. {l1[2]}")
    
    user = int(input("Choose any one option. 1, 2 or 3\n"))
    
    try:
        if 0 < user < 4:
            print("\nYou chose:")
            display_ascii_art(user)
            
            print("Bot chose:")
            display_ascii_art(c)
            
            if c == user:
                print(f"Bot and You both chose {l1[c-1]}\nTie")
            elif (c == 1 and user == 2) or (c == 2 and user == 3) or (c == 3 and user == 1):
                print(f"Bot chose {l1[c-1]} , Bot Wins")
                bot_score += 1
            else:
                print(f"Bot chose {l1[c-1]} , You Win")
                player_score += 1
    except Exception as e:
        print(e)

# Play 5 rounds
for i in range(5):
    play_game()

# Display final score and winner
print("\nFinal Scores:")
print(f"You: {player_score}")
print(f"Bot: {bot_score}")

if player_score > bot_score:
    print("Congratulations! You are the Winner! 🏆")
elif player_score < bot_score:
    print("Bot Wins! Better luck next time!")
else:
    print("It's a Tie!\n")

# Author
print("Made by **Ishant Yadav** with ❤️ in India.")
