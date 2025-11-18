import random

Scret = random.randint(0 ,10)

for i in range(3):
    guess = int(input("Enter a number(0-10):"))

    if guess== Scret:
        print("Numbers match!you win!")
        break
    
    elif guess > Scret:
        print("chosen number is too high.")

    else:
        print("Chosen number is too low.")

        print("The number was:",Scret)