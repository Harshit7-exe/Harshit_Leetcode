class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
                
        num_set = set(nums)
        start, end = min(nums), max(nums)
        return [x for x in range(start + 1, end) if x not in num_set]
        