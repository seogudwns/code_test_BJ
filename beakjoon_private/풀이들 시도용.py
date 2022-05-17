# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 22:27:27 2022

@author: 형준
"""




''' # 22222 이상의 이상과 같은 문제.   -  중심극한정리를 이용하는걸까?
import random
import math
c=0
for i in range(1000000):
    a=[random.random(),random.random()]
    b=[random.random(),random.random()]
    
    c+=math.sqrt(pow(a[0]-b[0],2)+pow(a[1]-b[1],2))

print(round(c/1000000,10))
'''


''' # p4 1168 요세푸스 순열2

a,b = map(int,input().strip().split())
d={str(i):0 for i in range(1,a+1)}  #숫자select할 곳.
e=[] #append 할 곳.

#N이 K보다 많이 남은 경우와 적게 남은 경우를 구분해서 코딩해야 함(2번째의 경우 나머지를 잘 이용해보자.)

while not all(d.values()):
    for i in d.keys():
        print('i : ',i)
        print('0갯수 : ',list(d.values()).count(0))
        d[i]=1



#e=['3','6','2','7','5','1','4']
#print('<'+', '.join(e)+'>') .....print is done
'''

''' # b2 13552 구와 쿼리 .... 숫자가 크다고 넓다. 다른 방법을 생각해볼 것!
a = int(input())
b = []
for i in range(a):
    c = list(map(int,input().strip().split()))
    b.append(c)

d = int(input())
e = 0
for i in range(d):
    f = list(map(int,input().strip().split()))
    for j in b:
        if pow(f[3],2)>= pow(j[0]-f[0],2) + pow(j[1]-f[1],2) + pow(j[2]-f[2],2):
            e+=1
    print(e)
    e=0
'''    


"""
'''
 # g4 19542 전단지 돌리기

import sys
a,b,c = map(int,sys.stdin.readline().strip().split())

wanted
1. tree 구현, b의 값에 따라 root 지정하기.
2. c의 크기에 따라 leaf들 제거.
3. 최소 이동거리를 구하는 알고리즘을 사용, 횟수 구하기.
'''

'''
a,root,c = map(int,input().strip().split()) # a: vertex 의 갯수, b: root번호, c: leaf 제거 횟수.

tree = {str(root):[]}

for i in range(a-1):
    a,b= map(int,input().strip().split())
    if not str(a) in tree.keys():
        tree[str(a)]=[b]
    else:
        tree[str(a)].append(b)
    if not str(b) in tree.keys():
        tree[str(b)]=[a]
    else:
        tree[str(b)].append(a)
#dictionary를 이용한 (undirected) tree 만들기 완.

def deleteleaf(tree,root):
    leafnum=[]
    for i in tree.keys():
        if len(tree[i])==1:
            leafnum.append(i)  #제거를 위한 leaf 추가
    if str(root) in leafnum:
        leafnum.remove(str(root)) #root가 list에 있을 시 제거를 위한 코드.
    for i in leafnum:
        par = tree[i][0]
        tree[str(par)].remove(int(i))
        del tree[i]
# 힘의 크기만큼 leaf 제거 def 완.
for i in range(c):
    deleteleaf(tree,root)
#  힘의 크기만큼 leaf 제거하기.


cnt=0
for i in tree.values():
    cnt+=len(i)
#sum1

print(cnt)    #35%에서 시간초과..... 방법은 맞음! 더 효율적인 방법이 없을까?
'''

'''  ######################################################################################################################################
a,root,c = map(int,input().strip().split()) # a: vertex 의 갯수, root: root번호, c: leaf 제거 횟수.

tree = {str(i):set([]) for i in range(1,a+1)}

for i in range(a-1):
    d,e= map(int,input().strip().split())
    tree[str(d)].add(e)
    tree[str(e)].add(d)
#dictionary를 이용한 (undirected) tree 만들기 완.

def deleteleaf(tree,root): #한큐에 제거하려 했으나 RuntimeError: dictionary changed size during iteration..
    leafnum=set([])
    for i in tree.keys():
        if len(tree[i])==1:
            leafnum.add(i)  #제거를 위한 leaf 추가.... 시간 효율성을 위해 list를 set으로 바꿈...미미?
    if str(root) in leafnum:
        leafnum.remove(str(root)) #root가 leaf에 있을 시 제거를 위한 코드.
    for i in leafnum:
        tree[str(tree[i].pop())].discard(int(i))
# 힘의 크기만큼 leaf 제거 def 완.
for i in range(c):
    deleteleaf(tree,root)
#  힘의 크기만큼 leaf 제거하기

cnt=sum(len(i) for i in tree.values()) #sum2
print(cnt)    #37%.... 시간 초과.... 더 효율적인 방법이 필요...
'''

'''
a,root,c = map(int,input().strip().split()) # a: vertex 의 갯수, root: root번호, c: leaf 제거 횟수.

tree = {str(i):set([]) for i in range(1,a+1)}

for i in range(a-1):
    d,e= map(int,input().strip().split())
    tree[str(d)].add(e)
    tree[str(e)].add(d)
#dictionary를 이용한 (undirected) tree 만들기 완.

def deleteleaf(tree,root): #한큐에 제거하려 했으나 RuntimeError: dictionary changed size during iteration..
    for i in tree.keys():
        if len(tree[i])==1 and int(i)!=root:
            tree[str(tree[i].pop())].discard(int(i))
# 힘의 크기만큼 leaf 제거 def 완.
for i in range(c):
    deleteleaf(tree,root)
#  힘의 크기만큼 leaf 제거하기.

cnt=sum(len(i) for i in tree.values()) #sum2
print(cnt)    #9%.... 시간 초과????
'''

'''
a,root,c = map(int,input().strip().split()) # a: vertex 의 갯수, b: root번호, c: leaf 제거 횟수.

edges=[]    #root를 제외하고 vertex를 한개만 가지는 edge를 계속 빼는 식으로?
for i in range(a-1):
    edges.append(list(map(int,input().strip().split())))  

print(edges)
'''

'''
import sys

a,root,c = map(int,sys.stdin.readline().strip().split())

tree = {str(i):set() for i in range(1,a+1)}

for i in range(a-1):
    d,e= map(int,sys.stdin.readline().strip().split())
    tree[str(d)].add(e)
    tree[str(e)].add(d)

for j in range(c):
    for i in tree.keys():
        if len(tree[i])==1 and int(i)!=root:
            tree[str(tree[i].pop())].discard(int(i))

cnt=sum(len(i) for i in tree.values())
print(cnt)    #틀림?
"""

a,root,c = map(int,input().strip().split()) # a: vertex 의 갯수, root: root번호, c: leaf 제거 횟수.

tree = {str(i):set([]) for i in range(1,a+1)}

for i in range(a-1):
    d,e= map(int,input().strip().split())
    tree[str(d)].add(e)
    tree[str(e)].add(d)
#dictionary를 이용한 (undirected) tree 만들기 완.

def deleteleaf(tree,root): #한큐에 제거하려 했으나 RuntimeError: dictionary changed size during iteration..
    leafnum=set([])
    for i in tree.keys():
        if len(tree[i])==1:
            leafnum.add(i)  #제거를 위한 leaf 추가.... 시간 효율성을 위해 list를 set으로 바꿈...미미?
    if str(root) in leafnum:
        leafnum.remove(str(root)) #root가 leaf에 있을 시 제거를 위한 코드.
    for i in leafnum:
        tree[str(tree[i].pop())].discard(int(i))
# 힘의 크기만큼 leaf 제거 def 완.

for i in range(c):
    deleteleaf(tree,root)
    if len(tree[str(root)])==0:
        break
#  힘의 크기만큼 leaf 제거하기, 이 때 edge가 없어지는 경우 break.

cnt=sum(len(i) for i in tree.values()) #sum2
print(cnt)    #41%.... 시간 초과.... 더 효율적인 방법이 필요...

  #pypy3 통과..
  
  #다른 python 사용자의 통과토드
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur, pre):
    global dist
    nodedist = 0
    
    for _next in graph[cur]:
        if _next != pre:
            nodedist= max(nodedist, dfs(_next, cur))
    if nodedist >= d :
        dist += 1
    return nodedist+1

n, s, d = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dist = 0
dfs(s,0)

print(2*(dist-1) if dist else 0)
