"""
Project 4.8
Quentin Miller

copies the text from a given input to a given file.
"""

#take the imputs

inName = input("Enter the input file name: ")
outName = input("Enter the output file name: ")

#Open the input file and read the text

inputFile = open(inName, 'r')
text = inputFile.read()

#Open the output and write the text

outFile = open(outName, 'w')
outFile.write(text)
outFile.close()
