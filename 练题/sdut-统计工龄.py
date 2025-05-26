n=int(input())
workYears={i: 0 for i in range(51) }


line=input().split()
for i in line:
    x=int(i)
    if(x>=0 and x<=50):
        workYears[x]+=1

for i in workYears:
    if(workYears[i]>0):
        print(f"{i}:{workYears[i]}")
