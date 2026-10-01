class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            med = (l+r)//2
            if nums[med] == target:
                return med
            elif nums[med] >= nums[l]:
                if nums[med] > target >= nums[l]:
                    r = med-1
                else:
                    l = med +1
            elif nums[med] <= nums[r]:
                if nums[med] < target <= nums[r]:
                    l = med +1
                else:
                    r = med-1
        return -1


        