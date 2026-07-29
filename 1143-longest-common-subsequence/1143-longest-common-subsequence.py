class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memory = {}
        def dfs(i, j):
            if i < 0 or j <0:
                return 0
            if (i,j) in memory:
                return memory[(i, j)]
            if text1[i] == text2[j]:
                memory[(i,j)] = 1 + dfs(i -1, j -1)
            else:
                memory[(i,j)] = max(dfs(i - 1,j), dfs(i,j - 1))
            return memory[(i,j)]
        return dfs(len(text1) -1, len(text2)-1)

         
        

        