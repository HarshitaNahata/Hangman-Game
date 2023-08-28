import random
#words=["SKYVIEW","PYTHON","JAVA","DEVELOPER"]
f=open("words.txt","r")
data=f.readline()
words=data.split()
word=random.choice(words)
word=word.upper()
chances = 7
guessed_word="-"*len(word)
while chances !=0:
    print(guessed_word)
    letter = input("Guess a letter: ").upper()
    if letter in word:
        for index in range (len(word)):
            if word[index]==letter:
                guessed_word=guessed_word[:index]+letter+guessed_word[index+1:]
                #print(guessed_word)
        if guessed_word==word:
            print("Congratulations!!")
            break
    else:
        chances-= 1
        print("Wrong guess")
        print("Remaining chances are :",chances)
else:
    print("GAME OVER")
    print("You lost")
print("The correct word is ",word)