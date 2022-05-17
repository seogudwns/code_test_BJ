# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 13:56:50 2022

@author: 형준
"""

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
"""




 # g4 5569 출근경로

'''
상근이가 사는 도시는 남북 방향으로 도로가 w개, 동서 방향으로 도로가 h개 있다. 
남북 방향 도로는 서쪽부터 순서대로 번호가 1, 2, ..., w로 매겨져 있다. 
또, 동서 방향 도로는 남쪽부터 순서대로 번호가 1, 2, ..., h로 매겨져 있다. 
서쪽에서 i번째 남북 방향 도로와 남쪽에서 j번째 동서 방향 도로가 만나는 교차로는 (i, j)이다.
상근이는 교차로 (1, 1)에 살고 있고, 교차로 (w, h)에 있는 회사에 차로 다니고 있다. 
차는 도로로만 이동할 수 있다. 상근이는 회사에 최대한 빨리 가기 위해서, 동쪽 또는 북쪽으로만 이동할 수 있다. 
또, 이 도시는 교통 사고를 줄이기 위해서 교차로를 돈 차량은 그 다음 교차로에서 다시 방향을 바꿀 수 없다. 
즉, 교차로에서 방향을 바꾼 후, 1 블록만 이동한 후 다시 방향을 바꿀 수 없다.
상근이가 회사에 출근할 수 있는 경로의 수는 몇 가지 일까?
w와 h가 주어졌을 때, 가능한 출근 경로의 개수를 구하는 프로그램을 작성하시오.
====================
input : w h  (2<=w,h<=100)

oupput : 경로의 갯수.
====================
w 와 h가 들어갈 때 실재 움직이는 도로들은 각각 w-1과 h-1.

오른우선카운트와 위우선카운트를 나눠야하나?(X)

조합론 문제... RUR 혹은 URU가 나오면 안됨.

모든 조합을 구한 후 RUR이 있는것들 pop,그 후 URU가 있는 것들을 pop?

1.. URU가 있는 것들, RUR이 있는 것들, 둘 다 있는 것들 카운트 후 +-카운트.
C(n+k-2,n-1) - (URU조합) - (RUR조합) + (둘 다 있는 조합....hard) = ?


2..  n,k중 하나가 1인 경우 return 1,
나머지 경우, 둘 중 하나가 2인 경우 return 2,
나머지 경우, 둘 중 하나가 3인 경우 return 나머지수+1 
아닌 경우, ....

RU --> U
UR --> R
UU --> R,U
RR --> R,U


P(n,k) 

'''

'''
# 남북 w 동서도로 h개
# 남북방향 도로는 왼쪽부터 1,2,...w개 동서도로는 아래부터 1,2,.,..h개
# 서쪽 i번째에서 남북 남쪽j번째도로가 만나는 교차로는 i,j이다.
#  (1,1) (w,h) 가는방법. 방향전환은 최소2칸이상.
# 상태값(x과표, y좌표, x방향전환가능, y방향전환 가능)
w,h = map(int,input().split())
dp = [[[[0 for _ in range(2)] for _ in range(2)] for _ in range(101)] for _ in range(101)]

# 앞의 0,1은 방향전환이 가능하냐, 불가능하냐? 뒤의 0,1은 북쪽 방향,동쪽 방향 어딜 일직선으로 통과하냐?
for i in range(2,h+1):
    dp[i][1][0][0] = 1
for i in range(2,w+1):
    dp[1][i][0][1] = 1

for i in range(2,h+1):
    for j in range(2,w+1):
        # 방향전환이 가능하고 북쪽 방향을 보는 애들은 남쪽에서 쭉 온 애들이랑 남족에서 왔는데 방향전환 불가능하던 애들.
        dp[i][j][0][0] = (dp[i-1][j][0][0] + dp[i-1][j][1][0])%100000
        # 방향전환 가능하고 동쪽 보는애드은 동쪽에서 쭉왔거나 동쪽에서 왔는데 방향전환 불가능해서 쭉온애들
        dp[i][j][0][1] = (dp[i][j-1][0][1] + dp[i][j-1][1][1])%100000
        # 방향전환 불가능한데 북쪽보는 애들은 남쪽에서 올라온 애들중에 동쪽 보고 있던 애들
        dp[i][j][1][0] = (dp[i-1][j][0][1])%100000
        # 방향전환 불가능한데 동쪽보는 애들은 동쪽에서 왔는데 원래 북쪽 보던애들.
        dp[i][j][1][1] = (dp[i][j-1][0][0])%100000
        print (dp[i][j][0][0],dp[i][j][1][0],dp[i][j][0][1],dp[i][j][1][1])
print(dp[h][w])
print((dp[h][w][0][0] + dp[h][w][1][0] + dp[h][w][0][1] + dp[h][w][1][1])%100000)
'''


###### 이게 무슨 문제였지??.....
"""  
def newsort(lis):
    sorted3 = [lis[0]]
    for i in range(1,len(lis)):
        if sorted3[-1][1]==lis[i][1]:
            sorted3.append(lis[i])  #경로의 마지막의 y축의 값이 다음과 같을 때 경로에 추가. [00,10,20]
        else:
            
            
            
            
    return sorted3


case = int(input())
for i in range(case):
    n = int(input())

    cafesite=[]

    for i in range(n):
        cafesite.append(list(map(int,input().strip().split())))

    sortedcafe=sorted(cafesite) #print(sortedcafe)  #x축 정렬 완..... 한큐에 솔트할 방법 필요.?
    #y축 정렬은 어떻게?
    sorted2={}
    for i in sortedcafe:
        if i[0] not in sorted2.keys():
            sorted2[str(i[0])]=[i]
        else:
            sorted2[str(i[0])].append(i)

    #x축에 따라 묶음.
    
    
    m = list(map(int,input().strip().split()))

    for i in range(1,m[0]+1):
        print('{} {}'.format(sortedcafe[m[i]][0],sortedcafe[m[i]][1]))
        #sorted2 리스트를 만들어서 print 해버리자.

"""


""" # p3 17100 Candy Boxes
'''
사탕 가게에서 특가 상품을 판매한다고 한다. 
특가 상품은 한 상자 안에 여러개의 라이언 모양 사탕이 들어 있는 형태이다. 
총 N개의 특가 상품이 존재하는데, i번째 특가 상품에는 당도 ai의 사탕 mi개가 들어있으며, 가격은 ci이다.

종영이는 당이 떨어져 여러 특가 상품을 구매해 이를 해결하려고 한다. 
1부터 L까지의 모든 k에 대해서, 당도의 합이 k가 되게 사탕을 먹을 수 있게 구매하는 최소의 비용을 구하여라. 
한 특가 상품을 구매하면, 그 특가 상품 내의 사탕을 모두 먹을 필요는 없다.
===========================================
N L
(N개줄)
a b c
===========================================



...
'''

def maker(pickboxes,d):
    cando = [0]
    for i,j,k in pickboxes:
        for x in range(j+1):
            
    
    
n, k = map(int,input().strip().split())

box=[]

for i in range(n):
    a,b,c = map(int,input().strip().split())
    box.append([a,b,c])   #차례대로 당도,갯수,box가격
"""

""" # s3 2606 바이러스
import sys

tree = [1]

def BFS(tree,edges):
    for i in tree:
        for j in edges:
            if (i == j[0]) and (j[1] not in tree):
                tree.append(j[1])
                edges.remove(j)
                BFS(tree,edges)
            elif (i == j[1]) and (j[0] not in tree):
                tree.append(j[0])
                edges.remove(j)

a=int(sys.stdin.readline())
nbr_of_edges=int(sys.stdin.readline())
edges=[]
for i in range(nbr_of_edges):
    edges.append(list(map(int,sys.stdin.readline().strip().split())))

BFS(tree,edges)

print(len(tree)-1)
"""

""" # s2 1012 유기농 배추

#func.

case = int(input())
for i in range(case):
    vtx = []
    edges=[]
    tree = []
    component = []
    
    a,b,nbr = map(int,input().strip().split())
    
    for j in range(nbr): #vtx = [[0,0],[1,2], ~~~~ ]
        vtx.append(list(map(int,input().strip().split())))
    
    for j in vtx: #edge 정의하기
        if [i[0]+1,i[1]] in vtx:
            edges.append([i,[i[0]+1,i[1]]]) 
        if [i[0],i[1]+1] in vtx:
            edges.append([i,[i[0],i[1]+1]])  
    #두 개의 점이 연결되어있다.. 바둑판 위의 점이기 때문에 이런식으로 오더를 주는게 가능.
    
    while len(edges) != 0:
         
"""     ##########################################################
    
"""
import sys

computer = int(sys.stdin.readline().strip())
pair = int(sys.stdin.readline().strip())
graph = []

for _ in range(pair): # 연결된 컴퓨터 쌍 정보
  graph.append(list(map(int, sys.stdin.readline().split())))

graph.sort(key = lambda x : (x[0], x[1]))
visited = [False] * (computer + 1) # 방문 확인 리스트
# print(graph)
def bfs(graph, start, visited):
  link_info = [] # 연결된 그래프 정보
  link_index = {} # 각 숫자가 들어간 그래프의 인덱스

  for i, j in graph: # [1, 2] [2, 3] ... [4, 7]
    if not visited[i] and not visited[j]: # 둘 다 방문하지 않은 상태이면
      visited[i] = True
      visited[j] = True
      link_info.append([i, j]) # 새로운 리스트로 추가
      link_index[i] = len(link_info) - 1
      link_index[j] = len(link_info) - 1
    elif visited[i] and not visited[j]: # i만 방문했으면
      visited[j] = True
      link_info[link_index[i]].append(j) # i가 들어있는 리스트에 추가
      link_index[j] = link_index[i] # 인덱스는 i랑 같음
    elif visited[j] and not visited[i]: # j만 방문했으면
      visited[i] = True
      link_info[link_index[j]].append(i) # j가 들어있는 리스트에 추가
      link_index[i] = link_index[j] # 인덱스는 j랑 같음
    else: # 둘 다 방문했으면
      continue

  # print(link_index)
  return len(link_info[link_index[start]]) - 1 # 바이러스가 시작된 컴퓨터가 속한 리스트의 길이에서 본인 빼기

print(bfs(graph, 1, visited))
"""


 # s4 4881 자리수의 제곱.
'''
문제를 나눌 필요성이 보임.
1. 각 자릿수의 제곱을 리스트에 넣기.
2. 각 리스트에서 만나는 숫자의 최소를 넣기..(ex 참조.)
3. 이때 각 숫자의 처음을 만나거나 중간에 만나는 경우?...
3-1. 한 숫자의 리스트가 다른 알파를 만났을 때.(두 숫자가 같은 경우도 이에 해당됨.)
3-2. 서로 사이클에 다가가지 않고 베타끼리 만났을 때.  .... 요게 문제인데..
3-3. 서로 사이클에 도착하고 탐색했을 때 만났을 때
3-4. 서로 사이클에 도착했지만 사이클이 달랐을 때. ==> print(0), then pass

'''
######################################
'''
ex. 11 26을 넣었을 때... [11, 2, 4, 16], [26, 40, 16] --> 7.. 이경우 11,2,4 ~~ 4,16  ~~ 26,40,16 에 4,16에서는 -1. 
'''

'''  3-3 해결..
#endcycle 정의. 각각의 숫자 리스트가 서로 다른 사이클에 있는 숫자를 포함하고 있을 경우 print(-1)하고 pass.
cycle1 = [4,16,37,58,89,145,42,20]
cycle2 = [1]
print('a',cycle1.index(20))  #16,4,20 case를 생각해보자.. 반시계일때는 6, 시계일때는 2..
print('aa',cycle1.index(16)) 
alist = [11,2,4]
blist = [26,40,16]

cycle_dist = abs(cycle1.index(alist[-1])-cycle1.index(blist[-1]))
min( cycle_dist , 8 - cycle_dist ) 
#done.. cycle1에서 만났을 때 체크 성공.. 0~4까지 잘 리턴됨.
print('cycle_dist = ' , min( cycle_dist , 8 - cycle_dist ))  
absum = 0

absum += len(alist) + len(blist) + min( cycle_dist , 8 - cycle_dist )
print('bb',absum)
'''

 #잠깐 보류..
#endcycle 정의. 각각의 숫자 리스트가 서로 다른 사이클에 있는 숫자를 포함하고 있을 경우 print(0)하고 pass.
cycle1 = [4,16,37,58,89,145,42,20]
cycle2 = [1]

while True:
    a,b = map(int,input().strip().split())
    if (a==0) and (b==0):
        break
    
    alist = [a]
    blist = [b]
    while True: #alist 만들기.
        if (alist[-1] in cycle1) or (alist[-1] in cycle2):
            break
        
        square_sum = 0
        div_nbr = [int(i) for i in str(alist[-1])]
        for i in div_nbr:
            square_sum += i**2
        alist.append(square_sum)
        
        
    while True: #blist 만들기.
        if (blist[-1] in cycle1) or (blist[-1] in cycle2):
            break
        
        square_sum = 0
        div_nbr = [int(i) for i in str(blist[-1])]
        for i in div_nbr:
            square_sum += i**2
        blist.append(square_sum)  
    
    #list 변환과정.. done.
    
    # 프린트하는 과정! 첫번째, 세번째 clear..
    if (alist[0] in blist) or (blist[0] in alist):
        print(a,b,abs(len(blist) - len(alist))+2)  #시작하는 수가 다른 리스트에 그대로 들어가있는 경우.  done.
        
    elif (alist[-1]==1) and (blist[-1]==1):  #종착지가 둘 다 cycle2에 있는 경우.
        if len(set(alist)&set(blist))==1:  #1이 유일하게 겹치는 케이스. done.
            print(a,b,len(alist)+len(blist))   
        else: 
            while alist[-1] == blist[-1]:
                alist.remove(alist[-1])
                blist.remove(blist[-1])
            print(a,b,len(alist)+len(blist)+2)  #done.
            
    elif (alist[-1] in cycle1) and (blist[-1] in cycle1):   #종착지가 둘 다 cycle1에 있는 경우
        if alist[-1] != blist[-1]:  
            cycle_dist = abs(cycle1.index(alist[-1])-cycle1.index(blist[-1]))  
            #cycle1에서 a->b 방향 거리.(시계반시계 x)
            print(a,b,len(alist) + len(blist) + min( cycle_dist , 8 - cycle_dist )) 
            #cycle1으로 도착하는 종착지가 다름. done.
        else: 
            while alist[-1] == blist[-1]:
                alist.remove(alist[-1])
                blist.remove(blist[-1])
            print(a,b,len(alist)+len(blist)+2)  #위의 (*)와 같은 케이스. done.
            
    else:
        print(a,b,0) #만나지 않기 때문에 0을 리턴.
