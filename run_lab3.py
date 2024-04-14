# from Parser import Parser
# from Lexer import Lexer
# from Nodes import *
# from SemanticAnalysis import *
#
# def print_tree(node, indent=0):
#     if isinstance(node, AST):
#         print(' ' * indent + str(node.__class__.__name__))
#         for key, value in node.__dict__.items():
#             if isinstance(value, AST):
#                 print_tree(value, indent + 4)
#             elif isinstance(value, list):
#                 for item in value:
#                     print_tree(item, indent + 4)
#             elif isinstance(value, Token):
#                 print(' ' * (indent + 4) + f'{key}: {value}')
#             else:
#                 print(' ' * (indent + 4) + f'{key}: {repr(value)}')
#     else:
#         print(' ' * indent + repr(node))
#
# def run_lab3():
#     with open('program.txt', 'r') as file:
#         text = file.read()
#         lexer = Lexer(text)
#         parser = Parser(lexer)
#         tree = parser.parse()
#         print_tree(tree)
#         try:
#             semantic_analyzer = SemanticAnalyzer()
#             semantic_analyzer.visit(tree)
#
#         except Exception as e:
#             print(e)
#
# if __name__ == '__main__':
#     run_lab3()
