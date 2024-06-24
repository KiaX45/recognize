from typing import List, Dict, Tuple, Optional, Union, Any, Callable
import re as regex

#Global exprecions
expresion: str = ""

def main():
    #ask for the initial exprecion 
    user_expression = input("Enter the expresion: ")
    # Eliminate the blank spaces 
    user_expression = user_expression.replace(" ", "")
    #this has to recognize aritmetic exprecions only we will check this with regex
    try:
        check(user_expression)
    except ValueError as e:
        print(e)
        return
    #if no extrange simboles have been found we start the process
    global expresion
    expresion = user_expression 
    evaluate()

def evaluate() -> int:
    procS()


def procS():
    print(procELO())
    pass


#Metodos seccion logica 
def procELO() -> bool:
    global expresion
    symbol = expresion[0]
    match symbol:
        case _ if symbol == "(" or regex.match(r'[0-9]+', symbol) or symbol == "!" or symbol == "-":
            primer_operando = procEL2()
            lista_operandos = procELO_L()
            final_expresion = f"{primer_operando}{lista_operandos}"
            return eval(final_expresion)
        case _:
            raise ValueError(f"Error Found in procELO with the character {expresion[0]}")
    pass


def procELO_L() -> str:
    global expresion
    if expresion == "":
        return ""
    symbol = expresion[0]
    match symbol:
        case _ if symbol == "|":
            advance("|")
            primer_operando = procEL2()
            lista_operandos = procELO_L()
            final_expresion = f"|{primer_operando}{lista_operandos}"
            return final_expresion
        case ")":
            return ""
        case _:
            raise ValueError(f"Error Found in procELO_L with the character {expresion[0]}")
            
    pass


def procEL2() -> bool:
    global expresion
    symbol: str = expresion[0]
    match symbol:
        case _ if regex.match(r'[0-9]+', symbol) or symbol== "(" or symbol == "!" or symbol == "-":
            primer_operando = procEL3()
            lista_operandos = procEL2_L()
            final_expresion = f"{primer_operando}{lista_operandos}"
            return eval(final_expresion)
        case _:
            raise ValueError(f"Error Found in procEL2 with the character {expresion[0]}")
    pass


def procEL2_L():
    global expresion
    if expresion == "":
        return ""
    symbol = expresion[0]
    match symbol:
        case _ if symbol == "&":
            advance("&")
            primer_operando = procEL3()
            lista_operandos = procEL2_L()
            final_expresion = f"&{primer_operando}{lista_operandos}"
            return final_expresion
        case _ if symbol == "|" or symbol == ")":
            return ""
        case _:
            raise ValueError(f"Error Found in procEL2_L with the character {expresion[0]}")
    pass

def procEL3():
    global expresion
    symbol = expresion[0]
    match symbol:
        case _ if symbol == "!":
            advance("!")
            return eval(f"not {procER()}")
        case _ if regex.match(r'[0-9]+', symbol) or symbol== "(" or symbol == "-":
            return procER()
        case _:
            raise ValueError(f"Error Found in EL3 with the character {expresion[0]}")




#Metodos segunda sección
def procER():
    global expresion
    symbol: str = expresion[0]
    match symbol:
        case _ if regex.match(r'[0-9]+', symbol) or symbol == "-" or symbol == "(":
            return procERL(procE())

def procERL(first_operator: int) -> bool:
    global expresion
    if expresion == "":
        return first_operator
    symbol: str = expresion[0]
    match symbol:
        case _ if regex.match(r'(=|!|<|>)', symbol): #si el siguiente es un operador de comparación 
            #En este puento el proceso OR nos dara el operador de comparación 
            # Y el proceso E nos dara el segundo operando
            operator = procOR()
            second_operator = procE()
            #Creamos una expreción para luego evaluar
            print(operator)
            exprecion = f"{first_operator} {operator} {second_operator}"
            #retornamos el resultado de la expreción
            print(exprecion)
            return eval(exprecion)
        case _ if regex.match(r"(\||&)", symbol):
            return first_operator
        case ")":
            return first_operator
        case _:
            raise ValueError(f"Error Found in procERL with the character {expresion[0]}")


def procOR():
    global expresion
    symbol: str = expresion[0]
    match symbol:
        case _ if symbol == "=":
            advance("=")
            return procIG()
        case _ if symbol == "<":
            advance("<")
            return procME()
        case _ if symbol == "!":
            advance("!")
            return procDI()
        case _ if symbol == ">":
            advance(">")
            return procMA()
        case _:
            raise ValueError(f"Error Found in procOR with the character {expresion[0]}")
    pass

def procMA():
    global expresion
    print(expresion)
    if expresion == "":
        return ""
    symbol: str = expresion[0]
    match symbol:
        case _ if symbol == "=":
            advance("=")
            return ">="
        case _ if regex.match(r'[0-9]+', symbol):
            return(">")
        case _: 
            raise ValueError(f"Error Found in procMA with the character {expresion[0]}")
    pass


def procIG() -> str:
    global expresion
    if expresion == "":
        raise ValueError(f"Error Found in procIG do you mean ==")
    symbol: str = expresion[0]
    match symbol:
        case _ if symbol == "=":
            advance("=")
            return "=="
        case _ if  regex.match(r'[0-9]+', symbol):
            raise ValueError(f"Error Found in procIG with the character {expresion[0]} do you mean ==")
        case _: 
            raise ValueError(f"Error Found in procIG with the character {expresion[0]}")
    pass


def procME() -> str:
    global expresion
    symbol: str = expresion[0]
    match symbol:
        case _ if  regex.match(r'[0-9]+', symbol):
            return ("<")
        case _ if symbol == "=":
            advance("=")
            return "<="
        case _: 
            raise ValueError(f"Error Found in procME with the character {expresion[0]}")
    pass

def procDI():
    global expresion
    if expresion == "":
        raise ValueError(f"Error Found in procDI do you mean !=")
    symbol: str = expresion[0]
    match symbol:
        case _ if symbol == "=":
            advance("=")
            return "!="
        case _ if  regex.match(r'[0-9]+', symbol):
            raise ValueError(f"Error Found in procDI with the character {expresion[0]} do you mean !=")
        case _: 
            raise ValueError(f"Error Found in procDI with the character {expresion[0]}")
    pass

#Metodos aritmeticos
def procE() -> int:
    global expresion
    symbol: str = expresion[0]
    match symbol:
        case _ if regex.match(r'[0-9]+', symbol) or symbol == "-":
            resultado = procEL(procResta())
            return resultado
        case _ if symbol == '(':
            return procEL(procResta()) 
        case _ if  symbol == ')':
            return None
        case _:
            raise ValueError(f"Error Found in procE with the character {expresion[0]}")
    pass

def procEL(operator: int) -> int:
    global expresion
    if len(expresion) == 0:
        return operator
    symbol: str = expresion[0]
    match symbol:
        case '+':
            # In this position we have to do the addition with the return of the next function
            advance("+")
            numero = operator + procEL(procResta())
            return numero
        case _ if symbol == "":
            return operator
        case _ if symbol == ')':
            return operator
        case _ if regex.match(r'(=|!|<|>)', symbol):
            return operator
        case _ if regex.match(r"(\||&)", symbol):
            return operator
        case _:
            raise (f"Error Found in procEL with the character {expresion[0]}")
    pass

def procResta():
    global expresion
    symbol: str = expresion[0]
    match symbol:
        case _ if regex.match(r'[0-9]+', symbol) or symbol == "-":
            resultado = procRestaL(procT())
            return resultado
        case _ if symbol == '(':
            return procRestaL(procT()) 
        case _ if  symbol == ')':
            return None
        case _:
            raise ValueError(f"Error Found in procResta with the character {expresion[0]}")
    pass

def procRestaL(operator: int) -> int:
    global expresion
    if len(expresion) == 0:
        return operator
    symbol: str = expresion[0]
    match symbol:
        case '-':
            # In this position we have to do the subtraction with the return of the next function
            advance("-")
            numero = operator - procRestaL(procT())
            return numero
        case "+":
            return operator
        case _ if symbol == "":
            return operator
        case _ if symbol == ')':
            return operator
        case _ if regex.match(r'(=|!|<|>)', symbol):
            return operator
        case _ if regex.match(r"(\||&)", symbol):
            return operator
        case _:
            raise ValueError(f"Error Found in procRestaL with the character {expresion[0]}")
    pass

def procT() -> int:
    global expresion
    symbol: str = expresion[0]
    match symbol:
        case _ if regex.match(r'[0-9]+', symbol) or symbol == "-":
            resultado = procDivicion()
            return procTL(resultado)
        case _ if symbol == '(':
            return procTL(procDivicion()) 
        case _:
            raise ValueError(f"Error Found in procT with the character {expresion[0]}")
    pass

def procTL(operator: int) -> int:
    global expresion
    if len(expresion) == 0:
        return operator
    # We have to check if the next operator is a multiplication 
    if expresion[0] == "*":
        advance("*")
        resultado = procTL(procDivicion())
        resultado = operator * resultado
        return resultado
    elif expresion[0] == "+" or expresion[0] == "-":
        return operator
    elif expresion[0] == "(":
        return procTL(procP())
    elif expresion[0] == ")":
        return operator
    elif regex.match(r"(\||&)", expresion[0]):
        return operator
    elif regex.match(r'(=|!|<|>)', expresion[0]):
        return operator
    else:
        raise ValueError(f"Error Found in procTL with the character {expresion[0]}")
    pass

def procDivicion():
    global expresion
    symbol: str = expresion[0]
    match symbol:
        case _ if regex.match(r'[0-9]+', symbol) or symbol == "-":
            resultado = procDivisionL(procP())
            return resultado
        case _ if symbol == '(':
            return procDivisionL(procP()) 
        case _:
            raise ValueError(f"Error Found in procT with the character {expresion[0]}")
    pass


def procDivisionL(operator: int) -> int:
    global expresion
    if len(expresion) == 0:
        return operator
    # We have to check if the next operator is a multiplication 
    if expresion[0] == "/":
        advance("/")
        resultado = procDivisionL(procP())
        resultado = operator / resultado
        return resultado
    elif expresion[0] == "+" or expresion[0] == "-" or expresion[0] == "*":
        return operator
    elif expresion[0] == "(":
        return procTL(procP())
    elif expresion[0] == ")":
        return operator
    elif regex.match(r'(=|!|<|>)', expresion[0]):
        return operator
    elif regex.match(r"(\||&)", expresion[0]):
        return operator
    else:
        raise ValueError(f"Error Found in procDivisionL with the character {expresion[0]}")
    pass

def procP() -> int:
    global expresion
    symbol: str = expresion[0]
    match symbol:
        case _ if regex.match(r'[0-9]+', symbol) or symbol == "-":
            return procPL(procF())
        case _ if symbol == '(':
            return procPL(procF()) 
        case _:
            raise ValueError(f"Error Found in procP with the character {expresion[0]}")
    pass

def procPL(operator: int) -> int:
    global expresion
    if len(expresion) == 0:
        return operator
    symbol: str = expresion[0]
    match symbol:
        case '^':
            advance("^")
            numero = operator ** procPL(procF())
            return numero
        case _ if symbol == "*" or symbol == "/" or symbol == "+" or symbol == "-":
            return operator
        case _ if symbol == "":
            return operator
        case _ if regex.match(r'(=|!|<|>)', symbol):
            return operator
        case _ if symbol == ')':
            return operator
        case _ if regex.match(r"(\||&)", symbol):
            return operator
        case _:
            raise ValueError(f"Error Found in procPL with the character {expresion[0]}")
    pass

def procF() -> int:
    global expresion
    symbol: str = expresion[0]
    match symbol:
        case '(':
            advance("(")
            resultado = procELO()
            advance(")")
            return resultado
        case _ if regex.match(r'[0-9]+', symbol):
            return get_operator()
        case _ if symbol == "-":
            # Check if the next value is a number
            if regex.match(r'[0-9]+', expresion[1]):
                advance("-")
                numero = get_operator() * -1
                return numero
        case _:
            raise ValueError(f"Error Found in procF with the character {expresion[0]}")
        
def get_operator() -> int:
    global expresion
    operator: str = ""
    for i in expresion:
        if i in ["+", "*", ")", "^", "−", "-", "/", "<", ">", "=", "!", "|", "&"]: 
            break
        else:
            operator += i
    #print(f"get operator {operator}")
    expresion = expresion.replace(operator, "", 1)
    # Try to convert to int; if the value is double we try that too
    try:
        return int(operator)
    except ValueError:
        try:
            return float(operator)
        except ValueError:
            raise ValueError(f"Error Found in get_operator with the character {expresion[0]}")
    pass

def advance(symbol):
    global expresion
    if expresion[0] == symbol:
        expresion = expresion[1:]
    else:
        raise ValueError(f"Error Found in advance with the character {expresion[0]}")

def check(cadena: str) -> bool:
    prohibited_patterns = [
        r'[A-Za-z]+', # All types of letters 
    ]

    for pattern in prohibited_patterns:
        if regex.search(pattern, cadena):
            result: str = "letters" if regex.search(r'[A-Za-z]+', cadena) else "symbols"
            raise ValueError(f"Invalid expresion it contains {result}")

    return True
    
main()
