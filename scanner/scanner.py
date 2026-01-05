from .token_type import TokenType
from .token import Token

class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

    def is_at_end(self):
        if self.current == len(self.source):
            return True
        else:
            return False
        

    def advance(self):
        current_char = self.source[self.current]
        self.current += 1
        return current_char
    

    def peek(self):
        if self.is_at_end():
            return '\0'
        else:
            return self.source[self.current]
        

    def peek_next(self):
        if self.current + 1 >= len(self.source):
            return '\0'
        else:
            return self.source[self.current + 1]
        
    
    def match(self, char):
        if self.is_at_end():
            return False
        if self.source[self.current] == char:
            self.current += 1
            return True
        else:
            return False


    def add_token(self, token_type: TokenType, literal = None):
        lexeme = self.source[self.start : self.current]
        token = Token(token_type, lexeme, literal, self.line)
        self.tokens.append(token)


    def scan_token(self):
        current_char = self.advance()

        if current_char == "(":
            self.add_token(TokenType.LEFT_PAREN)
        elif current_char == ")":
            self.add_token(TokenType.RIGHT_PAREN)
        elif current_char == "{":
            self.add_token(TokenType.LEFT_BRACE)
        elif current_char == "}":
            self.add_token(TokenType.RIGHT_BRACE)
        elif current_char == ",":
            self.add_token(TokenType.COMMA)
        elif current_char == ".":
            self.add_token(TokenType.DOT)
        elif current_char == "-":
            self.add_token(TokenType.MINUS)
        elif current_char == "+":
            self.add_token(TokenType.PLUS)
        elif current_char == ";":
            self.add_token(TokenType.SEMICOLON)
        elif current_char == "*":
            self.add_token(TokenType.STAR)
        

    
    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens


        