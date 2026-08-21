class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # 1. Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Handle sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Build number
        num = 0

        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # 4. Check overflow
            if num > 214748364 or (
                num == 214748364 and digit > 7
            ):
                return 2147483647 if sign == 1 else -2147483648

            num = num * 10 + digit
            i += 1
        return sign * num