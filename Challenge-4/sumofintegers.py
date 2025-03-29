class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        bitshortner = 0xffffffff

        while(b & bitshortner) > 0:
            carry = (a&b)<<1
            a =(a^b)
            b = carry
        return (a&bitshortner) if b > 0 else a