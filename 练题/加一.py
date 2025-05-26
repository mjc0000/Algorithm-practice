class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        the_number = 0
        for i in range(n):
            the_number += 10 ** i * digits[-i - 1]
        the_number += 1
        new_digits = str(the_number)
        new_new_digits = []
        for digit in new_digits:
            new_new_digits.append(int(digit))
        return new_new_digits