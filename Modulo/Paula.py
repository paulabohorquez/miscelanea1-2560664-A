def nombre_aprendiz(nom):
    print("bienvenido",nom,"al programa ADSO")

def edad_aprendiz(año_actual,año_nacimiento):
    edad=año_actual - año_nacimiento
    if edad<14:
        print("no puede acceder al sena") 
    elif edad>=14:
        print("si puede ingresar al sena")
    print("usted tiene: ",edad, "años")
 


import random
def usuario(id):
    chars=(random.choice(["gyuji59867","lñpoy201364","swaqe89546","gcxers01478"]))
    print("su usuario es:",id, "y su contraseña es: ",chars)

def indice_masa_corporal(p,a):
    imc=p/(a*a)
    if imc<18.5:
        print("bajo peso")
    elif 18.5<= imc <=24.9:
        print("normal")
    elif 25<= imc <=29.9:
        print("sobrepeso")
    elif 30<= imc <=34.9:
        print("obesidad I") 
    elif 35<= imc <=34.9:
        print("obesidad")
    elif 40<= imc <=49.9:
        print("obesidad II")
    elif imc >=50:
        print("obesidad IV")
        print("su nivel de peso es: ",indice_masa_corporal(p,a),imc)

def iva(valor):
    total=valor*0.19
    print("el precio total con el iva es: ",total)





            




    




    

