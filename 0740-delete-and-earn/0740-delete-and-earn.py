
def f(idx, points, mx, memo):
    if idx > mx:
        return 0
    if idx in memo:
        return memo[idx]

    take = points[idx] + f(idx + 2, points, mx, memo)
    skip = f(idx + 1, points, mx, memo)

    memo[idx] = max(take, skip)
    return memo[idx]


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        mx = max(nums)

        points = [0] * (mx + 1)
        for num in nums:
            points[num] += num

        memo = {}
        return f(0, points, mx, memo)