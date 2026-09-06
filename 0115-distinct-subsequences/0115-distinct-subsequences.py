class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
            
        # dp[i][j] stores ways to form t[0...j-1] using s[0...i-1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base Case: An empty t can always be formed by an empty subsequence of s
        for i in range(m + 1):
            dp[i][0] = 1
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    # Match (Take) + Skip
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # No Match (Must Skip)
                    dp[i][j] = dp[i - 1][j]
                    
        return dp[m][n]

        