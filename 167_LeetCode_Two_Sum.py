def two_sum(numbers, target):
    ans = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if(numbers[i] + numbers[j] == target):
                ans.append(i + 1)
                ans.append(j + 1)
    print(ans)


two_sum([-1, 0], -1)


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]  # 1-based indexing
            elif current_sum < target:
                left += 1
            else:
                right -= 1
