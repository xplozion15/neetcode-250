class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numbers = nums.copy()
        for num in nums:
            numbers.append(num)
        return numbers
