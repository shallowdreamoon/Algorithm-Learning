def linear_search(li,val):
    for ind,v in enumerate(li):
        if v==val:
            return ind
    else:
        return None

def binary_search(li,val):
    left=0
    right=len(li)-1
    while left<=right:
        mid=(left+right)//2
        if li[mid]==val:
            return mid
        elif li[mid]<val:
            left=mid+1
        else:
            right=mid-1
    else:
        return None





li=[1,2,3,4,5,6,78,9]
res=binary_search(li,5)
print(res)