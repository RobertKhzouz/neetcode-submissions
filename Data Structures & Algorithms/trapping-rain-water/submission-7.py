class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        if n < 2:
            return 0

        prefixes = [0] * n
        suffixes = [0] * n
        prefixes[0] = height[0]
        suffixes[n - 1] = height[n - 1]

        for i in range(1, n):
            prefixes[i] = max(prefixes[i - 1], height[i])

        for i in range(n - 2, -1, -1):
            suffixes[i] = max(suffixes[i + 1], height[i])

        total = 0
        for i in range(n):
            total += min(prefixes[i], suffixes[i]) - height[i]
            print(f"{total} -> ({prefixes[i]} or {suffixes[i]}) - {height[i]}")

        return total


