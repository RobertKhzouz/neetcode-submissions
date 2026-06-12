class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countDict = {}
        keys = countDict.keys()
        for key in nums:
            if key in keys:
                return True
            else:
                countDict[key] = 1
                keys = countDict.keys()
        return False