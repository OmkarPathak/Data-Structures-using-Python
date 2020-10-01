def top_down(s1,s2,n,m):
    dp=[[0 for x in range(n+2)] for x in range(m+2)]
    for x in range(n+1):
        for y in range(m+1):
            if x==0 or y==0:
                dp[x][y]=0
            elif s1[x-1]==s2[y-1]:
                dp[x][y]=1+dp[x-1][y-1]
            else:
                dp[x][y]= max(dp[x-1][y],dp[x][y-1])
    return m+n-dp[x][y]     

s2 = "AGGTAB"
s1 = "GXTXAYB"
b=top_down(s1,s2,len(s1),len(s2))
print(b
