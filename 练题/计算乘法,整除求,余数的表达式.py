
verifys=True
line=input().split()
a,symbol,b=int(line[0]),line[1],int(line[2])
if(symbol=='*'):
    c=a*b
elif(symbol=='//'):
    c=a//b
elif(symbol=='%'):
    c=a%b
else:
    print("Invalid operator")
    verify= False
if(verifys==True):
    print(f"{a}{symbol}{b}={c}")


