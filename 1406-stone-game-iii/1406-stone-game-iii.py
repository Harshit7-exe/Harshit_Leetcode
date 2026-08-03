class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        record = {}
        def dfs(i):
            if i >= n:
                return 0
            if i in record:
                return record[i]
            max_score = float("-inf")
            total = 0
            for k in range(3):
                if i + k <n:
                    total += stoneValue[i + k]
                    max_score = max(max_score, total - dfs(i + k + 1))
            record[i] = max_score
            return max_score
        difference = dfs(0)
        if difference >0:
            return "Alice"
        elif difference < 0:
            return "Bob"
        return "Tie"
        