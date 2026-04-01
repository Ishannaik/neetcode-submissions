class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        nums3 = []
        for i in nums1:
            nums3.append(i)
            print(nums3)
        for j in nums2:
            nums3.append(j)
            print(nums3)
        nums3.sort()
        print(nums3)
        nums3 = nums1 + nums2
        nums3.sort()
        n = len(nums3)
        mid = n // 2

        if n % 2:  # odd — single middle element
            return nums3[mid]
        else:      # even — average of two middle elements
            return (nums3[mid - 1] + nums3[mid]) / 2