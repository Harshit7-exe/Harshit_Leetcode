class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counts = Counter(nums)
        
        # Case 1: Subarray size is 1
        if k == 1:
            unique_nums = [num for num, count in counts.items() if count == 1]
            return max(unique_nums) if unique_nums else -1
            
        # Case 2: Subarray size is the full array length
        if k == n:
            return max(nums)
            
        # Case 3: 1 < k < n (Only boundary elements can be in exactly 1 subarray)
        ans = -1
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
        if counts[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans