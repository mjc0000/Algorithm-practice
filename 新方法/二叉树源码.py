import random


# 定义二叉树节点类
class TreeNode:
    # 类的构造函数，用于初始化节点的属性
    def __init__(self, value=0, left=None, right=None):
        # 节点存储的值，默认为 0
        self.value = value
        # 指向左子节点的引用，默认为 None
        self.left = left
        # 指向右子节点的引用，默认为 None
        self.right = right


# 生成随机二叉树的函数，接收一个整数参数 num_nodes 表示要生成的节点数量
def generate_random_binary_tree(num_nodes):
    # 如果要生成的节点数量为 0，直接返回 None，表示空树
    if num_nodes == 0:
        return None
    # 生成根节点，节点的值为 1 到 100 之间的随机整数
    root = TreeNode(random.randint(1, 100))
    # 初始化一个队列，用于按层构建二叉树，初始时队列中只有根节点
    queue = [root]
    # 记录已经生成的节点数量，初始为 1（根节点）
    node_count = 1
    # 当队列不为空且已生成的节点数量小于要生成的节点数量时，继续循环
    while queue and node_count < num_nodes:
        # 从队列头部取出一个节点进行处理
        current = queue.pop(0)
        # 以 0.8 的概率（通过 random.random() > 0.2 实现）生成左子节点
        # 并且要保证生成后节点数量不超过指定数量
        if random.random() > 0.2 and node_count < num_nodes:
            # 生成左子节点，节点的值为 1 到 100 之间的随机整数
            current.left = TreeNode(random.randint(1, 100))
            # 将左子节点加入队列，以便后续处理它的子节点
            queue.append(current.left)
            # 已生成的节点数量加 1
            node_count += 1
        # 以 0.8 的概率（通过 random.random() > 0.2 实现）生成右子节点
        # 并且要保证生成后节点数量不超过指定数量
        if random.random() > 0.2 and node_count < num_nodes:
            # 生成右子节点，节点的值为 1 到 100 之间的随机整数
            current.right = TreeNode(random.randint(1, 100))
            # 将右子节点加入队列，以便后续处理它的子节点
            queue.append(current.right)
            # 已生成的节点数量加 1
            node_count += 1
    # 返回生成好的二叉树的根节点
    return root


# 对二叉树进行前序遍历的函数，接收根节点作为参数
def preorder_traversal(root):
    # 用于存储遍历结果的列表
    result = []
    # 如果根节点不为空
    if root:
        # 先将根节点的值添加到结果列表中
        result.append(root.value)
        # 递归遍历左子树，并将结果添加到结果列表中
        result.extend(preorder_traversal(root.left))
        # 递归遍历右子树，并将结果添加到结果列表中
        result.extend(preorder_traversal(root.right))
    # 返回前序遍历的结果列表
    return result


# 生成一个包含 15 个节点的随机二叉树
root = generate_random_binary_tree(15)
# 对生成的二叉树进行前序遍历，并打印遍历结果
print("前序遍历结果:", preorder_traversal(root))
