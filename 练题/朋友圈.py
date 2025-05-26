from enum import member
from itertools import count

n,m =map(int,input().split())
parent=list(range(n+1))

def find(x):

    if parent[x] !=x:
        parent[x] =find(parent[x])
        return parent[x]


def union(x,y):
    root_x=find(x)
    root_y=find(y)
    if root_x != root_y:
        parent[root_y]=root_x

for _ in range(m):
    line =input().split()
    members= list(map(int,line[1:]))
    first=members[0]
    for member in members[1:]:
        union(first,member)


count ={}

for i in range(1,n+1):
    root = find(i)
    count[root]=count.get(root,0)+1

max_friends =max(count.values()) if count else 0

print(max_friends)

