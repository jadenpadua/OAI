class Solution:
    def isValid(self, s: str) -> bool:
        ht = {")": "(", "}": "{", "]": "["}
        closing = ")}]"
        stack = []
        for i in range(len(s)):
            # case where stack is empty and we are at closing char
            if len(stack) == 0 and s[i] in closing:
                return False
            # case where we check if closing char matches popped stack char
            elif s[i] in closing:
                popped = stack.pop()
                if popped != ht[s[i]]:
                    return False
            # if its open we simply push to stack
            else:
                stack.append(s[i])
        # return true only if stack is resolved and we do not have trailing open chars
        return len(stack) == 0
