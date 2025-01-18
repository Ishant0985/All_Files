import random as R
import string

coding = input("Enter what you want to do:\n a. coding \n B. Decoding \n").lower()

if (coding == "a"):
    st = input("Enter The word to code :\n")
    words = st.split()
    new_words = []
    for word in words:
        if (len(word)>=3):
            r1=(''.join(R.choices(string.ascii_letters,k=4)))
            r2=(''.join(R.choices(string.ascii_letters,k=4)))
            stword = r1 + word[1:] + word[0] + r2
            new_words.append(stword)
        else:
            new_words.append(word[::-1])
    print(" ".join(new_words))
else:
    st = input("Enter the Word to Decode :\n")
    words = st.split()
    new_words = []
    for word in words:
        if (len(word)>=3):
            stword =  word[4:-4]
            stword = stword[-1] + stword[:-1] 
            new_words.append(stword)
        else:
            new_words.append(word[::-1])
    print(" ".join(new_words))