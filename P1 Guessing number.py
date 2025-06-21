import random

def guessing_number():
    
    number_to_guess = random.randint(1 , 50)    
    attempts = 0
    
    print("Welcome to guessing game! Guess your number between 1 to 50.")
    
    while True:
        guess = int(input("Enter Your Guess : "))
        attempts +=1

        if guess < number_to_guess :
            print( "Too Low!" )  
        elif guess > number_to_guess :
            print("Too High!")
        else :
            print("You guessed the right number {number_to_guess} , in {attempts} attempts")
        
guessing_number()