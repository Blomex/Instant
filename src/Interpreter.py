import sys
import os
from antlr4 import *
from InstantLexer import InstantLexer
from InstantParser import InstantParser
from BetterVisitor import InstantVisitor
def main(argv):
    # text = InputStream(input(">"))
    if sys.argv[1]:
        file = sys.argv[1]
        filename, file_extension = os.path.splitext(file)
        result_file_path = filename + ".j"
        text = FileStream(file)
        lexer = InstantLexer(text)
        stream = CommonTokenStream(lexer)
        parser = InstantParser(stream)
        tree = parser.prog()
        ast = InstantVisitor().visitProg(tree)
        if parser.getNumberOfSyntaxErrors() == 0:
            result_file = open(result_file_path, "w+")
            for line in ast:
                print(line, file=result_file)
            result_file.close()
            sys.exit(0)
        else:
            print("Code generation failed due to parsing error", file=sys.stderr)
            sys.exit(1)
    #print(tree.toStringTree(recog=parser))
        #ast = InstantVisitor().visitCompileUnit(tree)
        #value = EvaluateExpressionVisitor().visit(ast)
        #print('=', value)
if __name__ == '__main__':
    main(sys.argv)
