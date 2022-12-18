def cube(num, euro):
    print(num*euro)#or you can use return (the same shit) and you have to type print(cube(...))
cube(350, 4.93)

is_femele= False
is_male=True
is_tall=True
if is_femele and is_tall:
    print("You are a tall woman")
elif is_male and is_tall:
    print("You are tall male")
elif is_femele and not(is_tall):
    print("You are not a tall woman")
elif is_male and not(is_tall):
    print("You are not a tall man")
else:
    print("Samething is wrong!")

def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(2,2,5))

num1=float(input("Input the first number: "))
op=input("Enter operator: ")
num2=float(input("Input the second number: "))

if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("Invalid operator")