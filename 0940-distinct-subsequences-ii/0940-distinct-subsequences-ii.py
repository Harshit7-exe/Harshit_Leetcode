class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        letter_count = [0] * 26 
        current_total = 0
        
        for char in s:
            idx = ord(char) - ord('a')
            new_subsequences = (current_total + 1) % MOD
            net_added = (new_subsequences - letter_count[idx] + MOD) % MOD
            current_total = (current_total + net_added) % MOD
            letter_count[idx] = new_subsequences
            
        return current_total

        