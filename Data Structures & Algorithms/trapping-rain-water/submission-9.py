class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        prefixes = [0] * n
        suffixes = [0] * n

        prefixes[0] = height[0]
        suffixes[n - 1] = height[n - 1]

        for l in range(1, n):
            prefixes[l] = max(prefixes[l - 1], height[l])

        for r in range(n - 2, -1, -1):
            suffixes[r] = max(suffixes[r + 1], height[r])

        area = 0
        for i in range(n):
            area += min(prefixes[i], suffixes[i]) - height[i]

        return area