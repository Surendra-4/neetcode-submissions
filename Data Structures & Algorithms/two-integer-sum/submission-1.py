class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        n = len(nums)
        for i in range(0, n):
            for j in range (i + 1, n):
                if nums[i] + nums[j] == target:
                    if i < j:
                        output.append(i)
                        output.append(j)
                        break
                    elif i > j:
                        output.append(j)
                        output.append(i)
                        break
        return output