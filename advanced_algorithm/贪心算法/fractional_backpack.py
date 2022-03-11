"""
分数背包问题
"""
goods=[(60,10),(100,20),(120,30)]
print(goods)
goods.sort(key=lambda x:x[0]/x[1],reverse=True)
print(goods)

def fractional_backpack(goods,w):
    m=[0 for _ in range(len(goods))]
    total_v=0
    for i,(prize,weight) in enumerate(goods):
        if w > weight:
            m[i]+=1
            w-=weight
            total_v+=prize
        else:
            m[i]=w/weight
            w=0
            total_v+=m[i]*prize
            break
    return m,total_v
res=fractional_backpack(goods,50)
print(res)

