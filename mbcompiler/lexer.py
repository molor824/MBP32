from peekable import *
from try_iter import *

class Token:
    pass
class Newline(Token):
    def __str__(self):
        return "Newline"
class Ident(Token):
    def __init__(self, ident: str):
        self.ident = ident
    def __str__(self):
        return f"Ident {self.ident}"
class Integer(Token):
    def __init__(self, integer: int):
        self.integer = integer
    def __str__(self):
        return f"Integer {self.integer}"
class Symbol(Token):
    def __init__(self, symbol: str):
        self.symbol = symbol
    def __str__(self):
        return f"Symbol {self.symbol!r}"

class Lexer:
    SYMBOLS = {
        '+', '-', '*', '/', '>>', '<<', ':', ',', '.', '[', ']', '(', ')'
    }
    MAX_LEN = max(len(s) for s in SYMBOLS)

    def __init__(self, source: str):
        self.source = source
        self.source_iter = Peekable(enumerate(source))
    def __iter__(self):
        return self
    def __next__(self) -> Token:
        for i, c in self.source_iter:
            if c == '\n':
                return Newline()
            if c.isspace():
                continue
            if c == ';':
                for _, c in self.source_iter:
                    if c == '\n':
                        break
                continue
            if c.isalpha() or c == '_':
                start = i
                end = i + 1
                while True:
                    result = try_peek(self.source_iter)
                    if result is None:
                        break
                    c = result[1]
                    if not c.isalnum() and c != '_':
                        break
                    end += 1
                    next(self.source_iter)
                return Ident(self.source[start:end])
            if c.isdigit():
                start = i
                end = i + 1
                while True:
                    result = try_peek(self.source_iter)
                    if result is None:
                        break
                    c = result[1]
                    if not c.isdigit():
                        break
                    end += 1
                    next(self.source_iter)
                return Integer(self.source[start:end])
            length = min(self.MAX_LEN + i, len(self.source))
            for i1 in range(length, i, -1):
                symbol = self.source[i:i1]
                if symbol in self.SYMBOLS:
                    for _ in range(i1 - i):
                        next(self.source_iter)
                    return Symbol(symbol)
            raise SyntaxError(f"Invalid character: {c!r}")
        raise StopIteration