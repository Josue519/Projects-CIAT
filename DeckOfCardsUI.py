from tkinter import *
#Imports tkinter 

class DeckOfCardsGUI:
    def __init__(self):
        window  = Tk() #Creates a window
        window.title("Pick a Card Randomly")

        self.imageList = [] #Store images for cards 
        for i in range(1,53):
            self.imageList.append(PhotoImage(file = "image/DECK"
                     + str(i) + ".gif"))

        frame = frame(window) #Hold four labels for cards 
        frame.pack()

        self.labelList = [] # A list of the labels
        for i in range(4):
            self.labelList.append(Label(frame, 
                image = self.imageList[i]))
            self.labelList.pack(side = LEFT)

            Button(window, text = "Shuffle",
                command = self.shuffle).pack()

            window.mainloop() #Create an event loop 

        # Choose four random cards
        def shuffle(self):
            random.shuffle(self.imageList)
            for i in range(4):
                self.labelList[i]["image"] = self.imageList[i]

def main():
    """Instatiates and pops up a Deck of cards that can be shuffled"""
    DeckOfCardsGUI()


if __name__ == "__main__":
    main()