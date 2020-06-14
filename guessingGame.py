'''
Amitva Pal
Period 6/7 HCP : Guessing Game
Uses loops and functions o play a guessing game with the user
'''

import random

def getRating(numTries):
    return 42

'''
Prompts user to enter a number between low and high; guarantees the number entered is valid (integer within range)
'''

def getNumBetween(message, low, high):
    num = low -1 # out of bounds so the loop will begin
    while(num<low or num>high): #continue to ask until valid number is entered
        try:
            num = int(input(message + " between " + str(low) + " and " + str(high) + ": "))
            if num<low or num > high:
                print("Error- number entered is out of range.")
        except ValueError:
            print("Invalid number entered.")
    return num
def main():
    #get max value to generate computer guess
    maxGameNum = getNumBetween("Enter Maximum game value for guessing",1, 100000 )
    numTries = 0
    low = 1
    high = maxGameNum
    mysteryNum = random.randint(1, maxGameNum)
    guess = 0
    print("Lets play a guessing game.  I am thinking of a number between 1 and " + str(maxGameNum))
    
    while(guess != mysteryNum):
        guess = getNumBetween("Enter a guess ", low, high)
        numTries += 1
        
        if (guess == mysteryNum):
            print("You won in", numTries, "tries")
        elif (guess < mysteryNum):
            print("That guess is too low ")
            low = guess + 1
        elif(guess > mysteryNum):
            print("That guess is too high")
            high = guess - 1
            
    print("\nYou earned a rating of ", getRating(numTries))
    
main()