class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s:
            if letter == '(':
                stack.append(')')
            elif letter == "{":
                stack.append("}")
            elif letter == "[":
                stack.append("]")
            else:
                if len(stack) > 0:
                    bruh = stack.pop()
                    if letter != bruh:
                        return False
                else:
                    return False
        if len(stack)> 0:
            return False
        return True
        