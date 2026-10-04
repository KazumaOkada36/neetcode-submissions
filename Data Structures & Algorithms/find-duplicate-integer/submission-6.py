class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bro = len(nums)
        slow, fast = 0, 0
        a = True
        while a:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                bruh = slow
                a = False
        
        chill = 0
        while bruh != chill:
            chill = nums[chill]
            bruh = nums[bruh]
            if chill == bruh:
                return chill



        