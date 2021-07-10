# Exercise , Number guessing game
# make a variable , like winning_number and assign any number to it
# ask user to guess a number
# if user guessed correctly then print  " YOU WIN !!"
# if user didn't guessed corectly then :
 # if user guessed lower than actual number then print  " Too low"
 # if user guessed higher than actual number then print  " Too High "

 # can use random number in python to generate random winning number

import random
winning_number = random.randint(1,100)
guess = 1
guessing_number= int(input("Enter your guessed number between 1 to 100:"))
game_over = False
while not game_over:

    if winning_number == guessing_number:
            print(f"YOU WIN!! , and you guessed this number in {guess} times")
            game_over = True

    else:   # nested if else
        if guessing_number < winning_number:
                    print("Too LOwW !")
                   
        else :
                    print("Too HIGH !!")
         # dont repeat this mistake again
        guess += 1
        guessing_number = int(input("guess again :"))soaouso