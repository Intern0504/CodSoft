def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        print("Not Defined")
    return x/y
def power(x,y):
    return x**y
print("CALCULATOR")
while True:
    print('''INSTRUCTIONS to use this calculator:
      Press 1 for addition(+)
      Press 2 for subtraction(-)
      Press 3 for multiplication(*)
      Press 4 for division(/)
      Press 5 to find power of a number(**)''')
    option=int(input("Enter your choice to perform desired operation (1/2/3/4/5) : "))
    if option>=6:
        print("invalid choice , please read the instructions")
        continue
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    if option==1:
        print("Result: ",add(a,b))
    elif option==2:
        print("Result: ",subtract(a,b))
    elif option==3:
        print("Result: ",multiply(a,b))
    elif option==4:
        print("Result: ",divide(a,b))
    elif option==5:
        print("Result: ",power(a,b))
    start=input("Do you want to use the calculator again? (yes/no)").lower()
    if start!="yes":
        print("Thanks for using our calculator,Byeeee :)")
        break


