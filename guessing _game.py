import random 


secret_number = random.randint(1, 10)
attempts = 0

print("I am thinking of a number between 1 and 10!")

while True :
    guess = int(input("Take a guess:"))
    attempts += 1
    if guess < secret_number:
           print("Too low!Try again")
    elif guess > secret_number:
          print("Too high Try again")       
    else:
          print(f"You got in {attempts} attempts!")

          break