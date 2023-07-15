print("----------Calculator----------")
n1 = int(input("Enter your first number: "))
op = input("Enter operation you want to perform: ")
n2 = int(input("Enter your second number: "))

lst = [(45,3),(56,9),(56,6)]

print()
if (n1,n2) in lst:
    if (n1,n2)==(45,3):
        print("45*3=555")
    elif(n1,n2)==(56,9):
        print("56+9=77")
    else:
        print("56/6=4")
elif op=='+':
    print(str(n1)+'+'+str(n2)+'='+str(n1+n2))
elif op=='-':
    print(str(n1)+'-'+str(n2)+'='+str(n1-n2))
elif op=='*':
    print(str(n1)+'*'+str(n2)+'='+str(n1*n2))
elif op=='/':
    print(str(n1)+'/'+str(n2)+'='+str(n1/n2))

