"""
File: labeldemo.py
"""
from breezypythongui import EasyFrame

class LabelDemo(EasyFrame):
    """Displays a greeting in a window."""

    def __init__(self):
        """Sets up the window and label."""
        EasyFrame.__init__(self, title="Label Demo", width=300, height=200)
        self.addLabel(text="Hello World",row=0,column=0)

def main():
    """Instantiates and pops up the window."""
    LabelDemo().mainloop()
if __name__ == "__main__":
    main()
