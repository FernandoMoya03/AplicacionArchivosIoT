import json
import datetime
from PersonasClase import Persona as P
from ArticulosClase import Articulo as A

p=P()
a=A()

class Prestamo:
    aidi = 0
    ListaPrestamos = []
    data = {}
    data['ListaPrestamos'] = []

    def __init__(self, folio=None, miembro=None, articulo=None, cantidad=None, fPrestamo=None, devuelto=None, fDevolucion=None):
        self.folio     = folio
        self.miembro   = miembro
        self.articulo  = articulo
        self.cantidad  = cantidad
        self.fPrestamo = fPrestamo
        self.devuelto       = False
        self.fDevolucion    = ""

    def RegistroPrestamo(self, miembro, articulo, cantidad, fecha):
        self.aidi += 1
        newPrestamo = Prestamo(self.aidi, miembro, articulo, cantidad, fecha)
        self.ListaPrestamos.append(newPrestamo)
        self.data['ListaPrestamos'].append(encoderPrestamo(newPrestamo))
        with open('dataPrestamos.json', 'w') as file:
            json.dump(self.data, file, indent=4)
        for p in self.ListaPrestamos:
            if self.aidi == p.folio:
                return newPrestamo
    
    def RegistroDevolucion(self, folio):
        i = 0
        for r in self.ListaPrestamos:
            if folio == r.folio:
                fecha = str(datetime.datetime.now())
                r.devuelto = True
                r.fDevolucion = fecha
                miembro = r.miembro
                articulo = r.articulo
                cantidad = r.cantidad
                disponibles = p.PrestamosDisponibles(miembro, 1)
                if disponibles:
                    disponibles = a.CantidadInventario(articulo, cantidad)
                    return True
        return False
                
    
    def VerPrestamos(self):
        with open('dataPrestamos.json') as f:
            listillaJSON = json.load(f)
            for li in listillaJSON['ListaPrestamos']:
                newPrestamo = Prestamo(li['folio'],li['miembro'],li['articulo'],li['cantidad'],li['fPrestamo'],li['devuelto'],li['fDevolucion'])
                self.ListaPrestamos.append(newPrestamo)
        return self.ListaPrestamos

    def ValidarDatosPrestamo(self, miembro,articulo,cantidad):
        #Validar que haya usuarios y tengan prestamos disponibles
        pase = p.ValidarDatosPersona(miembro)
        if pase:
            pase =a.ValidarDatosArticulo(articulo,cantidad)
            if pase:
                disponibles = p.PrestamosDisponibles(miembro, -1)
                if disponibles:
                    disponibles = a.CantidadInventario(articulo, -cantidad)
                    return True
        else: False
          
def encoderPrestamo(prestamo):
  if isinstance(prestamo,Prestamo):
    return {
      'folio'       : prestamo.folio,
      'miembro'     : prestamo.miembro,
      'articulo'    : prestamo.articulo,
      'cantidad'    : prestamo.cantidad,
      'fPrestamo'   : prestamo.fPrestamo,
      'devuelto'    : prestamo.devuelto,
      'fDevolucion' : prestamo.fDevolucion
    }
  raise TypeError(f'El objeto {prestamo} no es de tipo Persona')