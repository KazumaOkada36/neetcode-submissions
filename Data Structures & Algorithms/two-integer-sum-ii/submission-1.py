class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, i = 0, len(numbers) - 1
        while s <= i:
            if numbers[s] + numbers[i] == target:
                return [s+1, i+1]
            elif numbers[s] + numbers[i] < target:
                s += 1
            elif numbers[s] + numbers[i] > target:
                i -= 1
        