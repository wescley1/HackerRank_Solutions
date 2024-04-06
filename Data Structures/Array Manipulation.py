#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 18:08:56 2024

@author: wescley
"""

n = 10
queries = [[1, 5, 3],[4, 8, 7],[6, 9, 1]]
queries = [[2, 6, 8],[3, 5, 7],[1,8, 1],[5, 9, 15]]

def arrayManipulationOptimized(n,queries):
    ans = [0] * n
    for query in queries:
        start, end, value = query
        ans[start - 1] += value
        if end < n:
            ans[end] -= value

    max_value = 0
    current_value = 0
    for value in ans:
        current_value += value
        max_value = max(max_value, current_value)

    return max_value

def arrayManipulation(n, queries):
    ans = [0]*n
    for ctrl in range(len(queries)):
        print(f"After {ctrl} interation: {ans}")
        for i in range(queries[ctrl][0]-1,queries[ctrl][1]):
            ans[i] = ans[i] + queries[ctrl][2]
    
    print(f"After {ctrl} interation: {ans}")
    return max(ans)
    
    
    
print(arrayManipulation(n,queries))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

