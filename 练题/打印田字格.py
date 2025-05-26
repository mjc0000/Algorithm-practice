n=int(input())
for _ in range(n):
    for _ in range(n):
        print("+ - - - -",end='')
    print("+")
    for _ in range(4):
        for _ in range(n):
            print("|        ",end='')
        print("|")
for _ in range(n):
    print("+ - - - -", end='')
print("+\n")
