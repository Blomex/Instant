# Generated from .\Instant.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .InstantParser import InstantParser
else:
    from InstantParser import InstantParser
import sys
from TreeNode import NumberNode, InfixExpressionNode, LiteralNode


# This class defines a complete generic visitor for a parse tree produced by InstantParser.
class InstantVisitor(ParseTreeVisitor):

    def __init__(self):
        self.stackSize = 0
        self.maxStackSize = 0
        self.errors = []
        self.statementNumber = 0
        self.local_vars = {}
        self.instructions = []

    # Visit a parse tree produced by InstantParser#prog.
    def visitProg(self, ctx:InstantParser.ProgContext, class_name):
        if ctx.stmt():
            self.visitChildren(ctx) # just to get maxStackSize
            self.instructions.clear()
            self.stackSize = 0
            self.errors.clear()
            self.local_vars.clear()
            self.visitChildren(ctx)  # now every statement knows what is maximum stack size.
            self.instructions.insert(0, ".class public {}".format(class_name))
            self.instructions.insert(1, ".super java/lang/Object")
            self.instructions.insert(2, ".method public static main([Ljava/lang/String;)V")
            self.instructions.insert(3, ".limit stack {}".format(self.maxStackSize))
            self.instructions.insert(4, ".limit locals {}".format(max(len(self.local_vars), 1)))
            self.instructions.append("return")
            self.instructions.append(".end method")
            if len(self.errors) == 0:
                pass
                # for i in self.instructions:
                #     print(i)
            else:
                print("Errors found: {}".format(len(self.errors)), file=sys.stderr)
                for error in self.errors:
                    print(error, file=sys.stderr)
        return self.instructions

    # Visit a parse tree produced by InstantParser#stmt.
    def visitStmt(self, ctx:InstantParser.StmtContext):
        if ctx.Ident():
            depth, instructions = self.visitExp1(ctx.exp1())
            id = str(ctx.Ident())
            self.instructions.extend(instructions)
            if id not in self.local_vars.keys():
                self.local_vars[id] = len(self.local_vars)
            if self.local_vars[id] <= 3:
                self.instructions.append("istore_{}".format(self.local_vars[id]))
            else:
                self.instructions.append("istore {}".format(self.local_vars[id]))
            self.stackSize -= 1
        elif ctx.exp1():
            depth, instructions = self.visitChildren(ctx)
            if depth < self.maxStackSize:
                self.instructions.append("getstatic  java/lang/System/out Ljava/io/PrintStream;")
            self.instructions = self.instructions + instructions
            if depth >= self.maxStackSize:
                self.instructions.append("getstatic  java/lang/System/out Ljava/io/PrintStream;")
                self.instructions.append("swap")
            self.stackSize += 1
            self.maxStackSize = max(self.stackSize, self.maxStackSize)
            self.instructions.append("invokevirtual  java/io/PrintStream/println(I)V")
            self.stackSize -= 2
        return self.instructions
    # # Visit a parse tree produced by InstantParser#exp1.
    def visitExp1(self, ctx: InstantParser.Exp1Context):
        instructions = []
        if ctx.OP_ADD():
            prev_max = self.maxStackSize
            prev_stack = self.stackSize
            right, right_instructions = self.visit(ctx.right)
            left, left_instructions = self.visit(ctx.left)
            if left >= right and self.maxStackSize > prev_max:
                instructions = left_instructions + right_instructions
                self.maxStackSize = prev_max
                self.stackSize = prev_stack
                # Just to get real stack size...
                self.visit(ctx.left)
                self.visit(ctx.right)
            else:
                instructions = right_instructions + left_instructions
            instructions.append("iadd")
            self.stackSize -= 1
            depth = min(max(left, right+1), max(right, left+1))
            return depth, instructions
        else:
            return self.visit(ctx.exp2())

    # Visit a parse tree produced by InstantParser#exp2.
    def visitExp2(self, ctx: InstantParser.Exp2Context):
        instructions = []
        if ctx.Integer():
            value = int(str(ctx.Integer()))
            if 5 >= value >= 0:
                instructions.append("iconst_{}".format(value))
            elif 127 >= value:
                instructions.append("bipush {}".format(value))
            elif 32767 >= value:
                instructions.append("sipush {}".format(value))
            else:
                instructions.append("ldc {}".format(value))
            self.stackSize += 1
            self.maxStackSize = max(self.maxStackSize, self.stackSize)
            return 1, instructions
        elif ctx.Ident():
            self.stackSize += 1
            self.maxStackSize = max(self.maxStackSize, self.stackSize)
            ident = str(ctx.Ident())
            if ident in self.local_vars and self.local_vars[ident] <= 3:
                instructions.append("iload_{}".format(self.local_vars[ident]))
            elif ident in self.local_vars:
                instructions.append("iload {}".format(self.local_vars[ident]))
            elif ident not in self.local_vars:
                self.errors.append("Error at line {}, column {}: No variable {} previously declared"
                                   .format(ctx.start.line, ctx.start.column, ident))
            return 1, instructions
        elif ctx.PAREN():
            return self.visit(ctx.paren)
        else:  # complex expression
            prev_max = self.maxStackSize
            prev_stack = self.stackSize
            left, left_instructions = self.visit(ctx.left)
            right, right_instructions = self.visit(ctx.right)
            self.stackSize -= 1
            if right > left and self.maxStackSize > prev_max:
                instructions = right_instructions + left_instructions
                self.maxStackSize = prev_max
                self.stackSize = prev_stack
                # Just to get real stack size...
                self.visit(ctx.right)
                self.visit(ctx.left)
                self.stackSize-=1
                instructions.append('swap')
            else:
                instructions = left_instructions + right_instructions
            if ctx.OP_DIV():
                instructions.append('idiv')
            elif ctx.OP_MUL():
                instructions.append('imul')
            elif ctx.OP_SUB():
                instructions.append('isub')
            depth = min(max(left, right+1), max(right, left+1))
            return depth, instructions


del InstantParser
