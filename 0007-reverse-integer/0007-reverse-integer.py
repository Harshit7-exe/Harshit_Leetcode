class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1
        rev = 0
        x = abs(x)
        max_val = 2**31 - 1
        while x:
            digit = x % 10
            x //= 10
            if rev > max_val //10:
                return 0
            rev = rev * 10 + digit
        return sign * rev


        