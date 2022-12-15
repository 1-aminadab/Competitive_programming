class Solution(object):
    def targetIndices(self, nums, target):
        outPut = []
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j+1] =                   
                    nums[j+1], nums[j]

        for i in range(len(nums)):
            if target == nums[i]:
                outPut.append(i)
        return outPut
