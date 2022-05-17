# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 22:55:30 2022

@author: 형준
"""

"""
import sys
n=int(sys.stdin.readline(' '))

for i in range(n):
    a,b=map(int, sys.stdin.readline().split(' '))
    print(a+b)
    
"""    

"""
n=input()
m=n
c=0

while 1:
    if len(m)==1:
        m="0"+m
    p = str(int(m[0])+int(m[1]))
    m=m[-1]+p[-1]
    
    c+=1
    if m==n:
        break
    
print(c)
"""            

"""            
###############while ~ bronze1
n=int(input())
m=n
c=0

while True:
    a=m//10
    b=m%10
    d=(a+b)%10
    m=(b*10)+d
    
    c+=1
    if (m==n):
        break
print(c)

"""

"""############숫자큰거,몇번째. b2
dic={}

for i in range(1,10):
    a=int(input())
    dic[str(i)]=a
    
dic2={str(v):k for k,v in dic.items()}

print(max(dic.values()))
print(dic2.get(str(max(dic.values()))))
"""

""" ######### b2 각 자릿수의 숫자count
a=1
for i in range(3):
    a=a*int(input())
    
a=str(a)

for j in range(10):
    print(a.count(str(j)))
"""

"""# 숫자들을 42로 나누었을 때 생긴 서로 다른 나머지의 갯수 count

a=int(input())
b=[a%42]

for i in range(9):
    c=int(input())
    if c%42 not in b:
        b.append(c%42)

print(len(b))
"""

"""# b1 4344 평균은 넘겠지
import numpy as np

a=int(input())
g=1

for i in range(a):
    c=input().split()
    d=list(map(int,c[1:]))
    e=np.mean(d)
    d.sort()
    for i in d:
        if i<e:
            g+=1
            break
    print(str(float(g*1000/int(c[0]))/10)+"%")
    g=0
    ##################미결. 런타임에러.
""" 

"""# s1 4673 셀프nbr

def d(n):
    s=list(map(int,str(n)))
    for i in s:
        n+=i
    return n

def snd(): #n=bd.nbr 
    a=[i for i in range(10000)]    
    for i in range(9999):
        try:
            a.remove(d(i))
        except:
            continue
    for i in a:
        print(i)        
    
snd()
"""


"""# s4 1065 한수 ... n<=1000
n=int(input())

def hn(n):
    if n<100:
        return(n)
    else:
        hs=99 #100 미만의 수는 모두 한수.
        for i in range(100,n+1):
            a=list(map(int,str(i)))
            if a[0]-a[1]==a[1]-a[2]:
                hs+=1
    return hs

print(hn(n))

#i=100
#a=list(map(int,str(i)))
#print(a)                   ...return 100
"""

"""
# b2 15596 정수합
n=input()

def solve(a):
    b=0
    for i in a:
        b+=i
    return(b)

print(solve(n))
"""

"""
# b2 11720 숫자합
z=[1,2,5]
print(sum(z))
"""


"""#b2 10809 알파벳 찾기
n=input()
b={}
for i in range(len(n)):
    if n[i] in b.keys():
        continue
    else:
        b[n[i]]=i

c=''

for i in list(map(chr, range(97, 123))):  #아스키코드.. a~z.
    if i in b.keys():
        c+=str(b[i])
        c+=' '
    else:
        c+='-1 '

print(c)
"""

"""
# s5 2941 크로아티아 알파벳
#ca=['c=','c-','dz=','d-','lj','nj','s=','z=']
ca1=['c=','dz=','s=']
ca2=['z=','c-','d-','lj','nj']
# lj.e.s=.nj.a.k  return 6
#d.dz=.z=  return 3
#nl.j.j  return 3

str=input()
#ca에 있는 문자로 str을 나누자.
'''
for i in ca1
    try:
        str=str.split(i)
        a+=len(str)-1
    execpt    
    
    
str1='asz=ddz=asf'  ----시도1
ss1=str1.split('dz=')
print(ss1)
ss2=[]
for i in ss1:
    ss2+=[i.split('z=')]
print(ss2)


str1='asz=ddz=asf'  #return 8, 시도2

str1=str1.replace('dz=', '1')  # '12sd12'
print(str1)    ----------------------사용법 연습.
'''

for i in ca1:
    str=str.replace(i,'1')
for i in ca2:
    str=str.replace(i,'2')
print(len(str))
"""

"""
# b2 1152 단어의 개수

#첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 
#이 문자열의 길이는 1,000,000을 넘지 않는다. 
#단어는 공백 한 개로 구분되며, 
#공백이 연속해서 나오는 경우는 없다. 또한 문자열은 공백으로 시작하거나 끝날 수 있다.
'''str=input()
c=1 #nbr of units

if str[-1]==' ':
    str=str[:-1]  #뒷공백 제거
    
if str[0]==' ':
    str=str[1:]  #앞공백 제거

for i in str: 
    if i==' ':
        c+=1
print(c)       -----------------런타임에러(index error)
'''
import sys

input = sys.stdin.readline().strip().split()  #디버깅하는 방법 배울것!!

print(len(input))
"""

"""
# b3 10818 최소,최대
import sys

b=list(map(int,sys.stdin.readline().split()))

print(str(max(b))+' '+str(min(b)))
"""

"""
# s2 1927 최소힙
import heapq as hq
import sys

n=int(sys.stdin.readline())
a=[]

for i in range(n):
    b=int(sys.stdin.readline())
    if b==0:
        if a:
            print(hq.heappop(a))
        else:
            print(0)
    else:
        hq.heappush(a, b)
"""

"""
# b1 4344 평균은 넘겠지

import sys  #벡준에서는 input()을 sys.stdin.readline()으로 바꿈.

n = int(input())

for i in range(n):
    n1 = list(map(int,input().strip().split()))
    n2 = n1[0]
    n3 = 0
    average = sum(n1[1:])/n2
    for i in n1[1:]:
        if i>average:
            n3+=1

    per = int(1000000*n3/n2)/10   #소수 4째짜리까지 나오는 확률에 1000을 곱한 수.
    if int(str(per)[-1])>=5:
        per+=1                    #반올림
    per=str(int(per))
    print(per[:2]+'.'+per[2:]+'%')     #output
################################## 정상적으로 작동하는 것 같은데 코드가 먹질 않는다.....(결과 5개는 똑같이 잘 나옴!)
################################## output은 percent를 줘야하나??...
=============================================================================================

n = int(input())

for i in range(n):
    n1 = list(map(int,input().strip().split()))
    tp = n1[0]
    cp = 0
    average = sum(n1[1:])/tp
    for j in n1[1:]:
        if j>average:
            cp+=1
    per= cp/tp*100
    print(f'{per:.3f}%')   #처음보는 이게 뭐꼬???? + 여기는 왜 sys가 안쓰이는거지..?......
"""

"""# b3 10871 X보다 작은 수
import sys

a,b=map(int, sys.stdin.readline().strip().split())
c=list(map(int,sys.stdin.readline().strip().split()))
for i in c:
    if i<b:
        print(i)      
"""

"""# g5 1011 Fly me to the Alpha Centauri

'''
n per 번의 길이를 움직일 때 마지막에 1이 되게 만들 수 있는 거리의 최소값 = n(n-1)/2
 = 0에서 n으로 가속을 최대로 했을 때 드는 거리.(필요횟수=n)

거리 = b-a... 얼마나 가속할 수 있느냐? b-a-n(n-1)이 양수가 되는 최대 n.

최대속 = n
필요시간 = n(n-1) + k
(k는 b-a-n(n-1)-nk가 양수가 될 수 있는 최대값.)
end.    ---------------         XXXXXXXXXXXXX

그냥 수열 2개의 return. 

ex1.
dist=5.
1 2 1 1.. 4

ex2.
dist=4.
1 2 1.. 3 
'''

import sys    #벡준에서는 input()을 sys.stdin.readline()으로 바꿔줄 것!

n=int(input())

for i in range(n):
    a,b=map(int,input().split())
    l=b-a
    n=1
    while True:
        if l<=n**2:
            print(2*n-1)
            break
        elif l<=n*(n+1):
            print(2*n)
            break
        n+=1
"""

"""# b1 2839 설탕배달

n=int(input())

def cal(n):
    c=0
    if n in [1,2,4,7]:
        return(print(-1))
    while n>15:
        n-=15
        c+=3
    if n in [1,3,5]: #3*5+1= 5*2+3*2
        return(print(c+1))
    if n in [2,4,6,8,10]:
        return(print(c+2))
    if n in [7,9,11,13,15]:
        return(print(c+3))
    if n in [12,14]:
        return(print(c+4))

cal(n)
"""

"""# b1 1193 분수찾기(짝짝이분수...ㄷㄷ)

'''
분자! : 1.12321.123454321.   ....     1,1+(1+4),1+(1+4)+(1+4+4),... 1,6,15,...
분모! : 121.1234321.12345654321.      3,3+(3+4),3+(3+4)+(3+4+4),... 3,10,21...
'''
n1=int(input())


n2=int(str(n1)) #분모에 쓸려고 만든거.

k1,k2=1,3 #수열용 수 2개. 
d1,d2=4,4
d3,d4=1,2 #수열 어시용 수 4개.

while k1<n1: #분자
    n1-=k1 
    k1+=d1 
    d3+=2 #d3:분자 피라미드의 최고높이
#n1: 피라미드에서 몇번째.    

while k2<n2: #분모 8
    n2-=k2 #5
    k2+=d2 #
    
    d4+=2 #d3 :분모 피라미드의 최고높이
#n2: 피라미드에서 몇번째.

if n1>d3:
    n1=2*d3-n1
if n2>d4:
    n2=2*d4-n2
    
print(str(n1)+'/'+str(n2))    ㅋㅋㅋㅋㅋ 이상한 방법으로 풀어제낌.

"""    