theSum = 0.0
data = input("Enter a number: ")
while data != "":
    number = float(data)
    if number % 2 == 0:
        theSum += number
        print("the sum is: ", theSum)
    else:
        print("only numbers that are divisible by 2 are allowed")
        
    data = input("Enter the next number: ")
    
    


 
