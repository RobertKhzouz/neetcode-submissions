class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []

        position, speed = map(list, zip(*sorted(zip(position, speed), reverse=True)))

        for i in range(len(position)):

            time = (target - position[i]) / speed[i]

            if stack and time <= stack[-1]:
                pass
            else:
                stack.append(time)

        return len(stack)