class Solution:
    def eval(self, op, a, b):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(self.eval(token, a, b))
            else:
                stack.append(int(token))
        
        return stack[-1]