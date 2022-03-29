class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_of_nums = set(nums)
        longest = 0
        
        for num in set_of_nums:
            if num-1 in set_of_nums: continue # this ensures that we only start from the least significant number of every subsequence
            new_length = 1
            current_num = num
            while current_num + 1 in set_of_nums:
                current_num += 1
                new_length += 1
            longest = max(longest, new_length)
        return longest