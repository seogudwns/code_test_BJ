# -*- coding: utf-8 -*-

""" #코테 연습..ㅇㅅㅇ....
#직사각형의 세 점이 마우렇게나 주어져있을 때 구하는 방법.
'''
1. 주어지지 않은 점의 대각선 점이 무엇인지 찾음.
--> 벡터를 이용해서 찾으면 됨.

2.노드에서 두 점으로 향하는 두 벡터를 구함.(간단히 종점-원점)
(요구조건만 아니라면 굳이 귀찮게 메모리는 아끼지 말자..ㅇㅅㅇ)

3. 노드에 두 벡터를 더해줌.
'''
def solution(v):
    a,b,c = v 
    ab=[b[0]-a[0],b[1]-a[1]]
    ac=[c[0]-a[0],c[1]-a[1]]
    bc=[c[0]-b[0],c[1]-b[1]]  #벡터를 이용해서 답을 구할 예정.
    
    if ab[0]*ac[0]+ab[1]*ac[1]==0:  #node=a
        ab=[b[0]-a[0],b[1]-a[1]]
        ac=[c[0]-a[0],c[1]-a[1]]
        answer = [a[0]+ab[0]+ac[0],a[1]+ab[1]+ac[1]]
    elif ac[0]*bc[0]+ac[1]*bc[1]==0:  #node=c
        ca=[a[0]-c[0],a[1]-c[1]]
        cb=[b[0]-c[0],b[1]-c[1]]
        answer = [c[0]+ca[0]+cb[0],c[1]+ca[1]+cb[1]]
    else:  #node=b
        ba=[a[0]-b[0],a[1]-b[1]]
        bc=[c[0]-b[0],c[1]-b[1]]
        answer = [b[0]+ba[0]+bc[0],b[1]+ba[1]+bc[1]]
    
    return answer
"""

"""  #프로그래머스 bfs/dfs 네크워크   --   뭐가 틀렸는지 모르겠다..,,,,ㅠㅠ
'''
BFS(x)/DFS try!

'''

'''
def uppertriangular(computers):
    for i in range(n):
        for j in range(i):
            computers[i][j]=0   #상체삼각형만 남김, 즉 하체는 싸그리 0으로 만듦
    return computers
'''

'''   
def DFS(v,com,treenode):
    if v not in treenode:
        treenode.append(v)
    for vertex,conn in enumerate(com[v]):
        if vertex not in treenode and conn==1:
#            print('treenode add v: ',vertex)
            treenode.append(vertex)
            DFS(vertex,com,treenode)

def solution(n,computers):
    answer=0
    commp=[]
    treenode=[]
    for v in range(n):
#        print('v : ',v)
        if v not in sum(commp,[]):
#            print('add v')
            DFS(v,computers,treenode)
            commp.append(treenode)
#            print('commp add treenode:',treenode)
            treenode=[]
            answer+=1
#    print(commp)
    return answer

n=3
computers5 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]] #3
computers3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]] #1
computers2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]] #1
computers1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]] #2

n=4
computers4 = [[1,0,1,0],[0,1,0,1],[1,0,1,1],[0,1,1,1]] #1
computers6 = [[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,0,1]] #2


#print(solution(4,computers6))

solution(4, [[1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]])  #김채졍님 체크!!
'''
"""

"""  # 프로그래머스 bfs/dfs  여행경로
'''
digraph 문제.

여러 경로가 존재할 수 있고, 
도시별 이름의 사전순으로 우선순위가 존재, 
출력시 이를 고려해야함.

minimal directed-cycle을 생각해봐야하나..?...(아마 x?)

'''

def cycle_check_pick(last,tickets):  #어떻게 찾으면 좋을까?
    fcycles=[last]
    while True:
        
        nextone=[]
        for i in tickets:
            if i[0]==fcycles[-1]:
                nextone.append(i)
        nextaim = sorted(nextone)
        
        if len(nextaim)==0:
            break
        
        fcycles.append(nextaim[0][1])
        tickets.remove(nextaim[0])

    return fcycles    

def solution(tickets):
    answer = []
    answer.append("ICN")    #시작지 추가
    
    while len(tickets)!=0:
        
        nextone=[]
        for i in tickets:
            if i[0]==answer[-1]:
                nextone.append(i) #갈 수 있는 목적지 추가
        nextaim = sorted(nextone) 
#글자순서상으로 앞선 것을 선택.. nextone에 있는 모든 원소의 첫번째 원소가 같으므로 sort는 두 번째 원소로 진행됨
        if len(nextaim)==0:
            break
        answer.append(nextaim[0][1])
        tickets.remove(nextaim[0])
    
    print('1 : ',answer)
    print('2 : ',tickets)
    if len(tickets)!=0:
        while len(tickets)!=0:
            for i in range(len(answer)):                
                sumcitys = sum(tickets,[])  #한칸 밑으로 빼면 좋겠지만 케이스마다 체크해야하므로 메모리가 더 들더라도 안쪽으로 넣음.
                if answer[-i-1] in sumcitys:
                    a = cycle_check_pick(answer[-i-1],tickets)
                    answer=answer[:-i-1] + a + answer[-i:]
    return answer

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]  # 2  4  1  3  5

print(solution(tickets))
"""

""" # 프로그래머스 bfs/dfs  단어 변환
'''
주어진 것 : 시점,끝점,단어들(연결관계가 드러나는 vertex들)

1. 단어끼리 edge만들기. 

2. endpoint 존재성 체크

3. bfs를 이용한 최단거리? 과도한 메모리가 들 것 같다.. 일단 ㄱ(더 효율적인 방법은?)

'''
#begin	target	words	return
#"hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
#"hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	0


def nbr_set(parent,lists):   #parents의 원소가 lists의 list 안에 들어가있으면 그 다음 원소를 넣는 식으로..
    nbr=[]
    for i in lists:
        if parent == i[0]:
            nbr.append(i[1])
        elif parent ==i[1]:
            nbr.append(i[0])
    return nbr


def edges(words):
    edgeset=[]
    for i in words:
        for j in words:
            if i!=j and any([i[0]==j[0],i[1]==j[1],i[2]==j[2]]):
                edgeset.append([i,j])
    return edgeset  #edgeset만들기... not directed.

def solution(begin, target, words):
    if target not in words:
        return 0  #target이 단어모음에 없어서 0으로 end.
    
    edgeset=edges(words)
    
    lengthvertex=[[begin]]
    while target not in lengthvertex[-1]:
        for i in lengthvertex[-1]:
            print(i)
            des = nbr_set(i,edgeset)
            listsinvtx = sum(lengthvertex,[])
            for j in des:
                if j in listsinvtx:
                    des.remove(j)
            
            if i==lengthvertex[-1][0]:
                lengthvertex.append(des)
            else:
                lengthvertex[-1]=lengthvertex[-1]+des
                
    answer = len(lengthvertex)-1
    return answer


begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))
"""

from queue import Queue

a = Queue()


a.put(1)
a.put(3)
a.put(4)

print(a.get())
print(a.get())




