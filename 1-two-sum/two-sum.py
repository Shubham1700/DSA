class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for index, num in enumerate(nums): # gives both index and value
            rem = target - num

            if rem in my_dict:
                return [my_dict[rem], index]# rem's stored index, current index

            my_dict[num] = index # store number's index
        