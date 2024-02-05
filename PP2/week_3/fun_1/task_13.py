import random

def game():
     name = input("Hello! What is your name? \n")
     guess = 0
     num = 0
     a = random.randrange(1, 20)
     print(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.".format(fname = name))
     while num != a:
         num = int(input())
         if num < a:
             guess += 1
             print("Your guess is too low.\nTake a guess.")
         elif num > a:
             guess += 1
             print("Your guess is too big.\nTake a guess.")
         elif guess == 3:
             print("You're out of guesses, try again")
         else:
             guess +=1
             print(f"Good job, {name}! You guessed my number in {guess} guesses!".format(fname = name, fguess = guess))
             break
 
game()