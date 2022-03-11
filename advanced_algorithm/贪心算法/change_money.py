"""
找零问题
"""
t=[100,50,20,5]

def change(t,n):
    m=[0 for _ in range(len(t))]
    for i,money in enumerate(t):
        m[i]=n // money
        n=n % money
    return m,n

res=change(t,376)
print(res)