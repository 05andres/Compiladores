import ply.lex as lex
import sys

#list of tokens
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
'IDENTIDAD',
'NOIDENTIDAD',
'DESIGUALDAD',
#Incremento/Decremento
'INCREMENTO',
'DECREMENTO',
#Comparacion
'MENOR',
'MAYOR',
'MENORIGUAL',
'MAYORIGUAL',
'DIFERENTE',
'IGUAL',
'INTERROGACION',
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
'REFERENCIA',
'HASHTAG',
'DOT',
#OTROS
'ID',
'STRING',
'INTEGER',
'CADENA',
'CADENAA',
'CADENAAA',
'CONSTRUCTOR',
'NFUNCTION',
'HEXADECIMAL',
'OCTAL',
'OPAS',


)
#Reglas de expresiones regulares para simbolos simples
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_INTERROGACION= r'\?'
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
t_REFERENCIA = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_ignore = ' \t'
#OPERADORES Comparacion
t_IDENTIDAD = r'==='
t_IGUAL = r'=='
t_NOIDENTIDAD= r'!=='
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_DESIGUALDAD='<>'
t_INCREMENTO = '\++'
t_DECREMENTO = '\--'

def t_OPAS(t):
    r'as'
    return t
def t_NEW(t):
    r'new'
    return t

def t_HEXADECIMAL(t):
	r'(0x|0X)[a-fA-F0-9]+'
	return t
def t_OCTAL(t):
	r'0\d+'
	return t

def t_BREAK(t):
    r'break'
    return t

def t_CONSTRUCTOR(t):
    r'__construct'
    return t

def t_VAR(t):
    r'var'
    return t

def t_ARRAY(t):
    r'array'
    return t
def t_PRIVATE(t):
    r'private'
    return t
def t_PUBLIC(t):
    r'public'
    return t
def t_FOREACH(t):
    r'foreach'
    return t

def t_CADENA(t):
	r'\"[a-zA-Z_0-9\&\.\-\_\+\*\$\%\@\!\xc2\xa1\/\\\#\?\xc2\xbf\(\)\|\=\{\}\[\]\>\<\,\: \t]*\"' 
	return t
def t_CADENAA(t):
	r'\'[a-zA-Z_0-9\&\.\-\_\+\*\$\%\@\!\xc2\xa1\/\\\#\?\xc2\xbf\(\)\|\=\{\}\[\]\>\<\,\: \t]*\'' 
	return t
def t_CLASS(t):
    r'class'
    return t

def t_FUNCTION(t):
    r'function'
    return t
def t_ECHO(t):
    r'echo'
    return t
def t_TRUE(t):
    r'TRUE|true|True'
    return t

def t_FALSE(t):
    r'FALSE|False|false'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

'''
def t_ELSEIF(t):
    r'elseif'
    return t'''
#operadoreslogicos
def t_AND(t):
    r'and|&&'
    return t

def t_OR(t):
    r'or|\|\|'
    return t

def t_NOT(t):
    r'!'
    return t

def t_XOR(t):
    r'xor'
    return t
#estructuras de control
def t_WHILE(t):
    r'while'
    return t

def t_DO(t):
    r'do'
    return t

def t_FOR(t):
    r'for'
    return t

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    
def t_comments_C99(t):
    r'//(.)*?\n'
    t.lexer.lineno += 1
def t_INCLUDE(t):
    r'include'
    return t

def t_RETURN(t):
    r'return'
    return t

    
def t_ID(t):
    r'\$(_)?[0-9]*[a-zA-Z][a-zA-Z_0-9]*|\$(_)?[0-9]*'
    return t
def t_NFUNCTION(t):
	r'[a-zA-Z][a-zA-Z_a-zA-Z]*'
	return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"[a-zA-Z_0-9\&\.\-\_\+\*\$\%\@\!\xc2\xa1\/\\\#\?\xc2\xbf\(\)\|\=\{\}\[\]\>\<\,\: \t]*\"'
    t.value = str(t.value)
    return t

def t_STRINGG(t):
    r'\'[a-zA-Z_0-9\&\.\-\_\+\*\$\%\@\!\xc2\xa1\/\\\#\?\xc2\xbf\(\)\|\=\{\}\[\]\>\<\,\: \t]*\''
    t.value = str(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba\prueba.php'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	#input()