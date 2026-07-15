class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        mapping = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        stack = []

        for character in s:

            if character in mapping:
                stack.append(character)
            else:
                if len(stack) == 0 or mapping[stack.pop()] != character:
                    return False

        if len(stack) > 0:
            return False

        return True