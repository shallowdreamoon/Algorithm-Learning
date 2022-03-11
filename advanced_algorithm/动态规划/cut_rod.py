"""
钢条切割问题
"""

p=[0,1,5,8,9,10,17,17,20,24,30]

def cut_rod_recursion_1(p,n):
    if n==0:
        return 0
    else:
        res=p[n]
        for i in range(1,n):
            res=max(res,cut_rod_recursion_1(p,i)+cut_rod_recursion_1(p,n-i))
    return res


def cut_rod_recursion_2(p,n):
    if n==0:
        return 0
    else:
        res=0
        for i in range(1,n+1):
            res=max(res,p[i]+cut_rod_recursion_2(p,n-i))
    return res

#r_n=max(p[i]+r[n-i])(1<=i<=n)
#动态规划的思想求解(自下向上的求解)
def cut_rod_DP(p,n):
    r=[0]
    for i in range(1,n+1):
        res=0
        for j in range(1,i+1):
            res=max(res,p[j]+r[i-j])
        r.append(res)
    return r[n]

#改进代码，使其不仅输出最优解，而且将最优解时的方案也进行输出
def cut_rod_extend(p,n):
    r=[0]
    s=[0]
    for i in range(1,n+1):
        res_r=0
        res_s=0
        for j in range(1,i+1):
            if p[j]+r[i-j]>res_r:
                res_r=p[j]+r[i-j]
                res_s=j
        r.append(res_r)
        s.append(res_s)
    return r,s

def cut_solution(p,n):
    r,s=cut_rod_extend(p,n)
    ans=[]
    while n>0:
        ans.append(s[n])
        n-=s[n]
    return ans




res=cut_solution(p,9)
print(res)