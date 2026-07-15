class Solution:
    def isValid(self, s: str) -> bool:

        def isClosing(c):
            return True if c in [")", "}", "]"] else False

        if len(s) % 2 != 0:
            return False

        mapping = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        stack = []

        for character in s:

            if not isClosing(character):
                stack.append(character)
            else:
                if len(stack) == 0 or mapping[stack.pop()] != character:
                    return False

        if len(stack) > 0:
            return False

        return True