# Leetcode https://leetcode.com/problems/basic-calculator
# Notes: assumption, " "has no consequence on the expression, evaluating bracket expressions can be optimized
# JIRA: https://sde2.atlassian.net/browse/UB-41

class Solution:
    # O(nlogn) Time | O(1) Space, where n is length of s
    def calculate(self, s: str) -> int:
        return self.calculateHelper(s, 0, len(s) - 1)
        
    def calculateHelper(self, string, start, end):
        result = 0
        isAdd = True
        isSubtract = False
        number = ""
        isDigitFound = False
        while start <= end:
            char = string[start]
            if char in ' +-()' and isDigitFound:
                isDigitFound = False
                integer = int(number)
                number = ""
                if isAdd:
                    result += integer
                if isSubtract:
                    result -= integer
                isAdd = True
                isSubtract = False
            if char == ' ':
                start += 1
                continue
            elif char == "+":
                isAdd = True
                isSubtract = False
            elif char == "-":
                isAdd = False
                isSubtract = True
            elif char == '(':
                endCharIdx = self.getClosingBracketIdx(string, start + 1, end)
                integer = self.calculateHelper(string, start + 1, endCharIdx - 1)
                if isAdd:
                    result += integer
                if isSubtract:
                    result -= integer
                start = endCharIdx
            else:
                isDigitFound = True
                number += char
            start += 1
        if len(number) != 0:
            integer = int(number)
            if isAdd:
                result += integer
            if isSubtract:
                result -= integer
        return result
    
    def getClosingBracketIdx(self, string, start, end):
        stack = ['(']
        for index in range(start, end + 1):
            char = string[index]
            if char == ')':
                stack.pop()
                if len(stack) == 0:
                    return index
            elif char == '(':
                stack.append('(')
        return  
