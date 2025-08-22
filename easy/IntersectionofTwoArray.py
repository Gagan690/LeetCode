class Solution:
    def intersection(self, nums1, nums2):
        set_num1 , set_num2 = list(set(nums1)) , list(set(nums2))
        result = []
        for i in range(len(set_num1)):
            for j in range(len(set_num2)):
                if set_num1[i] == set_num2[j]:
                    result.append(set_num1[i])
        return result
