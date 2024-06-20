import re as regex
#hola medina 

pila = ["Fin"]
expresion: str = ""

def main():
    pila.append(procS)
    #ask for the initial exprecion 
    user_expression = input("Enter the expresion: ")
    #eliminate de blank spaces 
    user_expression = user_expression.replace(" ", "")
    #actualizate this "−" to "-"
    user_expression = user_expression.replace("−", "-")
    #this has to recognize aritmetic exprecions only we will check this with regex
    try:
        check(user_expression)
    except ValueError as e:
        print(e)
        return
    #if no extrange simboles have been found we start the process
    global expresion
    expresion = user_expression
    operate2()


def operate2():
    global pila
    index = 0
    while(True):
        top = pila[-1]
        if callable(top):
            top()
        else:
            advance(top)
            pila.pop()

        if pila[-1] == "Fin" and expresion == "":
            break
        index+=1


def procS():
    global pila
    pila.pop()
    añadirElemento(respuesta, 1)
    añadirElemento(getIndexOfBlanckeElement(), 0)
    añadirElemento(procE, 0)
    mostrar_lista_con_indices(pila, "1")
    pass

def respuesta():
    global pila
    pila.pop()
    #we try to convert the result to an int 
    try:
        resultadoFinal = pila[-1]
        pila.pop()
        mostrar_lista_con_indices(pila, "10")
        print(f"Resultado: {resultadoFinal}")
    except:
        raise ValueError("Error Found in respuesta")
    pass

def procE():
    global pila 
    pila.pop()
    añadirElemento(procEL, 1)
    añadirElemento(getIndexOfBlanckeElement(), 0)
    añadirElemento(procT, 0)
    mostrar_lista_con_indices(pila, "2")
    pass

def procEL():
    global pila 
    global expresion
    if len(expresion) == 0:
        symbol= " "
    else:
        symbol = expresion[0]
    match symbol:
        case "+":
            pila_operation_suma_resta(suma, symbol)
        case "-":
            pila_operation_suma_resta(resta, symbol)
            pass
        case ")":
            pila.pop()
            resultado = pila[-1]
            pila.pop()
            index = pila[-1]
            pila.pop()
            pila[index] = resultado
            mostrar_lista_con_indices(pila, "9")
            pass
        case " ":
            pila_non_operation_EL()
        case _:
            raise ValueError(f"Error Found in procEL with the character {expresion[0]}")
    pass

def pila_operation_suma_resta(operation, symbol):
    temporal = pila[-2]
    pila[-2] = " "
    añadirElemento(getIndexOfBlanckeElement(), 0)
    añadirElemento(temporal, 1)
    añadirElemento(operation, 0)
    añadirElemento(getIndexOfBlanckeElement(), 0)
    añadirElemento(procT, 0)
    advance(symbol)
    mostrar_lista_con_indices(pila, "11")


def suma():
    global pila
    pila.pop()
    operador1 = pila[-1]
    pila.pop()
    operador2 = pila[-1]
    pila.pop()
    index = pila[-1]
    pila.pop()
    pila[index] = operador1 + operador2
    mostrar_lista_con_indices(pila, "Suma")
    pass


def resta():
    global pila
    pila.pop()
    operador1 = pila[-1]
    pila.pop()
    operador2 = pila[-1]
    pila.pop()
    index = pila[-1]
    pila.pop()
    pila[index] = operador1 - operador2
    mostrar_lista_con_indices(pila, "Resta")
    pass

def pila_non_operation_EL():
    pila.pop()
    resultado = pila[-1]
    pila.pop()
    index = pila[-1]
    pila.pop()
    pila[index] = resultado
    mostrar_lista_con_indices(pila, "9")


def procT():
    global pila
    pila.pop()
    añadirElemento(procTL, 1)
    añadirElemento(getIndexOfBlanckeElement(), 0)
    añadirElemento(procP, 0)
    mostrar_lista_con_indices(pila, "3")
    pass

def procTL():
    global pila
    global expresion
    if len(expresion) == 0:
        symbol= " "
    else:
        symbol = expresion[0]
    match symbol:
        case "*":
            pila_operation_multiplication_divition(multiplicacion, symbol)
        case "/":
            pila_operation_multiplication_divition(divicion, symbol)
        case  _ if regex.match(r'[0-9]+', symbol):
            pila_non_operation_TL()
        case " ":
            pila_non_operation_TL()
        case ")":
            pila_non_operation_TL()
        case "+" | "-" | "−":
            pila_non_operation_TL()
        case _:
            raise ValueError(f"Error Found in procTL with the character {expresion[0]}")
    pass

def pila_operation_multiplication_divition(operation, symbol):
    operator = pila[-2]
    pila[-2] = " "
    añadirElemento(getIndexOfBlanckeElement(),0)
    añadirElemento(operator, 1)
    añadirElemento(operation,0)
    añadirElemento(getIndexOfBlanckeElement(), 0)
    añadirElemento(procP, 0)
    advance(symbol)
    mostrar_lista_con_indices(pila, "6")

def pila_non_operation_TL():
    pila.pop()
    resultado = pila[-1]
    pila.pop()
    index = pila[-1]
    pila.pop()
    pila[index] = resultado
    mostrar_lista_con_indices(pila, "6")

def multiplicacion():
    print("deberia multiplicar")
    global pila
    pila.pop()
    operador1 = pila[-1]
    pila.pop()
    operador2 = pila[-1]
    pila.pop()
    index = pila[-1]
    pila.pop()
    pila[index] = operador1 * operador2
    mostrar_lista_con_indices(pila, "7")    
    pass

def divicion():
    print("deberia dividir")
    global pila
    pila.pop()
    operador1 = pila[-1]
    pila.pop()
    operador2 = pila[-1]
    pila.pop()
    index = pila[-1]
    pila.pop()
    pila[index] = operador1 / operador2
    mostrar_lista_con_indices(pila, "8") 
    pass

def procP():
    global pila
    pila.pop()
    añadirElemento(procPL, 1)
    añadirElemento(getIndexOfBlanckeElement(), 0)
    añadirElemento(procF, 0)
    mostrar_lista_con_indices(pila, "13")
    pass

def procPL():
    global pila 
    global expresion
    if len(expresion) == 0:
        symbol= " "
    else:
        symbol = expresion[0]
    match symbol:
        case "^":
            pila_operation_exponencial(exponencial, symbol)
        case _ if regex.match(r'[0-9]+', symbol):
            pila_non_operation_PL()
        case " ":
            pila_non_operation_PL()
        case ")":
            pila_non_operation_PL()
        case "+" | "-" | "*" | "/" | "−":
            pila_non_operation_PL()
        case _:
            raise ValueError(f"Error Found in procPL with the character {expresion[0]}")
    pass

def exponencial():
    pila.pop()
    operador1 = pila[-1]
    pila.pop()
    operador2 = pila[-1]
    pila.pop()
    index = pila[-1]
    pila.pop()
    pila[index] = operador1 ** operador2
    mostrar_lista_con_indices(pila, "15")
    pass

def pila_operation_exponencial(operacion, symbol):
    global pila
    operador = pila[-2]
    pila[-2] = " "
    añadirElemento(getIndexOfBlanckeElement(), 0)
    añadirElemento(operador, 1)
    añadirElemento(operacion, 0)
    añadirElemento(getIndexOfBlanckeElement(), 0)
    añadirElemento(procF, 0)
    advance(symbol)
    mostrar_lista_con_indices(pila, "14")

def pila_non_operation_PL():
    pila.pop()
    resultado = pila[-1]
    pila.pop()
    index = pila[-1]
    pila.pop()
    pila[index] = resultado
    mostrar_lista_con_indices(pila, "12")
    pass

def procF():
    global pila
    global expresion
    symbol = expresion[0]
    match symbol:
        case _ if regex.match(r'[0-9]+', symbol):
            numero = get_operator()
            pila.pop()
            index = pila[-1]
            pila[index] = numero
            pila.pop()
            mostrar_lista_con_indices(pila, "16")
        case "-":
            #check if the next value is a number
            try: 
                nextSymbol = expresion[1]
                if regex.match(r'[0-9]+', nextSymbol):
                    advance("-")
                    numero = get_operator()
                    numero = numero * -1
                    pila.pop()
                    index = pila[-1]
                    pila[index] = numero
                    pila.pop()
                    mostrar_lista_con_indices(pila, "16")
                else:
                    raise ValueError(f"Error Found in procF with the character {expresion[0]}") 
            except:
                print("Error")
        case "(":
            pila.pop()
            temporal = pila[-1]
            pila.pop()
            añadirElemento(")", 0)
            añadirElemento(temporal, 0)
            añadirElemento(procE, 0)
            advance("(")
            mostrar_lista_con_indices(pila, "5")
            
        case _:
            raise ValueError(f"Error Found in procF with the character {expresion[0]}")
    pass


def mostrar_lista_con_indices(lista, operacion):
    print(f"Se aplica operacion {operacion}")
    for indice, elemento in enumerate(reversed(lista)):
        if callable(elemento):
            elemento = elemento.__name__
        print(f"{len(lista) - 1 - indice}: {elemento}")
    print("-----------------------------------------------")

def añadirElemento(elemento, espacios_en_blanco):
    global pila
    for i in range(espacios_en_blanco):
        pila.append(" ")
    pila.append(elemento)

def getIndexOfBlanckeElement():
    global pila
    for i in range(len(pila)):
        if pila[i] == " ":
            pila[i] = ""
            return i
    
def get_operator() -> int:
    global expresion
    operator:str = ""
    for i in expresion:
        if i in ["+", "*", ")", "^", "−", "-", "/"]: 
            break
        else:
            operator += i

    expresion = expresion.replace(operator, "", 1)
    print("getting operator: " + operator)
    #try to convert to int if the value is double we try that too
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
        r'[A-Za-z]+', #all tipes of letters 
    ]

    for pattern in prohibited_patterns:
        if regex.search(pattern, cadena):
            result: str = "letters" if regex.search(r'[A-Za-z]+', cadena) else "symbols"
            raise ValueError(f"Invalid expresion it contains {result}")

    return True


main()


