class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = list()
        tempLength = len(temperatures)
        distanceStack = list()

        for i in (range(tempLength)):
            continueNext = False
            if i == tempLength - 1:
                results.append(0)
                break
            counter = i + 1
            while (temperatures[i] >= temperatures[counter]):
                distanceStack.append(temperatures[counter])
                counter += 1
                if counter > tempLength - 1:
                    distanceStack.clear()
                    results.append(0)
                    continueNext = True
                    break
            if continueNext == True:
                continue
            results.append(len(distanceStack) + 1)
            distanceStack.clear()
        return results