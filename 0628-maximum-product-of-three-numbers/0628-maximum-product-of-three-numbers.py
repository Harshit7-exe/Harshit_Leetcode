class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        min1 = min2 = float('inf')
        for n in nums:
            if  n > first:
                third = second
                second = first
                first = n
            elif n > second:
                third = second
                second = n
            elif n > third:
                third = n
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n
            prod1 = first * second * third
            prod2 = first * min1 * min2
            max_prod = max(prod1, prod2)
        return max_prod

