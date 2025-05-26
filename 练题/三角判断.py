a,b,c=map(int,input().split())

maxline=max(a,b,c)


if(a+b+c>2*maxline ):
    print('yes')
else:
    print('no')
