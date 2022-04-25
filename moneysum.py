"""defines a function 
that adds the bill variables
 and returns the sum"""

def mysum(object1,object2,object3,object4,object5,object6):
    return object1+object2+object3+object4+object5+object6

def main():
    phone_bill = 100
    Student_Loans = 120 
    Car_pay = 350 
    City_Bank = 100
    Best_Buy = 100
    Apple_Car = 2184

    print(mysum(phone_bill,Student_Loans,Car_pay,City_Bank,Best_Buy,Apple_Car))

if __name__ == "__main__":
    main()


 