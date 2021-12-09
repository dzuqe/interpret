from typing import List, Dict

class Lexer:
  def __init__(self, filename):
    self.filename = filename
    self.tokens = []

  def lex(self):
    txt = open(self.filename, 'r').read()
    print(txt)
    for c in txt:
      if c == '>':
        self.tokens.append({'name': 'increment_ptr', 'value': '>'})
      elif c == '<':
        self.tokens.append({'name': 'decrement_ptr', 'value': '<'})
      elif c == '+':
        self.tokens.append({'name': 'increment_byte', 'value': '+'})
      elif c == '-':
        self.tokens.append({'name': 'increment_byte', 'value': '-'})
      elif c == '.':
        self.tokens.append({'name': 'print_byte', 'value': '.'})
      elif c == ',':
        self.tokens.append({'name': 'print_byte', 'value': ','})
      elif c == '[':
        self.tokens.append({'name': 'jump_]_zero', 'value': '['})
      elif c == ']':
        self.tokens.append({'name': 'jump_[_not_zero', 'value': ']'})

  def get_tokens(self) -> List[Dict]:
    return self.tokens

lexer = Lexer('./programs/hello.bf')
lexer.lex()
print(lexer.get_tokens())

class Expression:
  def interpret(self) -> None:
    pass

class Composite(Expression):
  def __init__(self):
    self.items : List[Expression] = []

  def interpret(self) -> None:
    for item in self.items:
      item.interpret()

  def add(self, value : Expression) -> None:
    self.items.append(value)


class Terminal(Expression):
  def __init__(self, item : str):
    self.item : str = item

  def interpret(self) -> None:
    print(self.item)


class Parser:
  def __init__(self, tokens : List[Dict]):
    self.tokens : List[Dict] = tokens
    self.ast : Expression = None
    self.code = []

  def parse(self):
    for token in tokens:
      if token['name'] == 'increment_ptr':
        code.append("ptr += 1")

    self.ast = Composite()
    self.ast.add(Terminal('what'))
    self.ast.add(Terminal('the'))
    self.ast.add(Terminal('hell'))

    pass

  def get_ast(self):
    return self.ast

parser = Parser(lexer.get_tokens())
parser.parse()
parser.get_ast().interpret()
