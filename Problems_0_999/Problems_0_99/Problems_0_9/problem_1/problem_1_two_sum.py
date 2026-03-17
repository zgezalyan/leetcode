from typing import List

class Solution:
    def twoSum_simple(self, nums: List[int], target: int) -> List[int]:
        for first_index in range(len(nums)):
            for second_index in range(first_index + 1, len(nums)):
                # print("Sum of {0} and {1} is {2}".format(nums[first_index], nums[second_index], nums[first_index] + nums[second_index]))
                if nums[first_index] + nums[second_index] == target:
                    return [first_index, second_index]
        return []
    def twoSum_optimized(self, nums: List[int], target: int) -> List[int]:
        """
        Improved version of twoSum using a hash map.
        Runs in O(n) time and O(n) extra space.
        """
        value_to_index = {}
        for current_index, value in enumerate(nums):
            complement = target - value
            if complement in value_to_index:
                return [value_to_index[complement], current_index]
            value_to_index[value] = current_index
        return []
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}
        for index, value in enumerate(nums):
            dif = target - value
            if dif in index_dict:
                return [index_dict[dif], index]
            index_dict[value] = index
        return []
