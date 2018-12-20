class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)  # put both arrays together
        x = sorted(nums1)  # sort so we can easily pick out the median
        if len(x) % 2 == 0:
            # if there are an even number of elements, the median is the avg of the 2 middle nums
            return (x[int((len(x) / 2) - .5)] + x[int((len(x) / 2) + .5)]) / 2
        else:
            # if there are an odd number of elements, the median is the middle number
            return x[int((len(x) / 2) - .5)]