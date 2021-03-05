#Lista para la validación pan-digital
lista1 = ['1','2','3','4','5','6','7','8','9']

comparacion_primero = []
comparacion_ultimo  = []

# funcion de fibonacci
def fib(k):
    f1 = 0
    f2 = 1
    
    for i in range(k):
        fn = f1+f2
        f1 = f2
        f2 = fn
    return f2

a=[]


# While que valida los numeros del 1 al 9 tanto de primeras como de últimas pan-digital
i = 1
while len(a) ==0:  
    b = str(fib(i))
    if len(b) > 9:
    	#Transforma y extrae caracteres
        primeros = list(b[:9])
        ultimos  = list(b[-9:])

        #Valida primeros carcateres
        for item in lista1:
            if item in primeros:
                comparacion_primero.append(item)
        #Valida últimos caracteres
        for item in lista1:
            if item in ultimos:
                comparacion_ultimo.append(item)
        #Condicional si los primeros 9 digitos son pan-digital y los últimos también inserta el i
        if len(comparacion_ultimo) == 9:
            if len(comparacion_primero) == 9:
                a.append(str(i))
    i = i + 1
    comparacion_primero = []
    comparacion_ultimo  = []
    print(i)

#imprime lista a con el valor de i
print(a)