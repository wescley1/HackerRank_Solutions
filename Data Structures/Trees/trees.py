#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 20:40:54 2024

@author: wescley
"""
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
        
def depth_first_traversal(node):
    print(node.value)
    for child in node.children:
        depth_first_traversal(child)
        
def search(value, node):
    if node.value == value:
        return node
    for child in node.children:
        result = search(value, child)
        if result:
            return result
    return None

        
root = TreeNode("Beverages")
hot = TreeNode("Hot")
cold = TreeNode("Cold")

root.add_child(hot)
root.add_child(cold)

print(root.children[1].value)

#print("Depth-First Traversal:")
#depth_first_traversal(root)

#soda_node = search("Soda", root)
#if soda_node:
#    print(f"Found node: {soda_node.value}")