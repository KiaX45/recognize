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
    print(procE())
    pass

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
        if i in ["+", "*", ")", "^", "-", "/"]:
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


