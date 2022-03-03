import random

def merge(li,low,mid,high):
    i=low
    j=mid+1
    ltemp=[]
    while i<=mid and j<=high:
        if li[i]<li[j]:
            ltemp.append(li[i])
            i+=1
        if li[j]<li[i]:
            ltemp.append(li[j])
            j+=1
    #while循环完后，至少有一部分已经已经无元素了，这时需要把有元素的一部分写进ltemp即可
    while i<=mid:
        ltemp.append(li[i])
        i+=1
    while j<=high:
        ltemp.append(li[j])
        j+=1

    #排序完成后，将ltemp的内容写进li中
    li[low:high+1]=ltemp

def merge_sort(li,low,high):
    if low<high: #说明至少有两个元素，即可以递归
        mid=(low+high)//2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)

li=list(range(10))
random.shuffle(li)
print(li)
merge_sort(li,0,len(li)-1)
print(li)