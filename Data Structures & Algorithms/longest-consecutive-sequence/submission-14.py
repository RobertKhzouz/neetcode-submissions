class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        string = None
        negString = None
        for num in nums:

            length = len(string) if string else 0
            negLength = len(negString) if negString else 0

            if num >= 0:
                if not string:
                    string = "0" + "0" * (num - length)
                elif length <= num:
                    string += "0" * ((num - length + 1) * 2)

                if string[num] == "0":
                    string = string[:num] + "1" + string[num + 1:]
            else:
                if not negString:
                    negString = "0" * (abs(num) - negLength)
                elif negLength <= abs(num):
                    negString += "0" * ((abs(num) - negLength) * 2)

                if negString[abs(num) - 1] == "0":
                    negString = negString[:abs(num) - 1] + "1" + negString[abs(num):]

        longest = 0
        current = 0
        if negString:
            for c in reversed(negString):
                if c == "1":
                    current += 1
                else:
                    if current > longest:
                        longest = current
                    current = 0
        if string:
            for c in string:
            
                if c == "1":
                    current += 1
                else:
                    if current > longest:
                        longest = current
                    current = 0
        if current > longest:
            longest = current;

        return longest