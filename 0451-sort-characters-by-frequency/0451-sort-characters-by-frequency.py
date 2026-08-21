class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) +1
        sorted_char = sorted(freq, key = freq.get, reverse = True)
        result = ""
        for ch in sorted_char:
            result += ch*freq[ch]
        return result