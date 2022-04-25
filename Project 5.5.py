"""
Project 5.5
Quentin Miller
Defines a function repToDecimal that converts a number
in any base to decimal.
"""

#table of digits in bases 2 - 16 with integer values

repTable = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6,
            '7': 7, '8':8, '9':9 , 'A': 10, 'B': 11, 'C': 12,
            'D': 13, 'E': 14, 'F': 15 }
def repToDecimal(rep, base):
    """ Converts the string rep of a number in base
    to decimal and returns the decimal as an int"""

    decimal = 0
    exp = len(rep) - 1

    for digit in rep:
        decimal += repTable[digit] * base ** exp
        exp -= 1
        return decimal

def main():
    """Test the function"""
    print(repToDecimal(10,'10'))
    print(repToDecimal(10,'8'))
    print(repToDecimal(10,'2'))
    print(repToDecimal(10,'16'))

#the entry point for program execution
    if __name__ == "__main__":
      main()
