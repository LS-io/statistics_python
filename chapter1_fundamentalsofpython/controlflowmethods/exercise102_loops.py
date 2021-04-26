##In this exercise, we will play a guessing game, where the user of the script will be prompted to guess a number between 0 and 100, and tell the user 'Higher' or 'Lower', depending on the accuracy of the guess
import random
true_value = random.randint(0, 100)

exit = False
while exit == False:
    guess = input('Enter your guess: ')

##We will be implementing the code inside a try...except block, in order to handle the situation when the user inputs a non-numeric value
    try:
        guess = int(guess)
        
        if guess == true_value:
            print('Congratulations! You guessed correctly.')
            print('Thank you for playing! :)')
            exit = True
        elif guess > true_value:
            print('Lower.') #The user's guess was too high
        else:
            print('Higher') #The user's guess was too low

    # when the input is invalid
    except ValueError:
        print('Please enter a valid number.')