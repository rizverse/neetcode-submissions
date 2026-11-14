class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        di =  {}
        for i in range(len(nums)):
            di[nums[i]] = i
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in di and di[rem] != i:
                return [i,di[rem]]
