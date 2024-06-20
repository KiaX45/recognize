from typing import List, Dict, Tuple, Optional, Union, Any, Callable
import re as regex

#Global exprecions
expresion: str = ""

def main():
    #ask for the initial exprecion 
    user_expression = input("Enter the expresion: ")
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


#Metodos primera sección 
def procELO() -> bool:
    global expresion
    symbol = expresion[0]
    match symbol:
        case _ if symbol == "(" or regex.match(r'[0-9]+', symbol) or symbol == "!":
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
        case _:
            raise ValueError(f"Error Found in procELO_L with the character {expresion[0]}")
            
    pass


def procEL2() -> bool:
    global expresion
    symbol: str = expresion[0]
    match symbol:
        case _ if regex.match(r'[0-9]+', symbol) or symbol== "(" or symbol == "!":
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
        case _ if symbol == "|":
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
        case _ if regex.match(r'[0-9]+', symbol) or symbol== "(":
            return procER()
        case _:
            raise ValueError(f"Error Found in EL3 with the character {expresion[0]}")


#Fin metodos primera sección


#Metodos segunda sección
def procER():
    global expresion
    symbol: str = expresion[0]
    match symbol:
        case _ if regex.match(r'[0-9]+', symbol):
            result = procERL(procE())
            print(result)
            return result
        case _ if symbol == "(":
            return procERL(procE())
        case _:
            raise ValueError(f"Error Found in procER with the character {expresion[0]}")
    pass

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
            return operator
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


#Fin Metodos segunda sección

def procE() -> int:
    global expresion
    symbol: str = expresion[0]
    match symbol:
        case _ if regex.match(r'[0-9]+', symbol):
            resultado = procEL(procT())
            print(resultado)
            return resultado
        case _ if symbol == '(':
            return procEL(procT()) 
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
            print("procEL deberia")
            #in this postion we have to do the addition with the return of the next function
            advance("+")
            numero = operator + procEL(procT())
            print("numero:" + str(numero))
            return(numero)
        case _ if regex.match(r'(=|!|<|>)', symbol):
            return operator
        case _ if regex.match(r"(\||&)", symbol):
            return operator
        case _ if symbol == "":
            return operator
        case _ if symbol == ')':
            return operator
        case _:
            raise ValueError(f"Error Found in procEL with the character {expresion[0]}")
    pass

def procT() -> int:
    global expresion
    symbol: str = expresion[0]
    match symbol:
        case _ if regex.match(r'[0-9]+', symbol):
            print("procT " + symbol)
            return procTL(procP())
        case _ if symbol == '(':
            print("Si")
            return procTL(procP()) 
        case _:
            raise ValueError(f"Error Found in procT with the character {expresion[0]}")
    pass

def procTL(operator: int) -> int:
    global expresion
    if len(expresion) == 0:
        return operator
    #we have to check if the next operator is an multiplication 
    if expresion[0] == "*":
        print("proc TL No")
        advance("*")
        return (operator * procTL(procP()))
    elif expresion[0] == "/":
        print("proc TL Si")
        advance("/")
        return (operator / procTL(procP()))
    elif expresion[0] == "+" or expresion[0] == "-":
        print("proc TL " + str(operator))
        return operator
    elif regex.match(r'(=|!|<|>)', expresion[0]):
        return operator
    elif regex.match(r"(\||&)", expresion[0]):
        return operator
    elif expresion[0] == "(":
        print("proc TL Si (")
        return procTL(procP())
    elif expresion[0] == ")":
        print("proc TL Si )")
        return operator
    else:
        raise ValueError(f"Error Found in procTL with the character {expresion[0]}")

    pass

def procP() -> int:
    global expresion
    symbol: str = expresion[0]
    match symbol:
        case _ if regex.match(r'[0-9]+', symbol):
            print("procT " + symbol)
            return procPL(procF())
        case _ if symbol == '(':
            print("Si")
            return procTL(procP()) 
        case _:
            raise ValueError(f"Error Found in procT with the character {expresion[0]}")
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
            print("numero:" + str(numero))
            return(numero)
        case _ if symbol == "*" or symbol == "/" or symbol =="+" or symbol == "-":
            return operator
        case _ if regex.match(r'(=|!|<|>)', symbol):
            return operator
        case _ if regex.match(r"(\||&)", symbol):
            return operator
        case _ if symbol == "":
            return operator
        case _ if symbol == ')':
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
            resultado = procE()
            advance(")")
            return resultado
        case _ if regex.match(r'[0-9]+', symbol):
            return(get_operator())

def get_operator() -> int:
    global expresion
    operator:str = ""
    for i in expresion:
        if i in ["+", "*", ")", "^", "-", "/", ">", "<", "=", "!", "|", "&"]:
            break
        else:
            operator += i

    expresion = expresion.replace(operator, "", 1)
    print("getting operator: " + operator)
    return int(operator)
    pass

def advance(symbol):
    global expresion
    if expresion[0] == symbol:
        expresion = expresion[1:]
    else:
        raise ValueError(f"Error Found in advance with the character {expresion[0]}")


def check(cadena: str) -> bool:
    prohibited_patterns = [
        r'[A-Za-z]+', #all tipes of letters 
    ]

    for pattern in prohibited_patterns:
        if regex.search(pattern, cadena):
            result: str = "letters" if regex.search(r'[A-Za-z]+', cadena) else "symbols"
            raise ValueError(f"Invalid expresion it contains {result}")

    return True
    

main()



