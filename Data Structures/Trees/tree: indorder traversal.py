#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 01:30:38 2024

@author: wescley
"""

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def inOrder(node):
    #Write your code here
    if node == None:
        return
 
    # First recur on left subtree
    inOrder(node.left)
 
    # Now deal with the node
    print(node.info, end=' ')
    
    # Then recur on right subtree
    inOrder(node.right)
 
    



#tree = BinarySearchTree()
#t = int(input())
#
#arr = list(map(int, input().split()))
#
#for i in range(t):
#    tree.create(arr[i])

root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.right = Node(4)

print(root.right)

