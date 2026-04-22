import random


def get_secret_number():
    return random.randint(1, 100)

def get_guess():
    return int(input("Take a guess: "))

def check_guess(guess, secret_number):
    if guess < secret_number:
        print("Too low!Try again")
    elif guess > secret_number:
       print("Too  high!Try again")    

    else:   
         return True
    
def play_game():
    secret_number = get_secret_number()    
    attempts = 0
    print("I am thinking of a number between 1 and 100")
    while True:
        guess = get_guess()
        attempts += 1
        if check_guess( guess, secret_number) == True:
         print(f" You got  it in {attempts} attempts!") 
         break

play_game()      
        
    


