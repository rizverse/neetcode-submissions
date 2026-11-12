class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #creating a set that cannot store duplicates
        #if using java use hashset which uses hash valuesas vlue key pair
        set_Empty = set()
        for i in nums:
            if i in set_Empty:
                return True
            else:
                set_Empty.add(i)
        return False
