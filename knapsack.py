import random

def knapsack(w,wt,val,n):
    if n==0 or w==0:
        return 0
    elif wt[n-1]>w:
        return knapsack(w,wt,val,n-1)
    else:
        return max(val[n-1] + knapsack(w-wt[n-1],wt,val,n-1), knapsack(w,wt,val,n-1))


val=[]
wt=[]
w=50
for a in range(3):
    t=random.randint(1,100)
    val.append(t)
    t=random.randint(1,50)
    wt.append(t)
n=len(val)
print(val)
print(wt)
print(knapsack(w,wt,val,n))




























# import random

# def k(w, wt, val, n):    
#     if n==0 or w==0:
#         return 0
#     if wt[n-1] > w:
#         return k(w,wt,val,n-1)
#     else :
#         return max(val[n-1] + k(w-wt[n-1],wt,val,n-1), k(w,wt,val,n-1))
     


# val = []
# wt = []
# for i in range(10):
#     j=random.randint(1,10)
#     wt.append(j)
#     f=random.randint(1,10)
#     val.append(f)

# w = 50
# n=len(val)
# print(n)
# print(wt)
# print(val)
# print(k(w,wt,val,n))