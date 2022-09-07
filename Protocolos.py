pasos = []
subpasos = []
contador = 1
subcontador = 1.1
def menu():
    print("""---------Creador de protocolos-------------------
1.-Agregar paso a protocolo
2.-Borrar paso de protocolo
3.-Ver protocolo
0.-Salir
""")
def agreg():
    posi=int(input("Escriba la posicion en la que desea añadir el dato: "))
    paso = input("Escribe el paso que quieras agregar al protocolo: ")
    pasos.insert(posi,paso)
    print("------Protocolo------")
    for i in range (0,(len(pasos))):
            print("---> "+pasos[i])
def elim():
    pasoe = input("Escribe el paso que quieras eliminar: ")
    inde=int((pasos.index(pasoe)))
    pasos.pop(inde)
    print("-----Protocolo-----")
    for i in range (0,(len(pasos))):
            print("---> "+pasos[i])
def ver():
    for i in range (0,(len(pasos))):
            print("---> "+pasos[i])
    
    
while(True):  
    menu()
    resp = int (input("Escribe la opción que deseas utilizar: "))
    if resp == 1:
        agreg()
    elif resp == 2:
        elim()
    elif resp == 3:
        ver()
    elif resp == 0:
        print("Hasta luego")
        break
    
    
    
        
        
