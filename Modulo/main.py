from Paula import nombre_aprendiz, edad_aprendiz, usuario, indice_masa_corporal, iva

nom=(input('ingrese nombre completo: '))
nombre_aprendiz(nom)

año_actuall=2023
año_nacimientoo=(int(input("ingrese su año de nacimiento: ")))
edad_aprendiz(año_actuall,año_nacimientoo)

identificacion=input("ingrese el numero de su documento de identidad: ")
usuario(identificacion)

peso=float(input("ingrese su peso: "))
altura=float(input("ingrese su altura: "))
indice_masa_corporal(peso,altura)

precio=(int(input("ingrese el valor de su compra: ")))
iva(precio)