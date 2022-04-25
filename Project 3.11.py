"""
Project 3.11
Quentin Miller

"""
import random

#request the imput
dollars = int(input("How much money do you want to play with? "))
#initialize the variables
maxDollars = dollars
countAtMax = 0
count = 0


#Loop until the money is gone

while dollars > 0:
    count += 1
    #Roll the dise
    die1 = random.randint(1,6)# 1-6 sides of die
    die2 = random.randint(1,6)
    #calulate winings or loses

    if die1 + die2 == 7:
        dollars += 4
    else:
        dollars -= 1
        #if this is the new maximum remember it

    if dollars > maxDollars:
        maxDollars = dollars
        countAtMax = count

#Display the Results
print(" You are dead broke after " + str(count) + " rolls.\n" + \
      "you shud have quit after " + str(countAtMax) + \
      " rolls when you had $" + str(maxDollars) + ".")
