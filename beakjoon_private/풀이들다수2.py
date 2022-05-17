# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 23:52:13 2022

@author: 형준
"""


""" # b1 2869 달팽이 올라가버리기.

import sys

u,d,h=map(int,sys.stdin.readline().strip().split()) #up,down,height

h-=u #-last day
tdps=u-d #24hour per speed
t=1 #+1 day.

'''
while h>tdps:
    t+=1
    h-=tdps

print(t)   #### 시간초과
'''

t+=h//tdps
if h%tdps!=0:
    t+=1
print(t)
"""

""" # b2 2292 벌집   (2022.1.27)
n = int(input())

'''
k=1
a=6
b=6
c=2
while True:
    if n==1:
        print(1)
        break
    if k<n and n<k+a:
        print(c)
        break
    k+=a
    a+=b
    c+=1    ---- 시간 초과.
'''    
# 1 7 19 38 61 ... +6+12+18+24 ... 3n(n+1)+1
d=1
if n==1:
    print(1)
else:
    while 3*d*(d+1)+1<n:
        d+=1
    print(d+1)
"""

""" # s4 1978 소수찾기 (22.1.27)
import sys

#cnt=int(sys.stdin.readline())
#m=list(map(int,sys.stdin.readline().strip().split()))


a=list(range(1,1001)) # 25 21(20,101~200) 16 16 17 14 16(15,600~700) 14 17(15,800~900) 15(14,900~1000)
cnt=len(a)
m=''

for i in a:
    m+=str(i)+' '

m=list(map(int,m.strip().split()))
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
isprime=[]

for i in a:
    for j in range(2,32): #2부터 32까지 나누기. .... 나 수학과 맞나??ㅋㅋㅋㅋ
        if i==1:
            cnt-=1
            break
        if (i%j==0 and i!=j):
            cnt-=1 #소수가 아닌거 빼기
            break
print(cnt)  
"""

""" # s2 1929 소수갯수구하기(에라토스테네스) (22.1.28)
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
'''
a,b=map(int,input().strip().split())

cnt=0

def Era_met(n): #Era_met(b)-Era_met(a)
    nums = [True]*(n+1)  #0~n까지의 T/F array
    for i in range(2,len(nums)//2+1):
        if nums[i]==True:
            for j in range(2*i,n+1,i):
                nums[j]=False
    a=[]
    for i in range(len(nums)):
        if nums[i]==True:
            a.append(i)
    #print(a[2:])
    return(nums.count(True)-2) #0,1 count를 뺀 return.

if a==1:
    print(Era_met(b)) #a=1일 때 -1을 return값으로 가짐.
else:
    print(Era_met(b)-Era_met(a-1))  
#3 16 ... 3 5 7 11 13 .... 5개....

'''     ###################### 숫자 사이의 갯수를 구한 뻘짓...,,,,,

a,b=map(int,input().strip().split())

def Era_met(n): #Era_met(b)-Era_met(a)
    nums = [True]*(n+1)  #0~n까지의 T/F array
    for i in range(2,len(nums)//2+1):
        if nums[i]==True:
            for j in range(2*i,n+1,i):
                nums[j]=False
    if a==1:
        for i in range(2,len(nums)):
            if nums[i]==True:
                print(i)
    else:
        for i in range(a,len(nums)):
            if nums[i]==True:
                print(i)

Era_met(b)
                 ########################### 뻘짓한 것은 s2 4948 베르트랑 공준에서 그대로 이용(바로 아래)
"""

""" # s2 4948 베르트랑 공준 (22.1.28)
def Era_met(n): 
    nums = [True]*(n+1)  #0~n까지의 T/F array
    for i in range(2,len(nums)//2+1):
        if nums[i]==True:
            for j in range(2*i,n+1,i):
                nums[j]=False
    a=[]
    for i in range(len(nums)):
        if nums[i]==True:
            a.append(i)
    return(nums.count(True)-2) #0,1 count를 뺀 return.



a=-1
while True:
    a=int(input())
    if a==0:
        break
    else:
        print(Era_met(2*a)-Era_met(a)) #조건 : 'n보다 크고...'
"""

""" # s1 9020 골드바흐의 추측 (22.1.28)
'''
1보다 큰 자연수 중에서  1과 자기 자신을 제외한 약수가 없는 자연수를 소수라고 한다. 
예를 들어, 5는 1과 5를 제외한 약수가 없기 때문에 소수이다. 하지만, 6은 6 = 2 × 3 이기 때문에 소수가 아니다.

골드바흐의 추측은 유명한 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다는 것이다. 
이러한 수를 골드바흐 수라고 한다. 또, 짝수를 두 소수의 합으로 나타내는 표현을 그 수의 골드바흐 파티션이라고 한다. 
예를 들면, 4 = 2 + 2, 6 = 3 + 3, 8 = 3 + 5, 10 = 5 + 5, 12 = 5 + 7, 14 = 3 + 11, 14 = 7 + 7이다. 
10000보다 작거나 같은 모든 짝수 n에 대한 골드바흐 파티션은 존재한다.

2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력하는 프로그램을 작성하시오. 
만약 가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가 가장 작은 것을 출력한다.
'''

def prime10000(): 
    nums = [True]*(10000+1)  #0~10000까지의 T/F array
    for i in range(2,len(nums)//2+1):
        if nums[i]==True:
            for j in range(2*i,10000+1,i):
                nums[j]=False
    a=[]
    for i in range(len(nums)):
        if nums[i]==True:
            a.append(i)
    return(a[2:]) #0,1 count를 뺀 return.

prime = prime10000()

T = int(input())
for i in range(T):
    n=int(input())
    for j in range(n//2,10000):
        if j in prime and n-j in prime:
            print(n-j,j)
            break
"""   #################################딱 2000ms 컷 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

""" # s3 1002 터렛 (22.1.29)

import sys
import math as m
    
c = int(input())
    
for i in range(c):
    [x1,y1,r1,x2,y2,r2] = list(map(int,input().split()))
    r3 = m.sqrt((x1-x2)**2+(y1-y2)**2)
    
    if (x1==x2 and y1==y2 and r1==r2):
        print(-1)
    elif r3>r1+r2 or r3<abs(r1-r2): 
        print(0)
    elif r3==r1+r2 or r3==abs(r1-r2):
        print(1)
    else: 
        print(2)   
"""  ##### 변수로 지정해주고 쓰는 것이 메모리에 훨씬 효율적임(r3)

""" # s1 2447 별 찍기 - 10 (22.1.29)

n = int(input())
    
def printstar(n):
    if n==1:
        return('*')
    
    sn_1 = printstar(n//3)
    l=[]
    for i in sn_1:
        l.append(i*3)
    for i in sn_1:
        l.append(i+' '*(n//3)+i)
    for i in sn_1:
        l.append(i*3)
    return(l)

print('\n'.join(printstar(n)))
"""

""" # s1 11729 하노이의 탑 (22.1.30)

n=int(input())

print(2**n-1) #실행횟수.

def hanoi(n,a,b,c):
    
    if n==1:
        return print(str(a)+' '+str(c))  #블록이 하나만 있을 때의 실행
    
    hanoi(n-1,a,c,b)     #n/2-1까지는 2,3의 위치가 바뀐 하노이.
    print(str(a)+' '+str(c))   #맨 아래 블록 옮기기.
    hanoi(n-1,b,a,c)     #n/2+1부터는 1,2의 위지가 바뀐 하노이.


hanoi(n,1,2,3)
"""

""" # s5 7568 덩치 (22.1.30)

import sys
n=int(sys.stdin.readline())
#n=int(input()) #실험용2
kh = []

for i in range(n):
    kh.append(list(map(int,sys.stdin.readline().strip().split()))+[1]) #정수 kg, height와 순서를 가진 list들을 포함한 list kh. 
#    kh.append(list(map(int,input().strip().split()))+[1]) #실험용2
#kh = [[55,185,1],[58,183,1],[88,186,1],[60,175,1],[46,155,1]] ##싷험용
'''
kh1 = sorted(kh,key = lambda kg : kg[0], reverse = True)
kh2 = sorted(kh1,key = lambda height : height[1], reverse = True) #몸무게,키 비교 돌리기.. 2번이면 충분?
'''  #### 쓰면 안됨..... return을 생각해보자.

for i in kh:
    for j in kh:
        if i[0]>j[0] and i[1]>j[1]:
            j[2]+=1    #순서주기.

s=''
for i in kh:
    s+=str(i[2])+' ' 
print(s.strip())   #한줄로 만들어서 print하기.
"""

""" # s5 1018 체스판 다시 칠하기. (22.2.2)

def mat88sumFromij(mat,i,j):
    a=0
    mat=mat[i:i+8]
    for b in mat:
        a+=sum(b[j:j+8])
    return a  #done.

def recoloredchessmap(nmmap):

    nmtrans1 = [[0 for i in range(len(nmmap[0]))] for j in range(len(nmmap))] #n*m 0행렬
    nmtrans2 = [[0 for i in range(len(nmmap[0]))] for j in range(len(nmmap))] #n*m 0행렬
    
    for i in range(len(nmmap)):
        for j in range(len(nmmap[0])):
            if (i+j)%2==0 and nmmap[i][j]=='W':
                nmtrans1[i][j]=1
    for i in range(len(nmmap)):
        for j in range(len(nmmap[0])):
            if (i+j)%2==1 and nmmap[i][j]=='B':  #i,j의 합이 짝수인 곳 W, 홀수인 곳을 B로 바꾸는 count1
                nmtrans1[i][j]=1
    
    for i in range(len(nmmap)):
        for j in range(len(nmmap[0])):
            if (i+j)%2==0 and nmmap[i][j]=='B':
                nmtrans2[i][j]=1
    for i in range(len(nmmap)):
        for j in range(len(nmmap[0])):
            if (i+j)%2==1 and nmmap[i][j]=='W':  #i,j의 합이 짝수인 곳 B, 홀수인 곳을 W로 바꾸는 count
                nmtrans2[i][j]=1

    sums=[]
    
    for i in range(len(nmtrans1)-7):
        for j in range(len(nmtrans1[0])-7):
            sums.append(mat88sumFromij(nmtrans1,i,j))
            sums.append(mat88sumFromij(nmtrans2,i,j))  #가장 작은 값 구하기.
    
    return(print(min(sums))) #가장 작은 수를 print

n,m = map(int,input().strip().split())
nmmap = []
for i in range(n):
    nmmap.append(input().strip())   #nmmap완성.

recoloredchessmap(nmmap)
"""

""" # b1 2750 수 정렬하기

n=int(input())
nums=[]
    
for i in range(n):
    nums.append(int(input()))
    
nums.sort()

for i in nums:
    print(i)
"""

""" # s5 2751 수 정렬하기2.... 2750이랑 차이?

import sys

n=int(sys.stdin.readline())
nums=[]
for i in range(n):
    nums.append(int(sys.stdin.readline()))

def merge_sort(nums):
    
    if len(nums)==1:
        return nums
    
    mid = len(nums)//2
    right = merge_sort(nums[mid:])
    left = merge_sort(nums[:mid])
    
    i,j,k = 0,0,0
    
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            nums[k] = left[i]
            i+=1
        else:
            nums[k] = right[j]
            j+=1
        k+=1
    
    if i==len(left):
        while j<len(right):
            nums[k] = right[j]
            j+=1
            k+=1
    if j==len(right):
        while i<len(left):
            nums[k] = left[i]
            i+=1
            k+=1
    
    return nums

nums=merge_sort(nums)

for i in nums:
    print(i)  
"""

""" # s4 2108 통계학   (22.2.5)

import sys

n=int(input())
m=[]
for i in range(n):
    m.append(int(input()))
        
################
print(round(sum(m)/n)) #1번 round함수는 반올림함수. n,a를 쓰면 소수 a번째 자리에서 반올림. 안쓰면 정수반올림.
#############
def merge_sort(nums):
    
    if len(nums)==1:
        return nums
    
    mid = len(nums)//2
    right = merge_sort(nums[mid:])
    left = merge_sort(nums[:mid])
    
    i,j,k = 0,0,0
    
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            nums[k] = left[i]
            i+=1
        else:
            nums[k] = right[j]
            j+=1
        k+=1
    
    if i==len(left):
        while j<len(right):
            nums[k] = right[j]
            j+=1
            k+=1
    if j==len(right):
        while i<len(left):
            nums[k] = left[i]
            i+=1
            k+=1
    
    return nums

m=merge_sort(m)
print(m[(n//2)]) #2번.... n은 홀수라는 조건, 2751의 수 정렬하기와 결과적으로 같은 시간,메모리 제한이 있기 때문에 merge_sort를 사용.
###################
#m_cnt.. keys = num, values = cnt.
m_cnt = {}
for i in m:
    if i in m_cnt.keys():
        m_cnt[i]+=1
    else:
        m_cnt[i]=1

max_nums = []
max_cnt = max(m_cnt.values())
for i in m_cnt.keys():
    if m_cnt[i]==max_cnt:
        max_nums.append(i)

if len(max_nums)==1:
    print(max_nums[0])
else: 
    print(max_nums[1]) #3번

###########

print(m[-1]-m[0]) #4번
"""

""" # s5 1427 소트인사이드  (22.2.5)

n = list(map(int,input().strip()))

n.sort(reverse = True)

m=''

for i in n:
    m+=str(i)
    
print(m)
"""

""" # s2 18870 좌표압축 (22.2.6)


n = int(input())
m =list(map(int,input().split(' ')))
'''
import sys

n = int(sys.stdin.readline().split())
m =list(map(int,sys.stdin.readline().split()))
'''
def merge_sort(nums):
    
    if len(nums)==1:
        return nums
    
    mid = len(nums)//2
    right = merge_sort(nums[mid:])
    left = merge_sort(nums[:mid])
    
    i,j,k = 0,0,0
    
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            nums[k] = left[i]
            i+=1
        else:
            nums[k] = right[j]
            j+=1
        k+=1
    
    if i==len(left):
        while j<len(right):
            nums[k] = right[j]
            j+=1
            k+=1
    if j==len(right):
        while i<len(left):
            nums[k] = left[i]
            i+=1
            k+=1
    
    return nums

i=1
res=[]
m_sort = merge_sort(list(set(m)))
m_ord = {}
for i in range(len(m_sort)):
    m_ord[m_sort[i]]=i


while True:
    for j in m:
        print(m_ord[j], end = ' ')
    break
"""  ##### sorted를 잘 이용해보자.

""" # s5 10814 나이순정렬 (22.2.7)

n=int(input())
people={}

for i in range(n):
    a,b = map(str,input().split(' '))
    if int(a) in people.keys():
        people[int(a)].append(b)
    else:
        people[int(a)]=[b]

c = sorted(people.keys())

for i in c:
    d = people[i]
    for j in d:
        print(str(i)+' '+j)
"""   ###### [[] for i in range(201)]..... list의 순서로 아이디어... 좋다.

""" # g4 2580 스도쿠     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx 미완
import sys

sdk=[]    #aim! keys : (i,j,k)... i행 j열 k칸.  values:들어가는 숫자.
'''
1 2 3
4 5 6
7 8 9 ....k
'''
def make_k(i,j):
    if j<3:
        if i<3: 
            k=1 
        elif i<6:
            k=2
        else:
            k=3
    elif j<6:
        if i<3: 
            k=4 
        elif i<6:
            k=5
        else:
            k=6        
    else:
        if i<3: 
            k=7 
        elif i<6:
            k=8
        else:
            k=9
    return k

for i in range(9):
    rows = list(map(int,input().split(' ')))
    for j in range(9):
        sdk.append({row: i+1, col : j+1, dial : maek_k(i,j), num : rows[j]})
        #sdk[(i+1,j+1)]=rows[j]  

#and, or, not은 boolean.
while True:
    for e in sdk:
        for ro in range(1,10):
            while e[row] == ro:
                
"""    #이거 우짜면 좋노??

""" # s3 15649 N과 M(1)  (22.2.12?)   .......  num 이하의 수에서 서로 겹치치 않는 cnt 길이의 모든 수열을 구하기...!...
num,cnt = map(int,input().split())

nums = [i for i in range(1,num+1)]

def permute(nums,cnt):
    for i in range(len(nums)):
        if cnt==1:
            yield [nums[i]]
        else:
            for n1 in permute(nums[:i]+nums[i+1:],cnt-1):
                yield [nums[i]]+n1

def stringchanger(lis):
    a = ''
    for i in lis:
        a = a + str(i) + ' '
    return a[:-1]

for i in permute(nums,cnt):
    print(stringchanger(i))
"""    

""" # s3 15650 N과 M(2)
num,cnt = map(int,input().split())

nums = [i for i in range(1,num+1)]
arr=[]

def stringchanger(lis):
    a = ''
    for i in lis:
        a = a + str(i) + ' '
    return a[:-1]

def setcount(nums,cnt):  #wanted : list로 결과 나오게.
    if cnt==1:
        for i in nums:
            if i not in arr:
                arr.append(i)
                print(stringchanger(arr))
                del arr[-1]
        return
    else:
        for j in range(len(nums)):
            if nums[j] not in arr:
                arr.append(nums[j])
                setcount(nums[j:],cnt-1)
                arr.remove(nums[j])

setcount(nums,cnt)
"""

 # b3 2839 설탕배달 done.
""" # b2 1233 주사위  (22.2.13?)

a,b,c = map(int,input().split(' '))

cntlist = {}
for i in range(3,a+b+c+1):
    cntlist[str(i)]=0
    
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            cntlist[str(i+j+k)]+=1

maxcnt = max(cntlist.values())

for i in cntlist.keys():
    if cntlist[i]==maxcnt:
        print(i)
        break
"""

""" # s3 11047 동전0  (22.2.13?)
import sys
 
n, needs = map(int,input().split())
moneys = []
for i in range(n):
    moneys.append(int(input()))
moneys = moneys[::-1]
cnt=0

while needs != 0:
    for i in moneys:
        while i<=needs:
            cnt+=needs//i
            needs = needs%i
print(cnt) 
"""   

""" # s5 11723 집합  (22.2.15)
import sys

n = int(sys.stdin.readline())

S=[]

for i in range(n):
    m=sys.stdin.readline().strip().split(' ')
    if m[0] =='all':
        S=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    elif m[0]=='empty':
        S=[]
    elif m[0]=='add':
        if int(m[1]) not in S:
            S.append(int(m[1]))
    elif m[0]=='remove':
        if int(m[1]) in S:
            S.remove(int(m[1]))
    elif m[0]=='toggle':
        S.remove(int(m[1])) if int(m[1]) in S else S.append(int(m[1]))
    else:
        print(S.count(int(m[1])))
""" #벡준은 두줄 이상 사용할 때 input에 항상 엔터가 들어간다고 한다. 주의!!!!

""" # s4 1120 문자열  (22.2.16)
 
a,b = map(str,input().strip().split(' '))

difcnt =[0 for i in range(len(b)-len(a)+1)]
for i in range(len(b)-len(a)+1):
    for j in range(len(a)):
        if b[i+j]!=a[j]:
            difcnt[i]+=1

print(min(difcnt))
"""

""" # s3 15651 N과 M(3)  (22.2.16)

num,cnt = map(int,input().split())

nums = [i for i in range(1,num+1)]
arr=[]

def stringchanger(lis):
    a = ''
    for i in lis:
        a = a + str(i) + ' '
    return a[:-1]

def setcount(nums,cnt):  #wanted : list로 결과 나오게.
    if cnt==1:
        for i in nums:
            arr.append(i)
            print(stringchanger(arr))
            del arr[-1]
        return
    else:
        for j in range(len(nums)):
            arr.append(nums[j])
            setcount(nums,cnt-1)
            del arr[-1]

setcount(nums,cnt)
"""




""" # s5 16171 난 친없찐ㅠ
a=input()
b=input()

c=''
nums=['0','1','2','3','4','5','6','7','8','9']

for i in a:
    if i not in nums:
        c+=i

if b in c:
    print(1)
else:
    print(0)
"""

""" # g5 17214 다항함수의 적분.
'''
입력 : 첫째 줄에 최대 일차 일변수 다항식이 주어진다. 
항의 개수는 최대 2개이고, 변수는 항상 x로 주어지며, 각 항은 공백 문자로 구분되지 않는다. 
주어지는 계수는 절댓값이 10,000을 넘지 않는 0이 아닌 2의 배수이고 
주어지는 상수는 절댓값이 10,000을 넘지 않는 정수이다. 
차수가 같은 항은 한 번만 주어진다. 단, 계수의 절댓값이 1인 경우에는 1을 생략한다.   ****************
다항식은 차수가 큰 것부터 작아지는 순서대로 주어진다.

출력 : 주어진 일변수 다항식을 적분한 결과를 입력 형식과 동일하게 출력한다. 적분상수는 "W"로 x2은 "xx"로 표현한다.
'''
c = input().strip()   #+대신 -가 들어가는 케이스 고려 필요.

if c[1:].count('-') == 1: #두 번째가 -인 경우
    if c[0]=='-': #첫 번째가 -인 경우
        a=list(map(str,c[1:].split('-')))
        a[0] = '-' + a[0]
    else:
        a=list(map(str,c.split('-')))
    a[1] = '-' + a[1]
else: #두 번째가 +인 경우.
    if c[0]=='-':
        a=list(map(str,c[1:].split('+')))
        a[0] = '-' + a[0] # - +
    else:
        a=list(map(str,c.split('+'))) # + +

b = {'x':0,'c':0 ,'xud':'','cud':'+'}
#각각의 계수끼리 합차계산
for i in a:
    if 'x' in i:
        b['x']+=int(i[:-1])
    else:
        b['c']+=int(i)

# 음수양수 나눠서 변환.
if b['x']<0:
    b['x']=abs(b['x'])
    b['xud']='-'
if b['c']<0:
    b['c']=abs(b['c'])
    b['cud']='-'

# 출력 진행
if b['x']==0 and b['c']==0:   #x=0인 케이스.
    print('W')   
elif b['x']==0 and b['c']!=0:
    if b['cud']=='-':
        if b['c']==1:
            print('-x+W')            
        else:
            print('-{}x+W'.format(b['c']))
    else:
        if b['c']==1:
            print('x+W')
        else:
            print('{}x+W'.format(b['c']))   #x가 없으므로 b['cud']를 넣으면 안됨
elif b['x']==2 and b['c']!=0:
    if b['c']==1:
        print('{}xx{}x+W'.format(b['xud'],b['cud']))
    else:
        print('{}xx{}{}x+W'.format(b['xud'],b['cud'],b['c']))
elif b['x']==2 and b['c']==0:
    print('{}xx+W'.format(b['xud']))
elif b['x']!=0 and b['c']==0:        #나머지 케이스.
    print('{}{}xx+W'.format(b['xud'],int(b['x']/2)))
else:
    if b['c']==1:
        print('{}{}xx{}x+W'.format(b['xud'],int(b['x']/2),b['cud']))
    else:
        print('{}{}xx{}{}x+W'.format(b['xud'],int(b['x']/2),b['cud'],b['c']))

""" #그지같네 ㅠ
 
""" 
programers lvl2(bfs/dfs) target_number
b=[1,1,1,1,1]
c=[0]
d=c.copy()
for i in b:
    for j in range(len(c)):
        c[j]+=i
        d[j]-=i
    c=c+d
    d=c.copy()
    print(c)

print(c.count(3))
"""
 
''' # s3 1874 스택 수열   - 틀림

n = int(input())
seq = []

for i in range(n):
    seq.append(int(input().strip()))
#seq = [4,3,6,8,7,5,2,1] #나중에 for 문으로 만들어주기.
#seq = (1,2,5,3,4) done.

def succstack(seq):
    a=0
    for i in range(len(seq)):
        if seq[i] in monoton_seq:
            for j in range(seq[i]-a):
                print('+')
                a=seq[i]
            print('-')
        elif seq[i-1]>seq[i]:
            print('-')  #될 때 성공!

monoton_seq = [0]
for i in seq:
    if i>monoton_seq[-1]:
        monoton_seq.append(i)   #monoton_seq 구현.

m = seq.index(n) #max_num 의 index.
#print(m) #3
#print(seq[m:]) #[8,7,5,2,1]
#print(seq[:m+1]) #[4,3,6,8]
for i in range(len(seq)-1):
    if i<m:
        if not (seq[i+1]>seq[i] or seq[i]-seq[i+1]==1):
            print('NO')
            break
    elif i>m-1:   
        if not (seq[i+1]<seq[i]):
            print('NO')
            break
else:
    succstack(seq)
 #예시는 맞았는데 틀림..?.. 3%clear, 7%false..?
'''
