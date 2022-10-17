def bsearch(a,l,h,x):
    if l<=h:
        mid=(l+h)//2
        if a[mid]==x:
            return mid
        elif a[mid]>x:
            return bsearch(a,l,mid-1,x)
        else:
            return bsearch(a,mid+1,h,x)

a=[1,2,3,4,5,6]
low=0
high=len(a)-1
x=3
print(bsearch(a,low,high,x))