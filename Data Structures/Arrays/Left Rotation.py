# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 11:47:28 2024

@author: wescl
linha de teste adicionada
"""

vec = [1, 2, 3, 4, 5]
a = 123

def rotateLeft(d, arr):
    aux = arr    
    size = len(arr)
    ans = [0]*size
    for execution in range(d):           
        for x in range(size):
            
            i = (x+1)%size            
            ans[x] = aux[i]
            print("Substituindo aux["+str(i)+"] = "+str(aux[i])+" em ans["+str(x)+"]")
        aux = ans            
    return ans
    
    
print (rotateLeft(3,vec))
#for x in range(len(vec)):
#    print(str((x-1)%5)+": "+str(vec[x]))

#for x in range(5):
#    print(x)
