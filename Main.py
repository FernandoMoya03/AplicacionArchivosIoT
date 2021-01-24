
import datetime
from PersonasClase import Persona as P
from ArticulosClase import Articulo as A
from PrestClase import Prestamo as L
a = A()
p = P()
l = L()
menu = True



def Prestamos(miembro,articulo,cantidad):
    datval = l.ValidarDatosPrestamo(miembro,articulo,cantidad)
    if datosValidados:
        fecha = str(datetime.datetime.now())
        prestamo = l.RegistroPrestamo(miembro, articulo, cantidad, fecha)
        print("Registro Exitoso|Folio del prestamo: "+str(prestamo.folio))
    else: print(datval)
def Devoluciones(folio):
    devolucion = l.RegistroDevolucion(folio)
    if devolucion:
      print('Devolucion Completada... ')
    else: print('No se pudo hacer la devolucion, Favor de verificar su folio...')
#MODIFICADO CORRECTAMENTE
def RegistrarUsuario():
    persona = p.RegistroPersona(nombre, correo, cel)
    print(" Bienvenido " + persona.name + " Se ha registrado correctamente, Su numero de ID es: " + str(persona.Id))
#MODIFICADO CORRECTAMENTE
def RegistrarArticulo():
    a.RegistroArticulo(articulo, inventario)
#MODIFICADO CORRECTAMENTE
def VerInventario():
    listaArt= a.VerArticulos()
    for articulo in listaArt:
        print(articulo.articulo+"-"+str(articulo.inventario))
#MODIFICADO CORRECTAMENTE    
def VerUsuario():
    ListaPer = p.VerPersonas()
    for miembro in ListaPer:
        print(miembro.name+" - "+miembro.email+" - "+miembro.cel)
#MODIFICADO CORRECTAMENTE     
def VerPrestamos():
    ListaL = l.VerPrestamos()
    for pres in ListaL:
        print("Folio: "+str(pres.folio)+" - "+"Usuario: "+str(pres.miembro)+" - "+"Articulo: "+str(pres.articulo)+" - "+"Cantidad: "+str(pres.cantidad)+" - "+"Fecha de Prestamo: "+pres.fPrestamo+" - "+"Fecha de Devolucion: "+pres.fDevolucion)

while menu == True:
    print(" --- MENU GENERAL --- ")
    print("1.- Nuevo Prestamo ")
    print("2.- Devolucion   ")
    print("3.- Registrar Usuario ")#
    print("4.- Registrar Articulo")#
    print("5.- Ver inventario")#
    print("6.- Ver Miembros")#
    print("7.- Ver Prestamos")
    print("0.- Salir")
    accion = input("Seleccion la accion a realizar: "); print()
    if accion in ("1","2","3","4","5","6","7","0"):
        accion = int(accion)
        if accion == 1:
            print("  ------ REGISTRAR NUEVO PRESTAMO ------ ")
            miembro  = int(input("ID Miembro: "))
            articulo = int(input("Articulo: "))
            cantidad = int(input("Cantidad: "))
            Prestamos(miembro,articulo,cantidad)
        elif accion == 2:
            print("  ------ DEVOLUCION ------ ")
            folio = int(input("Folio del Prestamo Asignado: "))
            Devoluciones(folio)
        elif accion == 3:
            #REVISION COMPLETADA
            print(" ----- REGISTRAR NUEVO USUARIO ----- ")
            nombre = input("Nombre: ")
            correo = input("Correo Electronico: ")
            cel    = input("Telefono / Celular: ")
            RegistrarUsuario()
        elif accion == 4:
            #REVISION COMPLETADA
            print(" ----- REGISTRAR ARTICULO ----- ")
            articulo   = input("Articulo: ")
            inventario = int(input("Cantidad: "))
            RegistrarArticulo()
        elif accion == 5:
            #REVISION COMPLETADA
            print("  --- INVENTARIO EXISTENTE --- ")
            VerInventario()

        elif accion == 6:
            #REVISION COMPLETADA
            print(" -------- VER MIEMBROS EXISTENTES ---------")
            VerUsuario()
            #REVISION COMPLETADA
        elif accion == 7:
            print(" ------- VER PRESTAMOS EXISTENTES ------- ")
            VerPrestamos()
        else:
            print("MUCHAS GRACIAS, VUELVA PRONTO!!....")
            menu = False
                
    else: print("NUMERO ERRONEO, SELECCIONE UN NUMERO DENTRO DEL MENU")
else: print("CERRANDO....")