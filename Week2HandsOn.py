"""
Project 4.1
Quentin Miller

Write a script that inputs a line of plain text and distance value and outputs
an encrypted text using Caesar cipher.
The script should work for any printable characters.
"""

#The ASCII values range from 0 through 127
plainText = input("Enter a message: ")
distance = int(input("Enter the distance value: "))
code = ""
for ch in plainText:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > 127:
        cipherValue = distance - (127 - ordValue + 1)
        code += chr(cipherValue)

print(code) 
    
