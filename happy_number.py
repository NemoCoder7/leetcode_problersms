class Solution(object):
    def isHappy(self, n):
        visited = set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return True
