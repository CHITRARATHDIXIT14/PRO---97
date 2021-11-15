import random

new = random.randint(1,9)
#print(new)

print("Welcome to my game !")
print("Guess a number between (1,9) ")
guess = input("Enter your number :")

chance = 0

while chance < 5 :
    if guess == new : 
        print('You won ')
    elif chance < 5 :
        print('You loose . The number is ' , new)
        break
    else : 
        print('Your chances are over ')
    
    chance = chance+1
    

