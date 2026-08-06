class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            prod = 1
            curr = n
            while curr > 0:
                prod *= curr % 10
                curr //= 10
            if prod % t == 0:
                return n
            n += 1
