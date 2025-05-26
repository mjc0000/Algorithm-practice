# 创建一个简单的二叉树
#       1
#      / \
#     2   3
#    / \
#   4   5

import random


class Treenode:
    def __init__(self,value=0,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right


def generate_random_binary_tree(num_of_tree):
    if num_of_tree==0:
        return None
    root=Treenode(random.randint(1,100))
    queue =[root]
    node_count=1

    while queue and node_count < num_of_tree:
        current=queue.pop(0)
        if random.random() >0.2 and node_count< num_of_tree:
            queue.append(current.left)

            node_count+=1

        if random.random() >0.2 and node_count<num_of_tree:
            current.right =Treenode(random.randint(1,100))

            queue.append(current.right)
            node_count+=1

    return root


def travel(root):

    result=[]

    if root:
        result.append(root.value)

        result.append(travel(root.left))

        result.append(travel(root.right))

    return result

root =generate_random_binary_tree(15)

print("前序遍历结果是:",travel(root))




