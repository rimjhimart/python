num1= float(input("enter the first operand: "))
num2 = float(input("enter the second operand: "))
operator = input("Choose your operator(+, -, *, /): ")

if operator =="+":
    result = num1 + num2
    print(round(result,3))
elif operator =="-":
    result = num1 - num2
    print(round(result,3))
elif operator =="*":
    result = num1 * num2
    print(round(result,3))
elif operator =="/":
    result = num1 / num2
    print(round(result,3))

   
   