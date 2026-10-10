class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):

        k = k1 + k2

        freq = [0] * 100001
        max_diff = 0

        for a, b in zip(nums1, nums2):
            d = abs(a - b)
            freq[d] += 1
            max_diff = max(max_diff, d)

        
        for d in range(max_diff, 0, -1):

            if k == 0:
                break

            count = freq[d]

            if count == 0:
                continue

            
            if k >= count:

                freq[d] -= count
                freq[d - 1] += count

                k -= count

            else:
                
                full = k // count
                remainder = k % count

                freq[d] -= count

               
                freq[d - full] += count - remainder

               
                freq[d - full - 1] += remainder

                k = 0
                break

        ans = 0

        for d in range(1, max_diff + 1):
            ans += freq[d] * d * d

        return ans