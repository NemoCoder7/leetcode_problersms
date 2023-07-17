class Solution(object):
    def letter_combinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        digit_letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        letters_list = [digit_letter_map[digit] for digit in digits]
        combinations = [''.join(combination) for combination in product(*letters_list)]

        return combinations
