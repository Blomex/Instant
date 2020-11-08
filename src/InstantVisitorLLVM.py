# Generated from .\Instant.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .InstantParser import InstantParser
else:
    from InstantParser import InstantParser

from InstantLexer import InstantLexer
# This class defines a complete generic visitor for a parse tree produced by InstantParser.
# text = FileStream("test")
# lexer = InstantLexer(text)
# stream = CommonTokenStream(lexer)
# parser = InstantParser(stream)

class InstantVisitor(ParseTreeVisitor):
    def __init__(self):
        self.instructions = []
        self.register_counter = 0
        self.local_vars = set()
    # Visit a parse tree produced by InstantParser#prog.
    def visitProg(self, ctx:InstantParser.ProgContext):
        self.instructions.append("declare void @printInt(i32)")
        self.instructions.append("define i32 @main() {")
        self.visitChildren(ctx)
        self.instructions.append("ret i32 0")
        self.instructions.append("}")
        return self.instructions


    # Visit a parse tree produced by InstantParser#stmt.
    def visitStmt(self, ctx:InstantParser.StmtContext):
        if ctx.Ident():
            variable = str(ctx.Ident())
            register = "%{}".format(variable)
            if variable not in self.local_vars:
                self.local_vars.add(variable)
                self.instructions.append("{} = alloca i32".format(register))
            value = self.visitExp1(ctx.exp1())
            self.instructions.append("store i32 {}, i32* {}".format(value, register))
        else:
            register = self.visitExp1(ctx.exp1())
            self.instructions.append("call void @printInt(i32 {})".format(register))

    # Visit a parse tree produced by InstantParser#exp1.
    def visitExp1(self, ctx:InstantParser.Exp1Context):
        if ctx.OP_ADD():
            left = self.visit(ctx.left)
            right = self.visit(ctx.right)
            self.instructions.append("%r{} = add i32 {}, {}".format(self.register_counter, left, right))
            register = "%r{}".format(self.register_counter)
            self.register_counter += 1
            return register
        elif ctx.exp2():
            return self.visitExp2(ctx.exp2())


    # Visit a parse tree produced by InstantParser#exp2.
    def visitExp2(self, ctx:InstantParser.Exp2Context):
        if ctx.Ident():
            variable = "%{}".format(str(ctx.Ident()))
            register = "%r{}".format(self.register_counter)
            self.instructions.append("{} = load i32, i32* {}".format(register, variable))
            self.register_counter += 1
            return register
        elif ctx.Integer():
            return str(ctx.Integer())
        elif ctx.PAREN():
            return self.visitExp1(ctx.exp1())
        else: #complex expression
            left = self.visit(ctx.left)
            right = self.visit(ctx.right)
            register = "%r{}".format(self.register_counter)
            if ctx.OP_SUB():
                self.instructions.append("{} = sub i32 {}, {}".format(register, left, right))
            if ctx.OP_MUL():
                self.instructions.append("{} = mul i32 {}, {}".format(register, left, right))
            if ctx.OP_DIV():
                self.instructions.append("{} = sdiv i32 {}, {}".format(register, left, right))
            self.register_counter += 1
            return register



del InstantParser