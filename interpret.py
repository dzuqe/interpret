from typing import List, Dict, Tuple

# polymorphic iterator
class Iterator:
    def __init__(self):
        pass

    def head(self):
        pass

    def next(self):
        pass
        
    def has_next(self) -> bool:
        pass


# interpreter pattern
# composite pattern
class IExpression:
    def __init__(self):
        pass

    def get_iterator(self) -> Iterator:
        pass

class Leaf(IExpression):
    def __init__(self, expression : str):
        self.expression = expression

    def interpret(self) -> str:
        #print(self.expression)
        return f"{self.expression}/Leaf"
    
    def get_iterator(self) -> Iterator:
        return Degenerate(self.expression)

class Branch(IExpression):
    def __init__(self, name : str) -> None:
        self.expressions = []
        self.name = name

    def interpret(self) -> None:
        data = []
        #json_str = ""
        for expression in self.expressions:
            data.append(expression.interpret())
            #json_str += f""
        return {f"{self.name}/Branch": data}
        #return json_str

    def add(self, expression : IExpression) -> None:
        self.expressions.append(expression)

    def get_iterator(self) -> Iterator:
        return General(self.expressions)


class General(Iterator):
    def __init__(self, items):
        self.items : List[IExpression] = items
        self.position : int = 0

    def head(self):
        pass

    def next(self) -> IExpression:
        item = self.items[self.position]
        self.position += 1
        return item

    def has_next(self) -> bool:
        return self.position < len(self.items)


    def current(self):
        return self.items[self.position]


class Degenerate(Iterator):
    def __init__(self, items):
        self.item : IExpression = item

    def next(self):
        return self.item

    def has_next(self) -> bool:
        return False
    
    def current(self):
        return self.item


# state pattern to handle state transitions
class IState:
    def __init__(self):
        pass


root = Branch("data")

swear = Branch("swear")
swear.add(Leaf("fuck"))
swear.add(Leaf("shit"))
swear.add(Leaf("horseshit"))
swear.add(Leaf("cunt"))
swear.add(Leaf("bitch"))

greet = Branch("greet")
hello_greet = Branch("hello_greet")
hello_greet.add(Leaf("hey"))
hello_greet.add(Leaf("heyo"))
hello_greet.add(Leaf("ey"))

greet.add(hello_greet)
greet.add(Leaf("hi"))
greet.add(Leaf("yo"))
greet.add(Leaf("wassup"))
greet.add(Leaf("wsg"))


root.add(swear)
root.add(greet)

# iterate through data and get recursive list of the tree
list = root.get_iterator()
data = []
while list.has_next():
    print(list.current().interpret())
    data.append(list.next().interpret())

#print(data)    

