class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        result = ""
        remaining = sum
        for i in range(num):
            digit = min(9, remaining)
            result += str(digit)
            remaining -= digit
        return result