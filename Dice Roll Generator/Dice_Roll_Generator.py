#Rolling the dice
import random
min = 1
max = 6
#the variable that stores the user’s decision
roll_again = "yes"
#The dice roll loop if the user wants to continue
while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
#Printing the randomly generated variable of the first dice
    print (random.randint(min, max))
#Printing the randomly generated variable of the second dice
    print (random.randint(min, max))
#Here the user enters yes or y to continue and any other input ends the program
    roll_again = input("Roll the dices again?")
