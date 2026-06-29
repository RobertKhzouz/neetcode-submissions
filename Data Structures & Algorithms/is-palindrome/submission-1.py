class Solution:
    def isPalindrome(self, s: str) -> bool:

        l_pos = 0
        r_pos = len(s) - 1
        while l_pos < r_pos:
            print(l_pos, r_pos)

            if not s[l_pos].isalnum():
                l_pos += 1
                continue
            if not s[r_pos].isalnum():
                r_pos -= 1
                continue

            if s[l_pos].lower() != s[r_pos].lower():
                return False

            l_pos += 1
            r_pos -= 1
            
        return True