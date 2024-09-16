class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if target - numbers[i] == numbers[i]:
                if numbers.count(target - numbers[i]) > 1:
                    a = numbers[i]
                    numbers[i] = -10000
                    if target - a in numbers:
                        return [i + 1, numbers.index(target - a) + 1]

            else:
                if target - numbers[i] in numbers:
                    return [i + 1, numbers.index(target - numbers[i]) + 1]
