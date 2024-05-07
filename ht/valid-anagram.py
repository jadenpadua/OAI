class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # trivial case where len(s) != len(t) so simply return false
        if len(s) != len(t):
            return False
        s_counter, t_counter = {}, {}
        # len(s) == len(t) so loop through any arbitrary string
        for i in range(len(s)):
            s_counter[s[i]] = s_counter.get(s[i], 0) + 1
            t_counter[t[i]] = t_counter.get(t[i], 0) + 1
        # if counters are equal then we arrive to an anagram
        return s_counter == t_counter
