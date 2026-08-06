class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mincoins = [float("inf")] * (amount + 1)
        mincoins[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    mincoins[i] = min(mincoins[i], mincoins[i - coin] + 1)
        if mincoins[amount] == float("inf"):
            return -1
        return mincoins[amount]


        