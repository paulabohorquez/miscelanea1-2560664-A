class pedido:
    def __init__(self, id_usuario, titulo_material,cod_material,fecha_reserva,fecha_entrega,modificar):
        self.__id_ususario=id_usuario
        self.__titulo_material=titulo_material
        self.__cod_material=cod_material
        self.__fechas=[]
    def reservar(self,fecha_reserva):
        self.__fechas.append(fecha_reserva)
    def entregar(self,fecha_entrega):
        self.__fechas.append(fecha_entrega)
    def modificar(self,fecha_entrega):
        del self.__fecha_entrega
        self.fechas.append(fecha_entrega)
    def ver_fecha(self):
        return self.__fechas
    
class lector:
    def __init__(self,id_usuario,nombre, direccion,telefono):
        self.__id_usuario=id_usuario
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono






    
a=pedido(45,'python',689,5-11-21,11-11-21,'no')
print