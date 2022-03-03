import random

#堆的向上调整---构成小根堆
def sift(li,low,high):
    i=low  #根节点的位置
    j=2*i+1  #左孩子的位置
    tmp=li[i]  #根节点
    while j<=high:  #只要j位置有数
        if j+1<=high and li[j+1]<li[j]:  #只要j+1位置有数且右孩子比左孩子大
            j=j+1  #j指向更大的右孩子
        if tmp>li[j]:  #根节点小于大的那个孩子
            li[i]=li[j]
            i=j  #更新根节点的位置
            j=2*i+1
        else:  #tmp更大时，则将其放在i的位置
            li[i]=tmp  #把tmp放在某一级领导的位置
            break
    else:
        li[i]=tmp  #如果根节点已经到了最后一层，则直接将其放在叶子节点上

def topk(li,k):
    #1.切片取出li中前k个数并将其构成小根堆heap
    heap=li[0:k]
    for i in range((k-2)//2,-1,-1):
        sift(heap,i,k-1)

    #2.从li中第k+1个元素开始遍历，并将每个值与heap中的堆顶元素作比较，若是比heap[0]大，则替换堆顶元素，然后将heap重新调整
    for i in range(k,len(li)-1):
        if li[i]>heap[0]:
            heap[0]=li[i]
            sift(heap,0,k-1)

    #遍历heap，将其中数字按序输出
    for i in range(k-1,-1,-1):
        heap[0],heap[i]=heap[i],heap[0]
        sift(heap,0,i-1)

    return heap





li=[random.randint(0,1000) for i in range(100)]
random.shuffle(li)
res=topk(li,10)
print(res)