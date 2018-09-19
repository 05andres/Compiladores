import ply.lex as lex

#list of tokens - Lista de tokens
tokens=(
    #reserved words - Palabras reservadas
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

    #Symbols - simbolos
    #Aritmeticos
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'ASIGNACION',
    #Incremento/Decremento
    'INCREMENTO'
    'DECREMENTO'
    #Comparacion
    'MENOR',
    'MAYOR',
    'MENORIGUAL',
    'MAYORIGUAL',
    'DIFERENTE',
    'IGUAL',
    'IGUALTIPODATO',
    'DIFERENTETIPODATO',
    'DISTINTO',
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBLOCK',
    'RBLOCK',
    'COLON',
    'AMPERSANT',
    'HASHTAG',
    'DOT'
)
    #Reglas de expresiones regulares para simbolos simples
    t_SUMA = r'\+'
    t_RESTA = r'-'
    t_MULTIPLICACION = r'\*'
    t_DIVISION = r'/'
    t_ASIGNACION = r'='
    t_MENOR = r'<'
    t_MAYOR = r'>'  
    t_SEMICOLON = ';'
    t_COMMA  = r','
    t_LPAREN = r'\('
    t_RPAREN  = r'\)'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_LBLOCK   = r'{'
    t_RBLOCK   = r'}'
    t_COLON   = r':'
    t_AMPERSANT = r'\&'
    t_HASHTAG = r'\#'
    t_DOT = r'\.'

def t_INCREMENTO(t):
    r'\+\+'
    return t

def t_DECREMENTO(t):
    r'--'
    return t

def t_MENORIGUAL(t):
    r'<='
    return t

def t_MAYORIGUAL(t):
    r'>='
    return t

def t_DIFERENTE(t):
    r'<>'
    return t

def t_IGUAL(t):
    r'=='
    return t
    
def t_IGUALTIPODATO(t):
    r'==='
    return t

def t_DIFERENTETIPODATO(t):
    r'!=='
    return t

def t_DISTINTO(t):
    r'!='
    return t
