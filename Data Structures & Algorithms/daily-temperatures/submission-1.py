class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        output = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                value, index = stack.pop()
                output[index] = i - index

            stack.append((temp, i))

        return output