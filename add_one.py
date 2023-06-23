class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = "".join(str(i) for i in digits)
        b = int(a) + 1

        return [int(i) for i in str(b)]


#   2nd solution

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10

        if carry:
            digits.insert(0, carry)

        return digits
