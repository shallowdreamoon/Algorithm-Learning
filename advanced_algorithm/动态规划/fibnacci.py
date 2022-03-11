"""
斐波那契数列
"""

#递归式写法
#缺点：子问题的重复计算
def fibnacci(n):
    if n==1 or n==2:
        return 1
    return fibnacci(n-1)+fibnacci(n-2)

#非递归式写法
#采用了动态规划（DP）的思想=递推式+重复子问题
def fibnacci_no_recursion(n):
    f=[0,1,1]
    if n>2:
        for i in range(n-2):
            num=f[-1]+f[-2]
            f.append(num)
    return f[n]
res=fibnacci_no_recursion(100)
print(res)