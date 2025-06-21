import random
#library which gives random values

name = input (" what is your name? ")
#name of user

print ("goood luck!", name )

words = ['rainbow', 'school', 'college', 'friends', 'family', 'work', 'travelling']
# random words which will be choosen 

word = random.choice(words)

print("Guess the letter:")
print ("Guess from one of these:", words)
guesses = ''

turns = 10
# n number of turns can be used

while turns > 0:
    
    failed = 0
    #number of times user can fails 
    
    for char in word:
    # all characters from the input word taking one at a time.

        if char in guesses:
            print ( char, end=" " )            
            #comparing the char if present in word
            
        else:
            print("_")
            # if failed 1 will be added in failure
            
            failed +=1
            
            
    if failed == 0:
        print ("You Win!")
            
        print ("the word is : ", word )   
        break
        #if user is failed 0 times then it will print 'You Win!' with the right word
        
    print ()
    guess = input("Guess the character: ")
    # if user guess is wrong it will ask for another guess
    
    guesses += guess
    #if guess is right it will be stored 
    
    if guess not in word:
        
        turns -=1 
        print ("Wrong")
        
        print ( 'you have', +turns, 'more turns')
        # this prints the number of turns left 
        
        print ("You Loose!")
        #if turns completed and user cannot guess the word it prints 'You Loose!'
        