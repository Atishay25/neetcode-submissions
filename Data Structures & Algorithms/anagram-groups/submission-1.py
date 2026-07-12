class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = dict()
        res = []
        for s in strs:
            a = [0]*26
            for i in s:
                a[ord(i) - 97] += 1
            a_ = ".".join(map(str, a)) 
            if a_ in h.keys():
                res[h[a_]].append(s)
            else:
                res.append([s])
                h[a_] = len(res) - 1
        return res