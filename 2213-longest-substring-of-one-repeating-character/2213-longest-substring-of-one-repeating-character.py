class Node:
    def __init__(self, size=0):
        self.max_len = 0
        self.pref_len = 0
        self.suff_len = 0
        self.size = size

class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        self.s = list(s)
        self.tree = [Node() for _ in range(4 * self.n)]
        self.build(1, 0, self.n - 1)

    # Indented by 4 spaces to place inside SegmentTree
    def merge(self, left, right, mid):
        parent = Node(left.size + right.size)
        parent.max_len = max(left.max_len, right.max_len)
        parent.pref_len = left.pref_len
        parent.suff_len = right.suff_len

        # If adjacent characters match, they can bridge across the children boundary
        if self.s[mid] == self.s[mid + 1]:
            parent.max_len = max(parent.max_len, left.suff_len + right.pref_len)
            if left.pref_len == left.size:
                parent.pref_len = left.size + right.pref_len
            if right.suff_len == right.size:
                parent.suff_len = right.size + left.suff_len
                
        return parent

   
    def build(self, node, start, end):
        if start == end:
            self.tree[node].max_len = 1
            self.tree[node].pref_len = 1
            self.tree[node].suff_len = 1
            self.tree[node].size = 1
            return

        mid = (start + end) // 2
        self.build(2 * node, start, mid)
        self.build(2 * node + 1, mid + 1, end)
        self.tree[node] = self.merge(self.tree[2 * node], self.tree[2 * node + 1], mid)

   
    def update(self, node, start, end, idx, ch):
        if start == end:
            self.s[idx] = ch
            return

        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node, start, mid, idx, ch)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, ch)
            
        self.tree[node] = self.merge(self.tree[2 * node], self.tree[2 * node + 1], mid)

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        st = SegmentTree(s)
        lengths = []
        
        for ch, idx in zip(queryCharacters, queryIndices):
            st.update(1, 0, st.n - 1, idx, ch)
           
            lengths.append(st.tree[1].max_len)
            
        return lengths
