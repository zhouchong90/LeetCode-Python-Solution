class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        
        a,b,c,d = 0, len(nums)-1, 0, len(nums)-1
        
        while a<b:
            mid = a+((b-a)>>1)
            if target<=nums[mid]:
                b = mid
            else:
                a = mid+1
        
        if nums[a]!=target:
            return [-1,-1]
                
        while c<d:
            mid = c+((d-c+1)>>1)
            if target<nums[mid]:
                d = mid-1
            else:
                c = mid
                
        return [a,c]