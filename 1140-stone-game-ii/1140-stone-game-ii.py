class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # suffix_sums[i] stores the total stones from pile i to the end
        suffix_sums = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]
            
        memo = {}
        
        def dp(i: int, m: int) -> int:
            
            if i >= n:
                return 0
            if i + 2 * m >= n:
                return suffix_sums[i]
                
            if (i, m) in memo:
                return memo[(i, m)]
            
            
            min_opponent_stones = float('inf')
            for x in range(1, 2 * m + 1):
                min_opponent_stones = min(min_opponent_stones, dp(i + x, max(m, x)))
            
           
            memo[(i, m)] = suffix_sums[i] - min_opponent_stones
            return memo[(i, m)]
            
        return dp(0, 1)