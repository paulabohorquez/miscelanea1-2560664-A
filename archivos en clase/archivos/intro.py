'''Los archivos son un conjunto de caracteres y bytes almacenados en archivos y carpetas '''
flujo=open('archivos/1.txt','a') #se instancia un objeto, con una ruta relativa de la ubicacion del archivo
#datos=flujo.read() en la variable datos queda almacenado el objeto y utilizaremos un metodo read para leer el archivo
#print(datos) #se imprime
flujo.write('\nCuando estudian con juicio') # con el objeto utilizaremos el metodo para escribir n el archivo lo que esta entre parentesis y pondremos un salto de linea
datos=flujo.read() #en la variable datos con el metodo read podrmos leer lo que se encuentra en el archivo
print(datos) #se imprime el contenido del archivo