class Solution:
    def maxProduct(self, n: int) -> int:
        largest_digit = 0
        second_largest = 0
        while n > 0:
            digit = n % 10 
            if digit > largest_digit:
                second_largest = largest_digit
                largest_digit  = digit
            elif digit > second_largest:
                second_largest = digit
            n //= 10
        return largest_digit * second_largest
        