# Generated from .\Instant.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write(":\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\3")
        buf.write("\3\3\3\4\3\4\3\5\6\5!\n\5\r\5\16\5\"\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\6\13\60\n\13\r\13\16\13\61")
        buf.write("\3\f\6\f\65\n\f\r\f\16\f\66\3\f\3\f\2\2\r\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\3\2\5\4\2C\\c")
        buf.write("|\3\2\62;\5\2\13\f\17\17\"\"\2<\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\3\31\3\2\2\2\5\33\3\2\2\2\7\35\3\2\2\2\t \3\2")
        buf.write("\2\2\13$\3\2\2\2\r&\3\2\2\2\17(\3\2\2\2\21*\3\2\2\2\23")
        buf.write(",\3\2\2\2\25/\3\2\2\2\27\64\3\2\2\2\31\32\7?\2\2\32\4")
        buf.write("\3\2\2\2\33\34\7+\2\2\34\6\3\2\2\2\35\36\7=\2\2\36\b\3")
        buf.write("\2\2\2\37!\t\2\2\2 \37\3\2\2\2!\"\3\2\2\2\" \3\2\2\2\"")
        buf.write("#\3\2\2\2#\n\3\2\2\2$%\7*\2\2%\f\3\2\2\2&\'\7-\2\2\'\16")
        buf.write("\3\2\2\2()\7/\2\2)\20\3\2\2\2*+\7,\2\2+\22\3\2\2\2,-\7")
        buf.write("\61\2\2-\24\3\2\2\2.\60\t\3\2\2/.\3\2\2\2\60\61\3\2\2")
        buf.write("\2\61/\3\2\2\2\61\62\3\2\2\2\62\26\3\2\2\2\63\65\t\4\2")
        buf.write("\2\64\63\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66\67\3\2")
        buf.write("\2\2\678\3\2\2\289\b\f\2\29\30\3\2\2\2\6\2\"\61\66\3\b")
        buf.write("\2\2")
        return buf.getvalue()


class InstantLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    SEPARATOR = 3
    Ident = 4
    PAREN = 5
    OP_ADD = 6
    OP_SUB = 7
    OP_MUL = 8
    OP_DIV = 9
    Integer = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "')'", "'('", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "SEPARATOR", "Ident", "PAREN", "OP_ADD", "OP_SUB", "OP_MUL", 
            "OP_DIV", "Integer", "WS" ]

    ruleNames = [ "T__0", "T__1", "SEPARATOR", "Ident", "PAREN", "OP_ADD", 
                  "OP_SUB", "OP_MUL", "OP_DIV", "Integer", "WS" ]

    grammarFileName = "Instant.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


