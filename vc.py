def posicion0(longitud, vector, cero, copia,pos,vE):
    lista=[]
    vector2= vector.copy()
    # valor de copia
    valor = int(cero)
    #si valor es igual a uno
    if valor == 1:
        print('\nNivel:',pos,'\nvector de colision', vector)
        if pos == 0:
            #eliminar el ultimo valor de la lista
            copia.pop()
            copia.reverse()
            #agregar un cero a la lista
            copia.append('0')
            copia.reverse()
            #comparar y agregar en una nueva lista el valor 
            for i in range(longitud):
                if vector[i] == '0' and copia[i] == '0':
                    lista.append('0')
                else:
                    lista.append('1')
            print('vector de posicion', copia,'\nvector calculado  ', lista)
            copia2 = lista.copy()
            lista.reverse()
            for i in range(vE):
                pos2=0
                pos2=i
                posicion1(longitud, vector2, lista[i], copia2, pos2)                           
        else:
            for i in range(longitud):
                if vector[i] == '0' and copia[i] == '0':
                    lista.append('0')
                else:
                    lista.append('1')
            print('vector de posicion', copia,'\nvector calculado  ', lista)
            copia.pop()
            copia.reverse()
            copia.append('0')
            copia.reverse()
            copia2 = lista.copy()
            lista.reverse()
            for i in range(vE):
                pos2=0
                pos2=i
                posicion1(longitud, vector2, lista[i], copia2, pos2)  
    else:
        copia.pop()
        copia.reverse()
        copia.append('0')
        copia.reverse()
        return

def posicion1(longitud, vector2, uno, copia2, pos2):
    lista2=[]
    # valor de cero
    valor = int(uno)
    #si valor es igual a uno
    if valor == 1:
        print('\n     Nivel Derivado:',pos2,'\n     vector de colision', vector)
        if pos2 == 0:
            #eliminar el ultimo valor de la lista
            copia2.pop()
            copia2.reverse()
            #agregar un cero a la lista
            copia2.append('0')
            copia2.reverse()
            #comparar y agregar en una nueva lista el valor 
            for i in range(longitud):
                if vector2[i] == '0' and copia2[i] == '0':
                    lista2.append('0')
                else:
                    lista2.append('1')
            print('     vector de posicion', copia2,'\n     vector calculado  ', lista2)
        else:
            #print('-------vector de posicion',copia2)
            for i in range(longitud):
                if vector2[i] == '0' and copia2[i] == '0':
                    lista2.append('0')
                else:
                    lista2.append('1')
            print('     vector de posicion', copia2,'\n     vector calculado  ', lista2)
            #eliminar el ultimo valor de la lista
            copia2.pop()
            copia2.reverse()
            #agregar un cero a la lista
            copia2.append('0')
            copia2.reverse()
    else:
        copia2.pop()
        copia2.reverse()
        copia2.append('0')
        copia2.reverse()
        return

#inicializacion de los datos
vector=['']
cero = []
uno = []
longitud = -1
k=0
x=1
# le decimos al usuario que ingrese su input de colision
entrada = input('Ingrese los valores del vector colision: ')
#el largo de la entrada
valor_entrada = len(entrada)
#convertir nuestra entrada a lista
vector = list(entrada)

#validacion de la cantidad de vectores colisiona mostrar
if valor_entrada < 19:

    #copiamos la lista
    for i in range(valor_entrada):
        cero.append(i+1)
        uno.append(i+2)
    # cambiar los valores de la lista de cero y determinar la longitud
    for i in range(valor_entrada):
        #si existe un cero en el vector 
        if vector[i] == '0':
            #agregar a cero la posicion que se encuentre i 
            cero[i]=k
        #si existe un 1 en el vector
        if vector[i] == '1':
            uno[i]=x

    #longitud del vector
    longitud=len(vector)

    #copia del vector
    copia = vector.copy()
    copia2 = vector.copy()

    # imprimir la longitud del vector de colision y su vector
    print('longitud: ', longitud)

    #invirtiendo posiciones del 0 y uno
    cero.reverse()
    uno.reverse()

    for i in range(valor_entrada):
        pos=0
        pos=i
        posicion0(longitud,vector, uno[i], copia, pos,valor_entrada)

else:
    #imprimir un mensaje de error 
    print('Agregaste mas 18 posiciones del vector\nCantidad de posiciones colocadas: ', valor_entrada)
    #salir
    exit()