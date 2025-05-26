line=input().split()
scores=[]
for i in line:
    scores.append(float(i))
maxscore=float(max(scores))
minscore=float(min(scores))
ave=(sum(scores)-maxscore-minscore)/(len(scores)-2)
print(f"最高分:{maxscore:.2f}\n最低分:{minscore:.2f}\n平均分：{ave:.2f}")