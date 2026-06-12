from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_letters = defaultdict(int)
        t_letters = defaultdict(int)

        for s_letter, t_letter in zip(s, t):
            s_letters[s_letter] += 1
            t_letters[t_letter] += 1

        return s_letters == t_letters