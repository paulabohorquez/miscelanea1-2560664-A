biblioteca=[]
class pedido:
    biblioteca=[]
    def __init__(self, id_usuario, titulo_material,cod_material,fecha_reserva,fecha_entrega):
        self.__id_ususario=id_usuario
        self.__titulo_material=titulo_material
        self.__cod_material=cod_material
        self.__fecha_reserva=fecha_reserva
        self.__fecha_entrega=fecha_entrega
        self.__biblioteca=[]
    def registrar_fechas(self):
        self.__biblioteca.append(self.__fecha_reserva)
        self.__biblioteca.append(self.__fecha_entrega)

    def getfechas(self):
        return 'fecha de reserva y entrega del material ',self.__biblioteca

    def modificar(self, nueva):
        self.__biblioteca.pop() 
        self.__biblioteca.append(nueva)
        return 'se ha modificado la fecha de entrega del material', self.__biblioteca

class Lector:
    def __init__(self, id_usuario,nombre,direccion,telefono,titulo_material):
        mat=[]
        self.__id_usuario=id_usuario
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
        self.__titulo_material=titulo_material
        self.__mat=[]
    def getusuario(self):
        if self.__id_usuario==1:
            return  'id de usuario' ,self.__id_usuario, 'es un estudiante'
        elif self.__id_usuario==2:
            return 'id de usuario' ,self.__id_usuario, 'es un docente'
        else:
            return 'no existe el usuario'
             
        
    def getreserva_material(self):
        self.__mat.append(self.__titulo_material)
        return    'el material es:', self.__titulo_material

    def modificar(self, a):
        self.__mat.pop() 
        self.__mat.append(a)
        return 'se ha modificado el material', self.__mat

class estudiante(Lector):
    def __init__(self, id_usuario, nombre, direccion, telefono, titulo_material):
        Lector.__init__(self,id_usuario, nombre, direccion, telefono, titulo_material)
    def est(self,a):
        return super().getusuario() ,super().getreserva_material(),super().modificar(a)

class docente(Lector):
    def __init__(self, id_usuario, nombre, direccion, telefono, titulo_material):
        Lector.__init__(self,id_usuario, nombre, direccion, telefono, titulo_material)
    def doc(self,a):
        return super().getusuario() ,super().getreserva_material(),super().modificar(a)
    
class materiales(pedido):
    
    def __init__(self,id_material,titulo,tipo,autor,editorial,fec_res,fec_ent):
        fechass=[]
        self.__id_material=id_material
        self.__titulo=titulo
        self.__tipo=tipo
        self.__autor=autor
        self.__editorial=editorial
        self.__fec_res=fec_res
        self.__fec_ent=fec_ent
        self.__fechass=[]
    
    def getfecha_materiales(self):
        self.__fechass.append(self.__fec_ent)
        self.__fechass.append(self.__fec_res)
        return 'fecha de reserva y entrega de material',self.__fechass
    def idmaterial(self):
        if self.__id_material==3:
            return 'es una revista',self.__id_material
        elif self.__id_material==4:
            return 'es una revista ',self.__id_material
        else:
            return 'el id no existe'

class revista(materiales):
    def __init__(self, id_material, titulo, tipo, autor, editorial, fec_res, fec_ent):
        materiales.__init__(self,id_material, titulo, tipo, autor, editorial, fec_res, fec_ent)
    def rev(self):
        return super().idmaterial(), super().getfecha_materiales()

class libro(materiales):
    def __init__(self, id_material, titulo, tipo, autor, editorial, fec_res, fec_ent):
        materiales.__init__(self,id_material, titulo, tipo, autor, editorial, fec_res, fec_ent)
    def lib(self):
        return super().idmaterial(), super().getfecha_materiales()

class bibliotecario:
    lista=[]
    def __init__(self,id_personal,fecha_reserva,fecha_entrega):
        self.__id_personal=id_personal
        self.__fecha_reserva=fecha_reserva
        self.__fecha_entrega=fecha_entrega
        self.__lista=[]
    def fechas(self):
        self.__lista.append(self.__fecha_reserva)
        self.__lista.append(self.__fecha_entrega)
        return 'id personal',self.__id_personal,'fechas',self.__lista
    def modificar(self, a):
        self.__lista.pop() 
        self.__lista.append(a)
        return 'se ha modificado el material', self.__lista



       
b=pedido(12, 'cuatro', 123, '12/12/23','02/05/23')
b.registrar_fechas()
print(b.getfechas())
print(b.modificar('12-11-22'))
c=Lector(1, 'paula','carrera 17', 12345,'cuatro')
print(c.getreserva_material())
print(c.modificar('tres'))
d=estudiante(1, 'paula','carrera 17', 12345,'cuatro')
print(d.est('cinco'))
e=docente(8, 'sofia','carrera 15', 54321,'seis')
print(e.doc('siete'))
d=materiales(3, 'bebe', 'terror', 'alfonso', 'el bosque','12/12/23','02/05/23')
print(d.getfecha_materiales())
e=revista(3, 'vea', 'farandula', 'francisco', 'torres', '12/12/23','02/05/23')
print(e.rev())
f=libro(4, 'pajarito', 'infantil', 'rafael', 'torres', '12/12/23','02/05/23')
print(f.lib())
g=bibliotecario(54, '12/12/23','02/05/23')
print(g.fechas())
print(g.modificar('04/12/23'))
