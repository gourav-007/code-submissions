class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        hash_map={}

        for i in range(0,n):
            hash_map[nums[i]] = hash_map.get(nums[i],0)+1

        for k,v in hash_map.items():
            if v>n//2:
                return k