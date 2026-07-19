class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_ocr = {}
        for i, ch in enumerate(s):
            last_ocr[ch] = i
        for i, ch in enumerate(s):
            if ch in seen:
                continue
            while stack and stack[-1] > ch and last_ocr[stack[-1]] > i:
                seen.remove(stack.pop())
            stack.append(ch)
            seen.add(ch)
        return "".join(stack)