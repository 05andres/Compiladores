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
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'MENOR',
    'MENORIGUAL',
    'IGUAL',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',

    #Reglas de expresiones regulares para simbolos simples
    t_SUMA = r'+'
    t_RESTA = r'-'
    t_MULTIPLICACION = r'*'
    t_DIVISION = r'/'
    t_MENOR = r'<'
    t_MENORIGUAL = r'<='
    t_IGUAL = r'='
    )
