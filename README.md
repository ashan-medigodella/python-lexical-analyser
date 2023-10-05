# python-lexical-analyser

## lexical analyser created with python

### Tokenizer

The lexer function takes an input string and breaks it into a list of tokens. It supports the following token types:

- `INTEGER` - a sequence of digits
- `PLUS` - the '+' character
- `MINUS` - the '-' character
- `MULTIPLY` - the '\*' character
- `DIVIDE` - the '/' character
- `LPAREN` - a left parenthesis '('
- `RPAREN` - a right parenthesis ')'
- `UNKNOWN` - any other single character
- `END_OF_INPUT` - marks end of input
It skips over any whitespace and extracts integers, operators, and parentheses as tokens.

### Parser

The parser utilizes a pushdown automaton (PDA) to check for balanced parentheses in the expression.

- STATE_START is the starting state
- STATE_OPEN_PARENS is entered when a '(' token is seen
- STATE_CLOSED_PARENS is entered when a ')' token is seen

paren_stack is used to push '(' tokens and pop ')' tokens.

check_parens() checks whether the paren_stack is empty after processing all tokens, which indicates balanced parens.

parse() calls the lexer, checks parentheses using the PDA, and prints if the expression is balanced or not.

### Usage

Call parse() passing an arithmetic expression string to tokenize it, check for balanced parentheses, and print the result.

For example:

```python
input_expr = "(2 \* (3 + 4)) / 5)"
parse(input_expr)
```

This will print "Expression is balanced" since the parentheses are properly balanced.
