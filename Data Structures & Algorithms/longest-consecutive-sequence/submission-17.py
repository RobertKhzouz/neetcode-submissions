class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        longest = 1
        for num in numSet:
            longest_tmp = 1
            if num - 1 not in numSet:

                check = num + 1
                while check in numSet:
                    check += 1
                    longest_tmp += 1

                if longest_tmp > longest:
                    longest = longest_tmp
        return longest