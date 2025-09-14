class Solution:
    def intersect(self, nums1, nums2):
        set_num1 , set_num2 = list(nums1) , list(nums2)
        result = []
        for i in set_num1:
            if i in set_num2:
                result.append(i)
                set_num2.remove(i)
        return result
