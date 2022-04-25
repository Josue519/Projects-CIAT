"""
File: texteditor.py
Josue marante
Project 8.8

"""

from breezypythongui import EasyFrame
import tkinter.filedialog

class TextEditor(EasyFrame):
    """Demonstrates the use of a file dialog."""
    
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, "Text Editor")
        self.outputArea = self.addTextArea("", row = 0, column = 0,
                                           columnspan = 3,
                                           width = 80, height = 15)
        self.addButton(text = "New", row = 1 , column = 0,
                       command = self.newFile)
                        
        self.addButton(text = "Open", row = 1, column = 1,
                       command = self.openFile)

        self.addButton(text = "Save", row = 1, column = 2,
                       command = self.saveFile)
        

    # Event handling method.


    def newFile(self):
        """Clears the text area and the title bar."""
        self.outputArea.setText("")
        self.setTitle("Text Editor")

        
    def openFile(self):
        """Pops up an open file dialog, and if a file is
        selected, displays its text in the text area and
        its pathname in the title bar."""
        fList = [("Python files", "*.py"), ("Text files", "*.txt")]
        fileName = tkinter.filedialog.askopenfilename(parent = self,
                                                      filetypes = fList)
        if fileName != "":
            file = open(fileName, 'r')
            text = file.read()
            file.close()
            self.outputArea.setText(text)
            self.setTitle(fileName)

    def saveFile(self):
        """Pops up an open file dialog, and saves the contents
        of the test area to the selected file name."""
        fList = [("Python files", "*.py"), ("Text files", "*.txt")]
        fileName = tkinter.filedialog.asksaveasfilename(parent = self,
                                                      filetypes = fList)
        if fileName != "":
            file = open(fileName, 'w')
            file.write(self.outputArea.getText())
            file.close()
            self.setTitle(fileName)

def main():
    """Instantiate and pop up the window."""
    TextEditor().mainloop()

if __name__ == "__main__":
 main()
   
