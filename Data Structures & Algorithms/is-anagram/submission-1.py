class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_ = [0]*26
        t_ = [0]*26
        for i in range(len(s)):
            s_[ord(s[i]) - 97] += 1
            t_[ord(t[i]) - 97] += 1
        return "".join(map(str,s_)) == "".join(map(str,t_))