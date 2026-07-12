class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        for i in nums:
            f[i] = f.get(i, 0) + 1
        max_f = max(f.values())
        b = [[] for i in range(max_f+1)]
        for n, c in f.items():
            b[c].append(n)
        a = []
        for i in range(max_f, 0, -1):
            for n in b[i]:
                a.append(n)
                if len(a) == k:
                    return a
        return a