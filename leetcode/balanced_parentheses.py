class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) == 0: return True
        
        stack = []
        
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif char == ")" and (len(stack)==0 or stack[-1] != "(" ):
                return False
            elif char == "}" and (len(stack)==0 or stack[-1] != "{" ):
                return False
            elif char == "]" and (len(stack)==0 or stack[-1] != "[" ):
                return False
            else:
                stack.pop()
                
        if len(stack)>0:
            return False
        
        return True
    def valid_parentheses_with_dict(self,s):
        # if there are odd no of parenthesis then it can't be true
        if len(s)%2 == 1:
            return False
        stack = []
        braces = {"{":"}","(":")","[":"]"}

        for c in s:
            if c in braces:
                stack.append(c)
            elif len(stack)!=0 and c == braces[stack[-1]]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
        