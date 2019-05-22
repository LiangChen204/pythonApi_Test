#!//usr/local/bin python
# -*- coding:utf-8 -*-

"""
Created on 2019/5/7 14:51
@author: liangchen
@File: 遍历二叉树
"""
from api_demo.other.createTree import Node


def preTraverse(root):
    """
    前序遍历
    (按根节点、左子树、右子树的顺序遍历)
    """
    if root == None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)


def midTraverse(root):
    """
    中序遍历
    (按左子树、根节点、右子树的顺序遍历)
    """
    if root == None:
        return
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)


def afterTraverse(root):
    """
    后序遍历
    (按左子树、右子树、根节点的顺序遍历)
    """
    if root == None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print(root.value)


if __name__ == '__main__':
    root = Node('D', Node('B', Node('A'), Node('C')), Node('E', right=Node('G', Node('F'))))
    print('前序遍历：')
    preTraverse(root)
    print('\n')
    print('中序遍历：')
    midTraverse(root)
    print('\n')
    print('后序遍历：')
    afterTraverse(root)
    print('\n')