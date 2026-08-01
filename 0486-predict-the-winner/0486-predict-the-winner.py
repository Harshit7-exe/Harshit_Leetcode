class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        record = {}
        def maxdiff(left,right):
            if left == right:
                return nums[left]
            if (left, right) in record:
                return record[(left, right)]
            pickleft = nums[left] - maxdiff(left + 1, right)
            pickright = nums[right] - maxdiff(left, right - 1)
            record[(left, right)] = max(pickleft, pickright)
            return record[(left, right)]
        return maxdiff(0, len(nums) - 1) >= 0

        