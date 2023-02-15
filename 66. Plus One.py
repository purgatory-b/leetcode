# Runtime 40 ms
# Beats   32.76%
# Memory  13.9 MB
# Beats   49.92%


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add_digits = ''
        res_list=[]
        for i in digits:
            add_digits+=str(i)
        res = int(add_digits)+1
        for i in str(res):
            res_list.append(int(i))
        return res_list
