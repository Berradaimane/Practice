class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic ={}
        for i in range (len(nums)):
         diff=target-nums[i]
         if diff in dic:
            return [dic[diff],i]
         else:
            dic[nums[i]]=i
                


        