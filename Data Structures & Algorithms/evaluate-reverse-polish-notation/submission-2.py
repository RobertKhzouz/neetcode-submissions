class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        def is_operator(s: str):
            return s in {"+", "-", "*", "/"}

        for token in tokens:

            if is_operator(token):
                match token:
                    case "+":
                        stack.append(stack.pop() + stack.pop())
                    case "-":
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(b - a)
                    case "*":
                        stack.append(stack.pop() * stack.pop())
                    case "/":
                        a = stack.pop()
                        b = stack.pop()
                        stack.append(int(b / a))
            else:
                stack.append(int(token))
            print(stack)

        return stack.pop()