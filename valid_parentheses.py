class Solution(object):
    def is_valid(self, s):
        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in brackets:
                stack.append(char)
            elif stack and char == brackets[stack[-1]]:
                stack.pop()
            else:
                return False

        return not stack


class Solution2(object):
    def is_valid(self, s):
        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in brackets:
                stack.append(char)
            elif stack and brackets.get(stack[-1]) == char:
                stack.pop()
            else:
                return False

        return len(stack) == 0
