grammar Instant;

/** The start rule; begin parsing here. */
prog: (stmt SEPARATOR)* stmt EOF | ;

stmt: Ident '=' exp1
    | exp1
    ;


exp1: left=exp2 '+' right=exp1
    | exp2
    ;
exp2: '(' paren=exp1 ')'
    | left=exp2 ('*'|'/') right=exp2
    | left=exp2 '-' right=exp2
    | Ident
    | Integer
    ;

SEPARATOR : (';');
Ident :   [a-zA-Z]+ ;
PAREN: '(';
OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';
Integer : [0-9]+;
WS : [ \t\r\n]+ -> skip;
