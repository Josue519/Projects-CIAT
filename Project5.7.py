"""
project 5.7

prints the unique words in a text file in alphabetical order

"""

#Take the input file

inName = input("Enter the input file name: ")


#open the input file Initialize the list of unique words 

inputFile = open(inName, 'r')
uniqueWords = []

#Add the unique words in a file to a list

for line in inputFile:
    words = line.split()
    for word in words:
        if not word in uniqueWords:
            uniqueWords.append(word)
uniqueWords.sort()

#Print the unique words

for word in uniqueWords:
    print(word)
