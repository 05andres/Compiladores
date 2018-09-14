import ply.lex as lex

#list of tokens
tokens=(
#reserved words
'__HALT_COMPILER',#()
'BREAK',
'CLONE',
'DIE',#()
'EMPTY',#()
'ENDSWITCH',
'FINAL',
'GLOBAL',
'INCLUDE_ONCE',
'LIST',#()
'PRIVATE',
'RETURN',
'TRY',
'XOR',
'ABSTRACT',
'CALLABLE',
'CONST',
'DO',
'ENDDECLARE',
'ENDWHILE',
'FINALLY',
'GOTO',
'INSTANCEOF',
'NAMESPACE',
'PROTECTED',
'STATIC',
'UNSET',#()
'YIELD',
'AND',
'CASE',
'CONTINUE',
'ECHO',
'ENDFOR',
'EVAL',#()
'FOR',
'IF',
'INSTEADOF',
'NEW',
'PUBLIC',
'SWITCH',
'USE',
'ARRAY',#()
'CATCH',
'DECLARE',
'ELSE',
'ENDFOREACH',
'EXIT',#()
'FOREACH',
'IMPLEMETS',
'INTERFACE',
'OR',
'REQUIRE',
'THROW',
'VAR',
'AS',
'CLASS',
'DEFAULT',
'ELSEIF',
'ENDIF',
'EXTENDS',
'FUNCTION',
'INCLUDE',
'ISSET',#()
'PRINT',
'REQUIRE_ONCE',
'TRAIT',
'WHILE',
)



def t_BREAK(t):
    r'break'
    return t
def t_VAR(t):
    r'var'
    return t
def t_PRIVATE(t):
    r'private'
    return t