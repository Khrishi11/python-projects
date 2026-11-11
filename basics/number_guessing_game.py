# Activity 5: Number Guessing Game
# Create a game in which user guesses a random number in python.

import random as r

play_again = True

while play_again:
    try: 
        print ("""  Welcome to the Number Guessing Game!
        - You have to guess a number between 1 and 100
        - You have 5 attempts to guess the number """)
        
        n = r.randint(1, 100)
        i = 0

        while i < 5:
            guess = int(input("Enter your guess: "))
            
            if guess < 1 or guess > 100:
                print ("Please enter a number between 1 and 100.")
            elif guess < n:
                print ("Your guess is too low.")
                i += 1
            elif guess > n:
                print ("Your guess is too high.")
                i += 1  
            elif guess == n:
                print ("Congratulations! You guessed the number correctly.")
                break
        else:
            print ("Sorry, you've used all your attempts. The number was:", n)  

        tryagain = input("Do you want to try again? (yes/no): ")
        if tryagain.lower() != "yes":
            play_again = False
            print ("Thank you for playing!")

    except ValueError:
        print ("Please input a valid integer.")
        exit()