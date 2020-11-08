# Generated from .\Instant.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("<\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\7\2\16\n")
        buf.write("\2\f\2\16\2\21\13\2\3\2\3\2\3\2\3\2\5\2\27\n\2\3\3\3\3")
        buf.write("\3\3\3\3\5\3\35\n\3\3\4\3\4\3\4\3\4\3\4\5\4$\n\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5/\n\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\7\5\67\n\5\f\5\16\5:\13\5\3\5\2\3\b\6\2\4\6")
        buf.write("\b\2\3\3\2\n\13\2@\2\26\3\2\2\2\4\34\3\2\2\2\6#\3\2\2")
        buf.write("\2\b.\3\2\2\2\n\13\5\4\3\2\13\f\7\5\2\2\f\16\3\2\2\2\r")
        buf.write("\n\3\2\2\2\16\21\3\2\2\2\17\r\3\2\2\2\17\20\3\2\2\2\20")
        buf.write("\22\3\2\2\2\21\17\3\2\2\2\22\23\5\4\3\2\23\24\7\2\2\3")
        buf.write("\24\27\3\2\2\2\25\27\3\2\2\2\26\17\3\2\2\2\26\25\3\2\2")
        buf.write("\2\27\3\3\2\2\2\30\31\7\6\2\2\31\32\7\3\2\2\32\35\5\6")
        buf.write("\4\2\33\35\5\6\4\2\34\30\3\2\2\2\34\33\3\2\2\2\35\5\3")
        buf.write("\2\2\2\36\37\5\b\5\2\37 \7\b\2\2 !\5\6\4\2!$\3\2\2\2\"")
        buf.write("$\5\b\5\2#\36\3\2\2\2#\"\3\2\2\2$\7\3\2\2\2%&\b\5\1\2")
        buf.write("&\'\7\7\2\2\'(\5\6\4\2()\7\4\2\2)/\3\2\2\2*/\7\6\2\2+")
        buf.write("/\7\f\2\2,-\7\t\2\2-/\7\f\2\2.%\3\2\2\2.*\3\2\2\2.+\3")
        buf.write("\2\2\2.,\3\2\2\2/8\3\2\2\2\60\61\f\7\2\2\61\62\t\2\2\2")
        buf.write("\62\67\5\b\5\b\63\64\f\6\2\2\64\65\7\t\2\2\65\67\5\b\5")
        buf.write("\7\66\60\3\2\2\2\66\63\3\2\2\2\67:\3\2\2\28\66\3\2\2\2")
        buf.write("89\3\2\2\29\t\3\2\2\2:8\3\2\2\2\t\17\26\34#.\668")
        return buf.getvalue()


class InstantParser ( Parser ):

    grammarFileName = "Instant.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "')'", "<INVALID>", "<INVALID>", 
                     "'('", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "SEPARATOR", 
                      "Ident", "PAREN", "OP_ADD", "OP_SUB", "OP_MUL", "OP_DIV", 
                      "Integer", "WS" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_exp1 = 2
    RULE_exp2 = 3

    ruleNames =  [ "prog", "stmt", "exp1", "exp2" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    SEPARATOR=3
    Ident=4
    PAREN=5
    OP_ADD=6
    OP_SUB=7
    OP_MUL=8
    OP_DIV=9
    Integer=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InstantParser.StmtContext)
            else:
                return self.getTypedRuleContext(InstantParser.StmtContext,i)


        def EOF(self):
            return self.getToken(InstantParser.EOF, 0)

        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(InstantParser.SEPARATOR)
            else:
                return self.getToken(InstantParser.SEPARATOR, i)

        def getRuleIndex(self):
            return InstantParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = InstantParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [InstantParser.Ident, InstantParser.PAREN, InstantParser.OP_SUB, InstantParser.Integer]:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 8
                        self.stmt()
                        self.state = 9
                        self.match(InstantParser.SEPARATOR) 
                    self.state = 15
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                self.state = 16
                self.stmt()
                self.state = 17
                self.match(InstantParser.EOF)
                pass
            elif token in [InstantParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Ident(self):
            return self.getToken(InstantParser.Ident, 0)

        def exp1(self):
            return self.getTypedRuleContext(InstantParser.Exp1Context,0)


        def getRuleIndex(self):
            return InstantParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = InstantParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(InstantParser.Ident)
                self.state = 23
                self.match(InstantParser.T__0)
                self.state = 24
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Exp2Context
            self.right = None # Exp1Context

        def OP_ADD(self):
            return self.getToken(InstantParser.OP_ADD, 0)

        def exp2(self):
            return self.getTypedRuleContext(InstantParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(InstantParser.Exp1Context,0)


        def getRuleIndex(self):
            return InstantParser.RULE_exp1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp1" ):
                listener.enterExp1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp1" ):
                listener.exitExp1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = InstantParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_exp1)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                localctx.left = self.exp2(0)
                self.state = 29
                self.match(InstantParser.OP_ADD)
                self.state = 30
                localctx.right = self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # Exp2Context
            self.paren = None # Exp1Context
            self.right = None # Exp2Context

        def PAREN(self):
            return self.getToken(InstantParser.PAREN, 0)

        def exp1(self):
            return self.getTypedRuleContext(InstantParser.Exp1Context,0)


        def Ident(self):
            return self.getToken(InstantParser.Ident, 0)

        def Integer(self):
            return self.getToken(InstantParser.Integer, 0)

        def OP_SUB(self):
            return self.getToken(InstantParser.OP_SUB, 0)

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InstantParser.Exp2Context)
            else:
                return self.getTypedRuleContext(InstantParser.Exp2Context,i)


        def OP_MUL(self):
            return self.getToken(InstantParser.OP_MUL, 0)

        def OP_DIV(self):
            return self.getToken(InstantParser.OP_DIV, 0)

        def getRuleIndex(self):
            return InstantParser.RULE_exp2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp2" ):
                listener.enterExp2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp2" ):
                listener.exitExp2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = InstantParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [InstantParser.PAREN]:
                self.state = 36
                self.match(InstantParser.PAREN)
                self.state = 37
                localctx.paren = self.exp1()
                self.state = 38
                self.match(InstantParser.T__1)
                pass
            elif token in [InstantParser.Ident]:
                self.state = 40
                self.match(InstantParser.Ident)
                pass
            elif token in [InstantParser.Integer]:
                self.state = 41
                self.match(InstantParser.Integer)
                pass
            elif token in [InstantParser.OP_SUB]:
                self.state = 42
                self.match(InstantParser.OP_SUB)
                self.state = 43
                self.match(InstantParser.Integer)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 52
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = InstantParser.Exp2Context(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 46
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 47
                        _la = self._input.LA(1)
                        if not(_la==InstantParser.OP_MUL or _la==InstantParser.OP_DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 48
                        localctx.right = self.exp2(6)
                        pass

                    elif la_ == 2:
                        localctx = InstantParser.Exp2Context(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 49
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 50
                        self.match(InstantParser.OP_SUB)
                        self.state = 51
                        localctx.right = self.exp2(5)
                        pass

             
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.exp2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




