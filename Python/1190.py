def reverse_parentheses(s: str) -> str:
    stack = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            start = stack.pop()
           
            s = s[:start] + s[start + 1:i][::-1] + s[i + 1:]
    
    result = ''.join([char for char in s if char not in '()'])
    return result
