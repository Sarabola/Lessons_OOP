class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        freq = {}
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1

        result = []
        for num in nums2:
            if freq[num] > 0:
                for _ in range(freq[num]):
                    result.append(num)
        return result
