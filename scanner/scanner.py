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
        
        