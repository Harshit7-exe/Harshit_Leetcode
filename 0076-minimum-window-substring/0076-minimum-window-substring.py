from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = {}

        required = len(need)
        formed = 0

        left = 0
        min_len = float("inf")
        min_start = 0

        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            # This character requirement has just been satisfied
            if ch in need and window[ch] == need[ch]:
                formed += 1

            # Current window is valid
            while formed == required:
                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                # Remove left character
                left_ch = s[left]
                window[left_ch] -= 1

                # Window is no longer valid
                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[min_start:min_start + min_len]
        