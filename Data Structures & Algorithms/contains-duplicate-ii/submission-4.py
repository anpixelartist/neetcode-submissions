class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = i+1

        while j<len(nums):
            j = i+1
            while j <= i+k:
                if nums[i]==nums[j]:
                    return True
                else:
                    j+=1
            i+=1
            


        return False
        
        