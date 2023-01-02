ans = True
while(ans):
    num1= int(input("Enter first num\n"))
    num2= int(input("enter second num\n"))
    op=input("choose operetor +,_,x ,^,/\n")
    if op=='+':
        if num1==56 and num2==9:
            print('77')
        else:
            print(num1+num2)

    elif op=='-':
     print(num1+num2)
    elif op=='x':
       if num1==45 and num2==3:
        print("555")
       else:
        print(num1*num2)
    elif op=='/':
     print(num1/num2)