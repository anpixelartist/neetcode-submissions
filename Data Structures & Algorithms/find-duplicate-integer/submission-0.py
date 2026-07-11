class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow1 = 0

        while True:
            fast = nums[nums[fast]]
            slow1 = nums[slow1]

            if fast==slow1:
                break

        slow2 = 0

        while True:
            slow1 = nums[slow1]
            slow2 = nums[slow2]

            if slow1==slow2:
                break
        return slow1                

        