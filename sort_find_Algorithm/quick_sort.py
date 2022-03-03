def partition(li,left,right):
    tmp=li[left]
    while left<right:
        while left<right and li[right]>=tmp: #从右边找比tmp小的数放到tmp左边
            right-=1  #往左走一步
        li[left]=li[right]
        while left<right and li[left]<=tmp: #从左边找比tmp大的值放到tmp右边
            left+=1
        li[right]=li[left]
    li[left]=tmp  #把tmp归为
    return left

def quick_sort(li,left,right):
    if left<right:  #至少两个元素（从而保证可以递归调用）
        mid=partition(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)

li=[5,7,4,6,3,1,2,9,8]
print(li)
#partition(li,0,len(li)-1)
quick_sort(li,0,len(li)-1)
print(li)