def parentheses_balancer(p):
    left = 0
    right = 0
    for i in p:
        if i == '(':
            left = left +1
        if i == ')':
            right =  right + 1
        if right > left:
            return "Unbalanced"
    if left > right or right > left:
        return "Unbalanced"
    else:
        return "Balanced"

p = '())()(()'
print(parentheses_balancer(p))

p = '(()())()'
print(parentheses_balancer(p))

    
        
        
        
    