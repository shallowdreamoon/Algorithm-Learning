"""
最大公约数
"""

#辗转相除法
def gcd_recursion(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def gcd_no_recursion(a,b):
    while b>0:
        t=a%b
        a=b
        b=t
    return a
res=gcd_no_recursion(12,16)
print(res)