class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_num = max(nums)
        points = [0] * (max_num + 1)

        
        for num in nums:
            points[num] += num

        
        prev_two = 0
        prev_one = 0

        for total_point in points:
            current = max(prev_one, prev_two + total_point)
            prev_two = prev_one
            prev_one = current

        return prev_one
        