import random

def k(w, wt, val, n):    
    if n==0 or w==0:
        return 0
    if wt[n-1] > w:
        return k(w,wt,val,n-1)
    else :
        return max(val[n-1] + k(w-wt[n-1],wt,val,n-1), k(w,wt,val,n-1))
     


val = []
wt = []
for i in range(10):
    j=random.randint(1,10)
    wt.append(j)
    f=random.randint(1,10)
    val.append(f)

w = 50
n=len(val)
print(n)
print(wt)
print(val)
print(k(w,wt,val,n))