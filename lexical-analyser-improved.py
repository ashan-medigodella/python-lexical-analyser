# D/BCS/21/0002
# WMAU Medigodella
# Automata Theory Assignment 02

# Token types
INTEGER = 'INTEGER'  
PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVIDE = 'DIVIDE'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
UNKNOWN = 'UNKNOWN'
END_OF_INPUT = 'END_OF_INPUT'

# Valid operators
VALID_OPERATORS = {
  '+': PLUS,
  '-': MINUS,
  '*': MULTIPLY,
  '/': DIVIDE
}

# PDA states
STATE_START = 'start'
STATE_OPEN_PARENS = 'open parens'  
STATE_CLOSED_PARENS = 'closed parens'

# Stack for balancing parens
paren_stack = []

def lexer(input_text):
    tokens = []
    position = 0
    
    while position < len(input_text):
        char = input_text[position]
        
        if char == ' ':
            position += 1
            continue
        
        if char.isdigit():
            # Integer token
            start = position
            while position < len(input_text) and input_text[position].isdigit():
                position += 1
            tokens.append((INTEGER, input_text[start:position]))
        
        elif char in VALID_OPERATORS:
            # Operator token
            tokens.append((VALID_OPERATORS[char], char))
            position += 1
        
        elif char == '(':
            tokens.append((LPAREN, char))
            position += 1
        
        elif char == ')':
            tokens.append((RPAREN, char))
            position += 1
            
        else:
            # Unknown token 
            tokens.append((UNKNOWN, char))
            position += 1
    
    tokens.append((END_OF_INPUT, ''))    
    return tokens

def check_parens(token_list):
  state = STATE_START

  for token in token_list:
    token_type, token_value = token

    if token_type == LPAREN:
      paren_stack.append(token)
      state = STATE_OPEN_PARENS

    elif token_type == RPAREN:
      if not paren_stack:
        return False  # Unbalanced
      paren_stack.pop()
      state = STATE_CLOSED_PARENS

  return state == STATE_CLOSED_PARENS and not paren_stack

def parse(input_str):
  tokens = lexer(input_str)
  print(tokens)

  if check_parens(tokens) and not paren_stack:
     print("Expression is balanced")
  else:
    print("Expression is unbalanced")

input_expr = "(2 * (3 + 4)) / 5)"
parse(input_expr)