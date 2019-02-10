import math

# Implementing stack data structure using a class
class Stack:
     def __init__(self):
         self.items = []

     def is_empty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

# Checks if c is an operand
def is_operand(c):
    return c.isalpha() or c.isdigit()

# Checks if c is an operator
def is_operator(c):
    return c == '+' or c == '-' or c == '*' or c == '/' or c == '%' or c == '^'

# Checks if c has right order of precedence
def has_right_precedence(c):
    return c == '^'

# Provides the precedence of an operator
def get_operator_precedence(c):
    return {
        '^': 1,
        '*': 2,
        '/': 2,
        '%': 2,
        '+': 3,
        '-': 3,
    } [c]

# Compares the precedence of c1 and c2
def has_higher_precedence(c1, c2):
    if get_operator_precedence(c1) < get_operator_precedence(c2):
        return True
        
    elif get_operator_precedence(c1) == get_operator_precedence(c2):
        return not has_right_precedence(c1)
        
    return False

# Converts an expression to postfix
def postfix(expression):
    result = ""
    s = Stack()
    
    for c in expression:
        
        if (c == ' '):
            continue
            
        elif is_operand(c):
            result += c
            result += ' '
            
        elif is_operator(c):
            while (not s.is_empty()) and s.peek() != '(' and has_higher_precedence(s.peek(), c):    # While the stack expression has higher precedence than the current operator
                result += s.pop()                                                                   # Keep popping
                result += ' '
                
            s.push(c)                                                                               # Pushing the operator at the end of iteration
        
        elif c == '(':
            s.push(c)
            
        elif c == ')':
            while (not s.is_empty()) and s.peek() != '(':
                result += s.pop()                                                                   # Iterate and add to the expression till opening parenthesis is detected
                result += ' '
                
            s.pop()
        
    while not s.is_empty():
        result += s.pop()
        result += ' '
        
    return result   

# Evaluates a postfix expression
def evaluate_postfix(expression):
    s = Stack()

    for c in expression:
        if c == ' ':
            continue
        
        elif c.isdigit():
            s.push(int(c))
            
        elif is_operator(c):
            n1 = s.pop()
            n2 = s.pop()
                
            n3 = {
                '+': n2 + n1,
                '-': n2 - n1,
                '/': n2 / n1,
                '*': n2 * n1,
                '%': n2 % n1,
                '^': pow(n2, n1)
                } [c]
                
            s.push(n3)
            
        else:
            print c
            return None
            
    return s.pop()

infix_expression = raw_input("Enter Infix Expression to be converted into Postfix\n>> ")
print "Your expression in postfix format is: -"
print postfix(str(infix_expression))

postfix_expression = raw_input("Enter the postfix expression to be evaluated\n>> ")
print "Your result is: - "
print evaluate_postfix(postfix_expression)
