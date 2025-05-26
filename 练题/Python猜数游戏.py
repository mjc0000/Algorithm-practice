import random
random.seed(1)
secret=random.randint(0,100)
max_step=8
step=0
while(step<max_step):
    guess=int(input())
    if(guess==secret):
        print("You Win!")
        break
    elif(guess>secret):
        print("Too Big")
    else:
        print("Too Small")
if(step==max_step):
    print("Game Over!")

