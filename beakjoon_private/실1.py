# -*- coding: utf-8 -*-
"""
a=1.4
print(a==int) //false.
"""

"""
n=int(input())

for i in range(n):
    a=int(input())
    if a>0:
        l.append(a)
    elif a<0:
        continue
    else:
        if len(l)>0:
            l=l.sort()
            print(l[0])
            l=l[:1]
        else:
            print(0)   -----> 9,0을 넣은 순간 output이 나오기 때문에 다른방법 강구.
"""

"""
n=int(input())
l=[]
t=[]

for i in range(n):
    a=int(input())
    if a>=0:
        l.append(a)
    else:
        continue

for i in l:
    if i==0:
        if len(t)>0:
            t.sort()
            print(t[0])
            t=t[1:]
        else:
            print(0)
    else:
        t.append(i) -----> 처음시도... 힙이 필요한 이유를 알게됨
"""

"""
import heapq

heap=[]
n=int(input())
l=[]

for i in range(n):
    a=int(input())
    if a>=0:
        l.append(a)
    else:
        continue

for i in l:
    if i==0:
        if len(heap)>0:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, i)  --> 역시 시간초과
"""

"""
import heapq
import sys

heap=[]
n=int(input())

for i in range(n):
    a=int(sys.stdin.readline())
    print(a)

    if a>0:
        print(heapq.heappush(heap, a))
    elif a<0:
        continue
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
            
"""
n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수
    rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')
