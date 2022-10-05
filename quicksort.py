import random
import time
def partition(a,low,high):
    pivot = a[high]
    i=low-1

    for j in range(low,high):
        if(a[j]<=pivot):
            i=i+1
            (a[j],a[i]) = (a[i],a[j])
    (a[i+1],a[high]) = (a[high],a[i+1])
    return i+1

def quicksort(a, low, high):
    if low<=high:
        pi = partition(a,low,high)
        quicksort(a,low,pi-1)
        quicksort(a,pi+1,high)


a = []
for x in range(500):
    y=random.randint(1,500)
    a.append(y)
low=0
high = len(a)-1
p=time.time()
quicksort(a, low, high)
q=time.time()
print(a)
print(q-p)
