class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))

            else:
                if token == "+":
                    stack.append(stack.pop() + stack.pop())
                elif token == "-":
                    b, a= stack.pop(), stack.pop()
                    stack.append(a - b)
                elif token == "*":
                    stack.append(stack.pop() * stack.pop())
                else:
                    b, a = stack.pop(), stack.pop()
                    stack.append(int(a / b))
        return stack.pop()