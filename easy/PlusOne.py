class Solution:
    def plusOne(self, digits):
        lst_to_num = int(''.join(map(str,digits)))
        lst_to_num += 1
        num_to_lst = list(map(int,str(lst_to_num)))
        return num_to_lst
