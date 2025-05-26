dic={'01': '播音主持艺术学院', '02': '新闻与传播学院', '03': '电视艺术学院', '04': '动画与数字艺术学院', '05': '国际文化传播学院', '06': '华策电影学院', '07': '媒体工程学院', '08': '设计艺术学院', '09': '文化创意与管理学院', '10': '文学院', '11': '音乐学院'}
n=input().split()
name=n[0]
ID=n[1]
grade=int(ID[0:2])+2000
college=ID[2:4]
major=ID[4]
Class=ID[5]
DtuNmb=ID[6:8]
real_college=dic[college]
print(f"{name}是{grade}级{real_college}{major}号专业{Class}班第{DtuNmb}号学生")


#案列：
#王雪梅 20071203