# 读取学生总数 n 和俱乐部个数 m
n, m = map(int, input().split())

# 初始化并查集，每个学生的父节点初始为自己
parent = list(range(n + 1))
# 初始化每个集合的秩（树的高度）
rank = [0] * (n + 1)

# 查找 x 的根节点，路径压缩优化
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 合并 x 和 y 所在的集合，按秩合并
def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

# 处理每个俱乐部的信息
for _ in range(m):
    line = input().split()
    members = list(map(int, line[1:]))
    first_member = members[0]
    for member in members[1:]:
        union(first_member, member)

# 统计每个集合的人数
count = {}
for i in range(1, n + 1):
    root = find(i)
    count[root] = count.get(root, 0) + 1

# 找出最大朋友圈的人数
max_friends = max(count.values()) if count else 0
print(max_friends)