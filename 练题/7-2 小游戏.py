n=int(input())
for _ in range(n):
    line=input().split()
    x=int(line[1])
    count=0
    for i in line:
        count+=int(i)
    count=count-x
    if(count%5 ==0 and count%7==0 and count%3==0):
        print("yes")
    else:
        print("no")

