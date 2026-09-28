class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for number in tokens:
            if number == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num1+num2))
            elif number == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2-num1))
            elif number == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num1*num2))
            elif number == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2/num1))
            else:
                stack.append(int(number))



        return stack.pop()

        