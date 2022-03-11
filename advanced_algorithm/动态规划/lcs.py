"""
最长公共子序列问题
"""

#返回最长公共子序列的长度
def lcs_length(x,y):
    m=len(x)
    n=len(y)
    c=[[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:  #表示：i，j位置上字符匹配的时候，来自于左上方+1
                c[i][j]=c[i-1][j-1]+1
            else:
                c[i][j]=max(c[i-1][j],c[i][j-1])
    return c[m][n]

#同时返回公共子串
def lcs(x,y):
    m=len(x)
    n=len(y)
    c=[[0 for _ in range(n+1)] for _ in range(m+1)]
    b=[[0 for _ in range(n+1)] for _ in range(m+1)] # 1： 左上方，2：上方，3：左方
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:  #表示：i，j位置上字符匹配的时候，来自于左上方+1
                c[i][j]=c[i-1][j-1]+1
                b[i][j]=1
            elif c[i-1][j]>c[i][j-1]: #来自于上方
                c[i][j]=c[i-1][j]
                b[i][j]=2
            else:
                c[i][j]=c[i][j-1]
                b[i][j]=3
    return c[m][n],b

def lcs_traceback(x,y):
    l,b=lcs(x,y)
    i=len(x)
    j=len(y)
    res=[]
    while i>0 and j>0:
        if b[i][j]==1:  #来自左上方=>>匹配
            res.append(x[i-1])
            i-=1
            j-=1
        elif b[i][j]==2: #来自于上方=>>不匹配
            i-=1
        else:            #来自于左方=>>不匹配
            j-=1
    return "".join(reversed(res))


s1="ABCBDAB"
s2="BDCABA"
res=lcs_length(s1,s2)
l,b=lcs(s1,s2)
print(res)
ans=lcs_traceback(s1,s2)
print(ans)

