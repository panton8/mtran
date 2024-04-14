from Token import Token

# Types of AST (abstract syntax trees) nodes / типы узлов АСД

class AST(object):
    def __str__(self):
        return type(self).__name__


class BinOp(AST):
    def __init__(self, left: AST, op: Token, right: AST):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return f'({self.left} {self.op.value} {self.right})'


class UnaryOp(AST):
    def __init__(self, op: Token, expr: AST):
        self.op = op
        self.expr = expr

    def __str__(self):
        return f'({self.op.value}{self.expr})'


class Num(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value

    def __str__(self):
        return str(self.value)


class Boolean(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value == 'TRUE'

    def __str__(self):
        return str(self.value)


class String(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value

    def __str__(self):
        return self.value


class Compound(AST):
    def __init__(self):
        self.children = []

    def __str__(self):
        return '\n'.join(str(child) for child in self.children)


class Assign(AST):
    def __init__(self, left: AST, op: Token, right: AST):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return f'{self.left} {self.op.value} {self.right}'


class Var(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value

    def __str__(self):
        return str(self.value)


class IndexVar(AST):
    def __init__(self, token: Token, index: AST):
        self.token = token
        self.value = token.value
        self.index = index

    def __str__(self):
        return f'{self.value}[{self.index}]'


class Type(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value

    def __str__(self):
        return str(self.value)


class RangeType(AST):
    def __init__(self, token: Token, low_range, high_range):
        self.token = token
        self.low_range = low_range
        self.high_range = high_range

    def __str__(self):
        return f'{self.token.value}[{self.low_range}..{self.high_range}]'


class Program(AST):
    def __init__(self, name: str, block: AST):
        self.name = name
        self.block = block

    def __str__(self):
        return f'Program: {self.name}\n{self.block}'


class Block(AST):
    def __init__(self, declarations: list, compound_statement: Compound):
        self.declarations = declarations
        self.compound_statement = compound_statement

    def __str__(self):
        decls = '\n'.join(str(decl) for decl in self.declarations)
        return f'Declarations:\n{decls}\nCompound Statement:\n{self.compound_statement}'


class VarDecl(AST):
    def __init__(self, var_node: AST, type_node: AST):
        self.var_node = var_node
        self.type_node = type_node

    def __str__(self):
        return f'{self.var_node} : {self.type_node}'


class Param(AST):
    def __init__(self, var_node: AST, type_node: AST):
        self.var_node = var_node
        self.type_node = type_node

    def __str__(self):
        return f'{self.var_node} : {self.type_node}'


class ProcedureDecl(AST):
    def __init__(self, proc_name, formal_params, block_node: Block):
        self.proc_name = proc_name
        self.formal_params = formal_params
        self.block_node = block_node

    def __str__(self):
        params_str = ', '.join(str(param) for param in self.formal_params)
        return f'Procedure: {self.proc_name}\nFormal Params: {params_str}\n{self.block_node}'


class ProcedureCall(AST):
    def __init__(self, proc_name: str, actual_params: list, token: Token):
        self.proc_name = proc_name
        self.actual_params = actual_params
        self.token = token
        self.proc_symbol = None

    def __str__(self):
        params_str = ', '.join(str(param) for param in self.actual_params)
        return f'Call: {self.proc_name}({params_str})'


class Then(AST):
    def __init__(self, token: Token, child: AST):
        self.token = token
        self.child = child

    def __str__(self):
        return f'Then: {self.child}'


class Else(AST):
    def __init__(self, token: Token, child: AST):
        self.token = token
        self.child = child

    def __str__(self):
        return f'Else: {self.child}'


class Condition(AST):
    def __init__(self, token: Token, condition_node: AST, then_node: AST, else_node: AST):
        self.token = token
        self.condition_node = condition_node
        self.then_node = then_node
        self.else_node = else_node

    def __str__(self):
        return f'Condition:\n{self.condition_node}\nThen:\n{self.then_node}\nElse:\n{self.else_node}'


class Do(AST):
    def __init__(self, token: Token, child: AST):
        self.token = token
        self.child = child

    def __str__(self):
        return f'Do: {self.child}'


class While(AST):
    def __init__(self, token: Token, condition_node: AST, do_node: AST):
        self.token = token
        self.condition_node = condition_node
        self.do_node = do_node

    def __str__(self):
        return f'While: {self.condition_node}\nDo: {self.do_node}'


class Repeat(AST):
    def __init__(self, token: Token, repeat_node: AST, condition_node: AST):
        self.token = token
        self.repeat_node = repeat_node
        self.condition_node = condition_node

    def __str__(self):
        return f'Repeat:\n{self.repeat_node}\nUntil: {self.condition_node}'


class Setlength(AST):
    def __init__(self, token: Token, var_node: AST, length_node: AST):
        self.token = token
        self.var_node = var_node
        self.length_node = length_node

    def __str__(self):
        return f'Setlength: {self.var_node}, {self.length_node}'


class Writeln(AST):
    def __init__(self, token: Token, node_list: list):
        self.token = token
        self.node_list = node_list

    def __str__(self):
        nodes_str = ', '.join(str(node) for node in self.node_list)
        return f'Writeln: {nodes_str}'


class Readln(AST):
    def __init__(self, token: Token, node_list: list):
        self.token = token
        self.node_list = node_list

    def __str__(self):
        nodes_str = ', '.join(str(node) for node in self.node_list)
        return f'Readln: {nodes_str}'


class NoOp(AST):
    pass


