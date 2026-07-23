class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        if n <= 2:
            return n
        while ans <= n:
            ans <<= 1
        return ans 
