class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        numberOfSmallers = []
        count = 0
        for i in range(len(nums)):
            number = nums[i]
            for j in range(len(nums)):
                if number > nums[j]:
                    count += 1

             numberOfSmallers.append(count)
            count = 0
        return  numberOfSmallers
