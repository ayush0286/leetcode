# Leetcode https://leetcode.com/problems/add-digits/
# Notes: convert each carry to a digit
# JIRA: https://sde2.atlassian.net/browse/UB-62

class Solution:
    # O(1) Time | O(1) Space
    def addDigits(self, num: int) -> int:
        string = str(num)
        carry = 0
        for digit in reversed(string):
            carry += int(digit)
            if carry >= 10:
                carry = self.compressNumber(carry)
        return carry


    def compressNumber(self, number):
        compress = 0
        while number >= 10:
            compress += number // 10
            compress += number % 10
            number = compress
            compress = 0
        return number
