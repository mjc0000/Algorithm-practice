n=int(input())
for _ in range(n):
    a,b,c,d=map(int,input().split())
    if(a>=55 and b>=55 and c>=90 and d>=90 and a+b+c+d>=320):
        print("Yes")

    else:
        print("No")