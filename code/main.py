from typing import List, Dict, Tuple, Optional, Union, Any, Callable
import re as regex

# Global exprecions
expresion: str = ""

def main():
    # Ask for the initial expression 
    user_expression = input("Enter the expresion: ")
    # Eliminate the blank spaces 
    user_expression = user_expression.replace(" ", "")
    # Update this "−" to "-"
    user_expression = user_expression.replace("−", "-")
    # This has to recognize arithmetic expressions only, we will check this with regex
    try:
        check(user_expression)
    except ValueError as e:
        print(e)
        return
    # If no strange symbols have been found we start the process
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
        if i in ["+", "*", ")", "^", "−", "-", "/"]: 
            break
        else:
            operator += i

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
