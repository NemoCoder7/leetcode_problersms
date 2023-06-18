class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.l1 = l1
        self.l2 = l2

        delta = abs(len(l1) - len(l2))

