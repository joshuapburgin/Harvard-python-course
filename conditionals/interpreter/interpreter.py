expression= input("Enter expresssion\n").replace(" ","")

operators = ['+', '-', '*', '/']
position=0

# Find the first occurrence of any operator in the expression
match expression[1]:
    case '+'| '-'| '*'| '/':
        position=1
    case _:
        position=2


x=float(expression[0:position])
y=expression[position]
z=float(expression[position+1:])

if y=="+":
    print(x+z)
elif y=="-":
    print(x-z)
elif y=="*":
    print(x*z)
elif y=="/":
    print(x/z)
else:
    print("enter a valid operation")


