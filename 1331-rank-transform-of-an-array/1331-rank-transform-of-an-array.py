class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        curr = 1

        for num in sorted(set(arr)):
            rank[num] = curr
            curr += 1

        return [rank[num] for num in arr]
        