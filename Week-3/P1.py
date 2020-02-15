a=int(input())
arr=[]
inp = list(map(int,input().split()))
for i in inp:
    arr.append(i)
 
for i in range(a):
    print(arr[i]+arr[-1-i],'',end='')
