def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1 // num2   #//remove the decimal point

def avg(num1,num2):
    return (num1+num2)/2

def sub(num1,num2):
    return num1-num2

#user input
print("Select an operation:\n" 
      "1. Addition\n"  
      "2. Subtraction\n" 
      "3. Multiplication\n" 
      "4. Division\n" 
      "5. Average\n")

select = int(input("Select a operation from 1,2,3,4,5: "))

number1 = int(input("Enter First Number: "))
number2 = int(input("Enter second Number: "))

 #step3 print the result
 
if select == 1:
     print(f"{number1}, + , {number2}, = , {add(number1, number2)}")
     
elif select == 2:
     print(f"{number1}, + , {number2}, = , {sub(number1, number2)}") 
     
elif select == 3:
     print(f"{number1}, + , {number2}, = , {multiply(number1, number2)}") 
     
elif select == 4:
     print(f"{number1}, + , {number2}, = , {divide(number1, number2)}")
     
elif select == 5:
     
     print(f"{number1}, + , {number2}, / 2 = , {avg(number1, number2)}") 
else:
    print("invalid operation! please select again ")    
     

