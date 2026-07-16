class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        position, speed = map(list, zip(*sorted(zip(position, speed), reverse=True)))
        stack = []
        fleets = 0

        print(position)
        print(speed)

        for i in range(len(position)):

            time = (target - position[i]) / speed[i]
            if stack and time <= stack[-1]:
                pass
            else:
                stack.append(time)

        return len(stack)