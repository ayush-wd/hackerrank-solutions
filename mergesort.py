def mergesort(a):
    if len(a)>1:
        r=len(a)//2
        l=a[:r]
        m=a[r:]
        mergesort(l)
        mergesort(m)
        i=j=k=0
        while i<len(l) and j<len(m):
            if l[i]<m[j]:
                a[k]=l[i]
                i=i+1
            else:
                a[k]=m[j]
                j=j+1
            k=k+1
        while i<len(l):
            a[k]=l[i]
            i+=1
            k+=1
        while j<len(m):
            a[k]=m[j]
            j+=1
            k+=1




























# def mergesort(a):
#     if(len(a)>1):
       
#         r=len(a)//2
#         l=a[:r]
#         m=a[r:]

#         mergesort(l)
#         mergesort(m)

#         i=j=k=0

#         while i< len(l) and j<len(m) :
#             if l[i] < m[j]:
#                 a[k] = l[i]
#                 i = i+1
#             else :
#                 a[k] = m[j]
#                 j = j+1
#             k=k+1
        
#         while i<len(l):
#             a[k] = l[i]
#             i = i+1
#             k=k+1
#         while j<len(m):
#             a[k] = m[j]
#             j = j+1
#             k=k+1
# a = [2,5,-1,6,7,-8]
# mergesort(a)

# print(a)