# Generated from .\Instant.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .InstantParser import InstantParser
else:
    from InstantParser import InstantParser

# This class defines a complete generic visitor for a parse tree produced by InstantParser.

class InstantVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by InstantParser#prog.
    def visitProg(self, ctx:InstantParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InstantParser#stmt.
    def visitStmt(self, ctx:InstantParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InstantParser#exp1.
    def visitExp1(self, ctx:InstantParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InstantParser#exp2.
    def visitExp2(self, ctx:InstantParser.Exp2Context):
        return self.visitChildren(ctx)



del InstantParser