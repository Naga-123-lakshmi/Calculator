choice=0
while choice<5:
    print("1.Add \n2.Sub \n3.Mul \n4.Div(1/2/3/4)")
    choice=int(input("Enter Your choice:"))
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    if choice==1:
        c=a+b
        print("Addition is:",c)
        break;
    elif choice==2:
        c=a-b
        print("Subtraction is:",c)
        break;
    elif choice==3:
        c=a*b
        print("Multiplication is:",c)
        break;
    elif choice==4:
        c=a//b
        print("Division is:",c)
    elif choice==5:
        break;
    else:
        print("Invalid choice")
            
