"""
Project 8.5
josue Marante
File: guessWithGUI.py
The Computer guesses a number and the user provides a hint
"""

from breezypythongui import EasyFrame
import random

class GuessingGame(EasyFrame):
    """ Plays a guessing game with the user."""

    def __init__(self):
        """Sets up the window, widgets, and data. """
        EasyFrame.__init__(self, title ="Guessing Game")
        self.lowerBound = 1
        self.upperBound = 100
        self.count = 0
        self.myNumber = (self.lowerBound + self.upperBound) // 2
        guess = "Is the number " + str(self.myNumber) + "?"
        self.myLabel = self.addLabel(text = guess, row = 0, column = 0, sticky = "NSEW", columnspan = 4)
        self.small = self.addButton(text = "Too small", row = 1, column = 0, command = self.goLarge)
        self.large = self.addButton(text = "Too Large", row = 1, column = 1, command = self.goSmall)
        self.correct = self.addButton(text = "correct!!", row = 1, column = 2 , command = self.goCorrect)
        self.newButton = self.addButton(text = "New Game", row = 1, column = 3, command = self.newGame)

    def goLarge(self):
        """Guess was too small, so move guess to the right of the number."""
        self.count += 1
        self.lowerBound = self.myNumber + 1
        self.myNumber = (self.lowerBound + self.upperBound) // 2
        guess = "Is the number " + str(self.myNumber) + "?"
        self.myLabel["text"] = guess

    def goSmall(self):
        """Guess was too Large, so move guess to the left  of the number."""
        self.count += 1
        self.lowerBound = self.myNumber - 1
        self.myNumber = (self.lowerBound + self.upperBound) // 2
        guess = "Is the number " + str(self.myNumber) + "?"
        self.myLabel["text"] = guess

    def goCorrect(self):
        """Guess was too correct, so announce and wait."""
        self.count += 1
        guess = "I've got it in " + str(self.count) + " tries!"
        self.myLabel["text"] = guess
        self.small["state"] = "disabled"
        self.large["state"] = "disabled"
        self.correct["state"] = "disabled"

    def newGame(self):
        """Resets the GUI to its original state. """
        self.lowerBound = 1
        self.upperBound = 100
        self.count = 0
        self.myNumber = (self.lowerBound + self.upperBound) // 2
        guess = "Is the number " + str(self.myNumber) + "?"
        self.myLabel["text"] = guess
        self.small["state"] = "normal"
        self.large["state"] = "normal"
        self.correct["state"] = "normal"

        
def main():
    """ Instantiate and pop up teh window."""
    GuessingGame().mainloop()

if __name__ == "__main__":
    main()
        
