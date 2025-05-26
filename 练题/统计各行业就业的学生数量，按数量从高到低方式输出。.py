

count={}
line=input().split()
for i in line:
    if i not in count:
        count[i]=1
    else:
        count[i]+=1

sorted_count=sorted(count.items(),key=lambda item: item[1], reverse=True)
for key,value in sorted_count:
    print(f"{key}:{value}")