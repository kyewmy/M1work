# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 20:26:01 2024

@author: 86139
"""

class TreeNode:
    def __init__(self, value):
        self.value = value      
        self.firstChild = None  
        self.nextSibling = None 
        
        
# 计算节点的度
def get_degree(node):
    if not node:
        return 0  
    degree = 0
    child = node.firstChild
    while child:
        degree += 1 
        child = child.nextSibling  
    return degree

# 输出每个节点的度
def print_node_degrees(root):
    if not root:
        return
    print(f"Node {root.value} has degree: {get_degree(root)}")
    child = root.firstChild
    while child:
        print_node_degrees(child)
        child = child.nextSibling

# 测试
if __name__ == "__main__":
    # 构造根节点为1的树
    root = TreeNode(1)  
    # 根节点有两个子节点2和3
    root.firstChild = TreeNode(2)
    root.firstChild.nextSibling = TreeNode(3)
    # 节点2有一个子节点4
    root.firstChild.firstChild = TreeNode(4)
    # 节点3有一个子节点5
    root.firstChild.nextSibling.firstChild = TreeNode(5)
    # 输出
    print_node_degrees(root)
