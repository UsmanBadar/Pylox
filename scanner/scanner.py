from .token_type import TokenType, KEY_WORDS_MAP
from .token import Token
from .pylox import PyLox

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


    def string(self):

        next_char = self.peek()

        while next_char != "\0" and next_char != '"':
            curr_char = self.advance()
            if curr_char == "\n":
                self.line += 1
            next_char = self.peek()
        
        if next_char == "\0":
            PyLox.error(self.line, "Unterminated string")
            return 

        if next_char == '"':
            self.advance()
            self.add_token(TokenType.STRING, self.source[self.start + 1 : self.current - 1])


    def is_digit(self, n):
        return "0" <= n <= "9"


    def number(self):
        next_char = self.peek()      

        while next_char != '\0' and self.is_digit(next_char):
            self.advance()
            next_char = self.peek()

        if next_char == ".":

            if self.is_digit(self.peek_next()):
                self.advance()

            while self.is_digit(self.peek()):
                self.advance()
        
        self.add_token(TokenType.NUMBER, float(self.source[self.start : self.current]))


    def is_alpha(self, c):
        return "a" <= c <= "z" or "A" <= c <= "Z" or c == "_"
    
    
    def is_alpha_numeric(self, c):
        return self.is_alpha(c) or self.is_digit(c)
    

    def identifier(self):
        next_char = self.peek()
        while self.is_alpha_numeric(next_char):
            self.advance()
            next_char = self.peek()
        
        text = self.source[self.start : self.current]
        token_type = KEY_WORDS_MAP.get(text, TokenType.IDENTIFIER)

        self.add_token(token_type) 
        

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
        elif current_char == " " or current_char == "\t" or current_char == "\r":
            pass
        elif current_char == "\n":
            self.line += 1
        elif current_char == "/":
            if self.match("/"):
                next_char = self.peek()
                while next_char != "\0" and next_char != "\n":
                    self.advance()
                    next_char = self.peek()
            else:
                self.add_token(TokenType.SLASH)
        elif current_char == "!":
            self.add_token(TokenType.BANG_EQUAL) if self.match("=") else self.add_token(TokenType.BANG)
        elif current_char == "=":
            self.add_token(TokenType.EQUAL_EQUAL) if self.match("=") else self.add_token(TokenType.EQUAL)
        elif current_char == "<":
            self.add_token(TokenType.LESS_EQUAL) if self.match("=") else self.add_token(TokenType.LESS)
        elif current_char == ">":
            self.add_token(TokenType.GREATER_EQUAL) if self.match("=") else self.add_token(TokenType.GREATER)
        elif current_char == '"':
            self.string()
        elif self.is_digit(current_char):
            self.number()
        elif self.is_alpha(current_char):
            self.identifier()
        else:
            PyLox.error(self.line, "Unexpected character.")

    
    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens


        