class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{","]":"["}
        for i in s:
            if i in "([{":
                stack.append(i)
            elif i in ")]}":
                    if stack == []:
                        return False
                    elif stack[-1] == mapping[i]:
                        stack.pop()
                    else:
                        return False
            else:
                return False
        if stack == []:
            return True
        else:
            return False


        