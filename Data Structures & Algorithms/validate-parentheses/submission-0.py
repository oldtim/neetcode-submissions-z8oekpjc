class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        uppercase = {'(','{','['}
        lowercase = {')','}',']'}
        for char in s:
            if char in uppercase:
                stack.append(char)
            if char in lowercase:
                if stack:
                    temp = stack.pop()
                else:
                    return False
                if temp == '(' and char != ')':
                    return False
                if temp == '{' and char != '}':
                    return False
                if temp == '[' and char != ']':
                    return False
        if stack:
            return False
        else:
            return True


        