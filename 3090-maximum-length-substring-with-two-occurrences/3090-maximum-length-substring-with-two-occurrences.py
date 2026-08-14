class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counts = Counter()
        max_len = 0
        l = 0
        
        for r in range(len(s)):
            counts[s[r]] += 1
            
            
            while counts[s[r]] > 2:
                counts[s[l]] -= 1
                l += 1
                
            max_len = max(max_len, r - l + 1)
            
        return max_len