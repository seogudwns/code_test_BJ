# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 19:27:14 2022

@author: 형준
"""

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
    
    if len(tickets)!=0:
        while len(tickets)!=0:
            for i in range(len(answer)):                
                sumcitys = sum(tickets,[])  #한칸 밑으로 빼면 좋겠지만 케이스마다 체크해야하므로 메모리가 더 들더라도 안쪽으로 넣음.
                if answer[-i-1] in sumcitys:
                    a = cycle_check_pick(answer[-i-1],tickets)
                    answer=answer[:-i-1] + a + answer[-i:]
    return answer