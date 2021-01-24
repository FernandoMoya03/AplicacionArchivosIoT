import json

class Persona:
  aidi = 0
  ListaUsuario = []
  data = {}
  data['ListaUsuario'] = []

  def __init__(self, Id=None, name=None, email=None, cel=None, prestamo=None):
    self.Id    = Id
    self.name  = name
    self.email = email
    self.cel   = cel
    self.prestamos  = 2
  
  def RegistroPersona(self, nombre, correo, cel):
    self.aidi += 1
    newUsuario = Persona( self.aidi, nombre, correo, cel)
    self.ListaUsuario.append(newUsuario)
    self.data['ListaUsuario'].append(encoderPersona(newUsuario))
    with open('dataPersonas.json', 'w') as file:
      json.dump(self.data, file, indent=4)
    return newUsuario
  
  def VerPersonas(self):
    with open('dataPersonas.json') as f:
      listillaJSON = json.load(f)
      for li in listillaJSON['ListaUsuario']:
        newUsuario = Persona(li['Id'],li['name'],li['email'],li['cel'],li['prestamos'])
        self.ListaUsuario.append(newUsuario)
    return self.ListaUsuario


  def ValidarDatosPersona(self, miembro):
    for m in self.ListaUsuario:
      if miembro == m.Id:
        if m.prestamos > 0:
          return True
        else: print("Prestamo no Hecho, Ya no cuenta con mas prestamos...")
        break
    return print("Prestamo no Hecho, Usuario no registrado")

  def PrestamosDisponibles(self, miembro, prestamosD):
    for m in self.ListaUsuario:
      if miembro == m.Id:
        m.prestamos += prestamosD
        return True
    return False



def encoderPersona(persona):
  if isinstance(persona,Persona):
    return {
      'Id'        : persona.Id,
      'name'      : persona.name,
      'email'     : persona.email,
      'cel'       : persona.cel,
      'prestamos' : 3
    }
  raise TypeError(f'El objeto {persona} no es de tipo Persona')