from tabulate import tabulate

libros={1: ['LOS JUEGOS DEL HAMBRE', 'SUZANNE COLLINS', 'CIENCIA FICCION', '1/8/2010', 4235436343, '22/3/2022'],
        2: ['LAS AVENTURAS DE PINOCHO', 'CARLO COLLODI', 'NOVELA','5/2/1890', 1932453229 , '1/4/2020'],
        3: ['BAJO LA MISMA ESTRELLA', 'JOHN GREEN', 'NOVELA', '10/1/2012', 1359230542, '11/9/2022']}

while True:
    print("")
    print("Menu principal")
    print("")
    print("1.-Registrar Nuevo Ejemplar\n2.-Consulta y Reportes\n3.-Salir")
    opcion=int(input("¿Que opcion desea?: "))
        
    if (opcion==1):
        print("")
        id=max(libros,default=0)+1
        Titulo=input("Ingrese el nombre del titulo: ")
        Autor=input("Ingrese el nombre del autor: ")
        Genero=input("Ingrese el genero del libro: ")
        fecha_publicacion=input("Ingrese la fecha de publicacion: ")
        isbn=int(input("Ingrese el ISBN del libro: "))
        fecha_adquisicion=input("Ingrese la fecha de Adquisicion: ")
        libros[id]=[Titulo,Autor,Genero,fecha_publicacion,isbn,fecha_adquisicion]
        continue
        print("")
        
        
    if (opcion==2):
        while True:
            print("")
            print("Menu Consultas y Reportes")
            print("")
            print("1.-Consulta del titulo\n2.-Reportes\n3.-Menu principal")
            opcion2=int(input("Seleccione una opcion: "))
                
            if (opcion2==1):
                while True:
                    print("")
                    print("Menu Consulta Titulo")
                    print("1.-Por Titulo\n2.-Por ISBN\n3.-Menu Anterior")
                    opcion3=int(input("Seleccione una opcion: "))
                    if (opcion3==1):
                        tabla=[]
                        if bool(libros):
                            Titulo_busqueda=input("Que Titulo desea buscar: ")
                            for id, datos in libros.items():
                                if Titulo_busqueda == datos[0]:
                                    tabla.append([id] + datos)

                            if tabla:
                                print(tabulate(tabla, headers=["ID", "Titulo", "Autor", "Genero", "Fecha de publicacion", "ISBN", "Fecha de ingreso a la libreria"]))
                                break
                            else:
                                print("No se encontro ningun titulo con el nombre proporcionado ")
                                break
                        else:
                            print('El diccionario está vacío')
                            break
                        
                        
                    if (opcion3==2):
                        tabla=[]
                        if bool(libros):
                            ISBN_busqueda=int(input("Que ISBN desea buscar: "))
                            for id, datos in libros.items():
                                if ISBN_busqueda == datos[4]:
                                    tabla.append([id] + datos)

                            if tabla:
                                print(tabulate(tabla, headers=["ID", "Titulo", "Autor", "Genero", "Fecha de publicacion", "ISBN", "Fecha de ingreso a la libreria"]))
                                break
                            else:
                                print("No se encontro ningun libro con el ISBN proporcionado")
                                break
                        else:
                            print('El diccionario está vacío')
                            break

                    
                    if (opcion3==3):
                        break
                    
                    if (opcion3>3 or opcion3<1):
                        print("Opcion no valida.")
                        continue
                
            if (opcion2==2):
                while True:
                    print("")
                    print("Menu Reportes")
                    print("")
                    print("1.-Catalogo Completo\n2.-Reporte por Autor\n3.-Reporte por genero\n4.-Reporte por Año de Publicacion\n5.-Menu Anterior")
                    opcion4=int(input("Seleccione una opcion: "))
                    print("")
                    if (opcion4==1):
                        tabla = []
                        if bool(libros):
                            for id, datos in libros.items():
                                tabla.append([id] + datos)
                            print(tabulate(tabla, headers=["ID", "Titulo", "Autor", "Genero", "Fecha de publicacion", "ISBN", "Fecha de ingreso a la libreria"]))
                        else:
                            print('El diccionario está vacío')
                          
                    if (opcion4==2):
                        tabla=[]
                        if bool(libros):
                            Autor_busqueda=input("Ingresa el autor el cual desea buscar: ")
                            for id, datos in libros.items():
                                if Autor_busqueda == datos[1]:
                                    tabla.append([id] + datos)

                            if tabla:
                                print(tabulate(tabla, headers=["ID", "Titulo", "Autor", "Genero", "Fecha de publicacion", "ISBN", "Fecha de ingreso a la libreria"]))
                            else:
                                print("No se encontraron resultados para el autor buscado")
                        else:
                            print('El diccionario está vacío')
                        
                          
                    if (opcion4==3):
                        tabla=[]
                        if bool(libros):
                            genero_busqueda=input("Ingresa el genero el cual desea buscar: ")
                            for id, datos in libros.items():
                                if genero_busqueda == datos[2]:
                                    tabla.append([id] + datos)

                            if tabla:
                                print(tabulate(tabla, headers=["ID", "Titulo", "Autor", "Genero", "Fecha de publicacion", "ISBN", "Fecha de ingreso a la libreria"]))
                            else:
                                print("No se encontro ningun genero con el nombre proporcionado")
                        else:
                            print('El diccionario está vacío')
                        
                        
                    if (opcion4==4):
                        tabla = []
                        if bool(libros):
                            Publicacion_busqueda = input("¿Qué año de publicación desea buscar?: ")
                            for id, datos in libros.items():
                                if Publicacion_busqueda == datos[3]:
                                    tabla.append([id] + datos)

                            if tabla:
                                print(tabulate(tabla, headers=["ID", "Título", "Autor", "Género", "Fecha de publicación", "ISBN", "Fecha de ingreso a la librería"]))
                            else:
                                print("No se encontro el año de publicación buscado")
                        else:
                            print('El diccionario está vacío')
                        
                    if (opcion4==5):
                        break
                        
                    if (opcion4<1 or opcion4>3):
                        print("Opcion no valida.")
                        continue
               
            if (opcion2==3):
                break   
                          
            if (opcion2<1 or opcion2>3):
                print("Opcion no valida")
                continue
      
    if (opcion==3):
        break
     
    if (opcion>3 or opcion<1):
        print("Opcion no valida")
        continue

while True:
    print("")
    print("Menu principal")
    print("")
    print("1.-Registrar Nuevo Ejemplar\n2.-Consulta y Reportes\n3.-Salir")
    opcion=int(input("¿Que opcion desea?: "))
        
    if (opcion==1):
        print("")
        id=max(libros,default=0)+1
        Titulo=input("Ingrese el nombre del titulo: ")
        Autor=input("Ingrese el nombre del titulo: ")
        Genero=input("Ingrese el genero del libro: ")
        fecha_publicacion=input("Ingrese la fecha de publicacion: ")
        isbn=int(input("Ingrese el ISBN del libro: "))
        fecha_adquisicion=input("Ingrese la fecha de Adquisicion: ")
        libros[id]=[Titulo,Autor,Genero,fecha_publicacion,isbn,fecha_adquisicion]
        continue
        print("")
        
        
    if (opcion==2):
        while True:
            print("")
            print("Menu Consultas y Reportes")
            print("")
            print("1.-Consulta del titulo\n2.-Reportes\n3.-Menu principal")
            opcion2=int(input("¿Que opcion desea?: "))
                
            if (opcion2==1):
                while True:
                    print("")
                    print("Menu Consulta Titulo")
                    print("1.-Por Titulo\n2.-Por ISBN\n3.-Menu Anterior")
                    opcion3=int(input("Seleccione una opcion: "))
                    if (opcion3==1):
                        tabla=[]
                        if bool(libros):
                            Titulo_busqueda=input("Que Titulo desea buscar: ")
                            for id, datos in libros.items():
                                if Titulo_busqueda == datos[0]:
                                    tabla.append([id] + datos)

                            if tabla:
                                print(tabulate(tabla, headers=["ID", "Titulo", "Autor", "Genero", "Fecha de publicacion", "ISBN", "Fecha de ingreso a la libreria"]))
                                break
                            else:
                                print("No se encontro ningun titulo con el nombre proporcionado ")
                                break
                        else:
                            print('El diccionario está vacío')
                            break
                        
                        
                    if (opcion3==2):
                        tabla=[]
                        if bool(libros):
                            ISBN_busqueda=int(input("Que ISBN desea buscar: "))
                            for id, datos in libros.items():
                                if ISBN_busqueda == datos[4]:
                                    tabla.append([id] + datos)

                            if tabla:
                                print(tabulate(tabla, headers=["ID", "Titulo", "Autor", "Genero", "Fecha de publicacion", "ISBN", "Fecha de ingreso a la libreria"]))
                                break
                            else:
                                print("No se encontro ningun libro con el ISBN proporcionado")
                                break
                        else:
                            print('El diccionario está vacío')
                            break

                    
                    if (opcion3==3):
                        break
                    
                    if (opcion3>3 or opcion3<1):
                        print("Opcion no valida.")
                        continue
                
            if (opcion2==2):
                while True:
                    print("")
                    print("Menu Reportes")
                    print("")
                    print("1.-Catalogo Completo\n2.-Reporte por Autor\n3.-Reporte por genero\n4.-Reporte por Año de Publicacion\n5.-Menu Anterior")
                    opcion4=int(input("Seleccione una opcion: "))
                    print("")
                    if (opcion4==1):
                        tabla = []
                        if bool(libros):
                            for id, datos in libros.items():
                                tabla.append([id] + datos)
                            print(tabulate(tabla, headers=["ID", "Titulo", "Autor", "Genero", "Fecha de publicacion", "ISBN", "Fecha de ingreso a la libreria"]))
                        else:
                            print('El diccionario está vacío')
                          
                    if (opcion4==2):
                        tabla=[]
                        if bool(libros):
                            Autor_busqueda=input("Ingresa el autor el cual desea buscar: ")
                            for id, datos in libros.items():
                                if Autor_busqueda == datos[1]:
                                    tabla.append([id] + datos)

                            if tabla:
                                print(tabulate(tabla, headers=["ID", "Titulo", "Autor", "Genero", "Fecha de publicacion", "ISBN", "Fecha de ingreso a la libreria"]))
                            else:
                                print("No se encontraron resultados para el autor buscado")
                        else:
                            print('El diccionario está vacío')
                        
                          
                    if (opcion4==3):
                        tabla=[]
                        if bool(libros):
                            genero_busqueda=input("Ingresa el genero el cual desea buscar: ")
                            for id, datos in libros.items():
                                if genero_busqueda == datos[2]:
                                    tabla.append([id] + datos)

                            if tabla:
                                print(tabulate(tabla, headers=["ID", "Titulo", "Autor", "Genero", "Fecha de publicacion", "ISBN", "Fecha de ingreso a la libreria"]))
                            else:
                                print("No se encontro ningun genero con el nombre proporcionado")
                        else:
                            print('El diccionario está vacío')
                        
                        
                    if (opcion4==4):
                        tabla = []
                        if bool(libros):
                            Publicacion_busqueda = input("¿Qué año de publicación desea buscar?: ")
                            for id, datos in libros.items():
                                if Publicacion_busqueda == datos[3]:
                                    tabla.append([id] + datos)

                            if tabla:
                                print(tabulate(tabla, headers=["ID", "Título", "Autor", "Género", "Fecha de publicación", "ISBN", "Fecha de ingreso a la librería"]))
                            else:
                                print("No se encontro el año de publicación buscado")
                        else:
                            print('El diccionario está vacío')
                        
                    if (opcion4==5):
                        break
                        
                    if (opcion4<1 or opcion4>3):
                        print("Opcion no valida.")
                        continue
               
            if (opcion2==3):
                break   
                          
            if (opcion2<1 or opcion2>3):
                print("Opcion no valida")
                continue
      
    if (opcion==3):
        break
     
    if (opcion>3 or opcion<1):
        print("Opcion no valida")
        continue
