class Solution(object):
    def coinChange(self, m, n):
        dp=[n+1]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            for j in m:
                if i-j>=0:
                    dp[i]=min(dp[i],1+dp[i-j])
        return dp[n] if dp[n]!=n+1 else -1

# Time Complexity: O(m*n)  where m is number of coins and n is the amount
# Space Complexity: O(n)