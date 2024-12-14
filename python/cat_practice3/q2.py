def remove_unwanted_parentheses(s):
    stack = []
    result = []
    
    # Iterate over each character in the string
    for char in s:
        if char == '(':
            # Push opening parentheses onto the stack
            stack.append(len(result))  # Store the current position in result
            result.append(char)  # Add to result
        elif char == ')':
            if stack:
                # If there's a matching opening parenthesis, pop from stack
                stack.pop()
                result.append(char)  # Add to result
        else:
            result.append(char)  # Add non-parenthesis characters to result

    # Remove any unmatched opening parentheses from the end of the result
    while stack:
        result.pop(stack.pop())  # Remove the unmatched opening parentheses

    return ''.join(result)

# Input
s = input().strip()
# Output
output = remove_unwanted_parentheses(s)
print(output)