
def guess():
    num_guess = 0
    c = 0
    while(num_guess != number):
        num_guess = int(input())
        c = c + 1

        if(num_guess < number):
            print("OOPs too LOW!!! guess higher")

        elif(num_guess > number):
            print("OOPs too HIGH!!! guess lower")

    print("WELL DONE!!!!! You Correctly Guessed the Number",number,"in",c,"Tries")

import random

print("YOU HAVE TO GUESS A NUMBER BETWEEN 1 and 10")
print("THE LESSER THE NUMBER OF TRIES THE MORE THE POINTS\n")

number = random.randint(1,10)

print("OK THE COMPUTER HAS RANDOMLY CHOSEN A NUMBER BETWEEN 1 and 10")
print("NOW ITS YOUR TIME TO GUESS:\n")

guess()
