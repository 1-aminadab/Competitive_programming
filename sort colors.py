class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        colors = [0,1,2]
        count = 0
        for i in range(len(colors)):
            for j in range(len(nums)):       
                if nums[j] == colors[i]:
                    nums[count], nums[j] =nums[j], nums[count]
                    count += 1
                   

                     
    

     
