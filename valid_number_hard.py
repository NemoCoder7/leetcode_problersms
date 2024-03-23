class Solution:
    def isNumber(self, s: str) -> bool:
        self.s = s.strip()

        if not self.s:
            return False

        seen_digit = False
        seen_dot = False
        seen_e = False

        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char == ".":
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            elif char in ("e", "E"):
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit = False
            elif char in ("+", "-"):
                if i > 0 and self.s[i - 1] not in ("e", "E"):
                    return False
            else:
                return False

        return seen_digit


# Test cases
valid_numbers = [
    "2",
    "0089",
    "-0.1",
    "+3.14",
    "4.",
    "-.9",
    "2e10",
    "-90E3",
    "3e+7",
    "+6e-1",
    "53.5e93",
    "-123.456e789",
]
invalid_numbers = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

for num in valid_numbers:
    number = Solution()
    print(number.isNumber(num))

for num in invalid_numbers:
    print(number.isNumber(num))
