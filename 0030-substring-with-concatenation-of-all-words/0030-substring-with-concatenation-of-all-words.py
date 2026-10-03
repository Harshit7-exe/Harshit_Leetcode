class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        wordLen = len(words[0])
        wordCount = len(words)
        totalLen = wordLen * wordCount
        if totalLen > len(s):
            return []
        required = Counter(words)  
        result = []
        for offset in range(wordLen):
            left = offset
            right = offset
            current = {}
            count = 0
            while right + wordLen <= len(s):
                word = s[right:right + wordLen]
                right += wordLen
                if word in required:
                    current[word] = current.get(word, 0) + 1
                    count += 1

                    while current[word] > required[word]:
                        leftWord = s[left:left + wordLen]
                        current[leftWord] -= 1
                        left += wordLen
                        count -= 1

                    if count == wordCount:
                        result.append(left)

                        leftWord = s[left:left + wordLen]
                        current[leftWord] -=1
                        left += wordLen
                        count -= 1
                else:
                    current.clear()
                    count = 0
                    left = right
        return result
        