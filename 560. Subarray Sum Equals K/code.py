class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0 : 1}

        prefixSum = 0
        answer = 0

        for n in nums:
            prefixSum += n
            answer += count.get(prefixSum - k, 0)
            count[prefixSum] = count.get(prefixSum , 0) + 1

        return answer