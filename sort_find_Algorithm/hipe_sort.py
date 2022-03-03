import random
#堆的向下调整
def sift(li,low,high):
    i=low  #根节点的位置
    j=2*i+1  #左孩子的位置
    tmp=li[i]  #根节点
    while j<=high:  #只要j位置有数
        if j+1<=high and li[j+1]>li[j]:  #只要j+1位置有数且右孩子比左孩子大
            j=j+1  #j指向更大的右孩子
        if tmp<li[j]:  #根节点小于大的那个孩子
            li[i]=li[j]
            i=j  #更新根节点的位置
            j=2*i+1
        else:  #tmp更大时，则将其放在i的位置
            li[i]=tmp  #把tmp放在某一级领导的位置
            break
    else:
        li[i]=tmp  #如果根节点已经到了最后一层，则直接将其放在叶子节点上

#堆排序
def heap_sort(li):
    n=len(li)
    for i in range((n-2)//2,-1,-1):   #从最后一个非叶子节点开始调整，从而使整体构成一个堆
        sift(li,i,n-1)
    #建堆完成后开始将堆顶元素和最后一个元素换位
    for i in range(n-1,-1,-1):
        li[0],li[i]=li[i],li[0]
        sift(li,0,i-1)


li=[random.randint(0,10) for i in range(5)]
random.shuffle(li)
heap_sort(li)
print(li)