class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            #we gonna counting the bit 
            n = n & (n - 1)
            res += 1
        return res