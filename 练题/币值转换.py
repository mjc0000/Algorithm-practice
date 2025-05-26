
line=input()
kind=line[-1]
amount=float(line[:-1])
if(kind=='R'):
    result=amount/6.5
    d='M'
elif(kind=='M'):
    result=amount*6.5
    d='R'
print(f"{result:.2f}{d}")
