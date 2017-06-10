import random #importamos la libreria ramdom que ocuparemos para que nos de numeros al azar 

continuar = 1  #le decimos al usuario que 1 es para empezar el juego

while continuar == 1: #imprimimos mensajes para que el jugador elija  la dificultad 
	print("bienvenido a master mind")
	print("elija la dificultad  del juego <1=Facil, 2=Dificil, 3=Muy Dicifil")
	dificultad = int(input("Digite el Numero de Dificultad: "))
	if dificultad == 1: 
		cant_digitos = 3 #si elije la dificultad 1, se le asignaran 3 digitos al azar
	elif dificultad == 2:
		cant_digitos = 4  #si elije la dificultad 2, se le asignaran 4 digitos al azar
	elif dificultad == 3:
		cant_digitos = 5  #si elije la dificultad 3, se le asignaran 5 digitos al azar
		
	digitos = ('0','1','2','3','4','5','6','7','8','9')  # en esta seccion le decimos al programa que elija entre numeros del 0 al 9
	codigo = ''
	
	for i in range(cant_digitos):
		elegido = random.choice(digitos) #aqui escoje los digitos dependiendo de la dificultad que el usuario hayya escogido
		while elegido in codigo:
			elegido = random.choice(digitos)
		codigo = codigo + elegido
	
	print("tienes que adivinar un codigo de: ", cant_digitos, "distintos digitos") #aqui le decimos al usuario que tiene que adivinar un codigo y le decimos de cuantos digitos es el numero a adivinar
	propuesta = input("que codigo propones?")   #le pedimos al usuario que ingrese un codigo con digitos al azar 
	
	intentos = 1  #acumnulamos intentos en caso de equivocarse
	
	while propuesta != codigo:    #aqui obtenemos el codigo que el usuario intriduce
		intentos = intentos + 1    #cada error es un intento mas que se suma
		aciertos = 0        #declaramos aciertos en 0 e ira incrementando de acuerdo a los aciertos que tenga el usario
		coincidencias = 0   #coincidencias son los digitos que esten correctos pero mal ordenados
		for i in range(cant_digitos):
			if propuesta[i] == codigo[i]:    
				aciertos = aciertos + 1  #si el usuario tiene un acierto el programa indica que tiene 1 acierto
			elif propuesta[i] in codigo:
				coincidencias = coincidencias + 1  # el usuario tiene numeros que si estan el codigo pero estan mal ordenados
		print("tu propuesta(",propuesta,")tiene",aciertos,    #imprimimos en pantalla al usuario la cantidad de aciertos y coincidencias que tiene su codigo introducido
			"aciertos y ", coincidencias,"coincidencias")
		propuesta = input("propon otro codigo: ")    #le pedimos que introduzca otro codigo

	print("FELICIDADES! adivinaste el codigo en ",intentos,"intentos")  #finalmente cuando acierta al codigo se le imprime un mensaje de felicitaciones y le muestra la cantidad de intentos que hizo para acertar al codigo
	continuar = int(input("desea seguir jugando?: <1= si, 0=no>:"))  #imprimimos en pantalla la opcion de si quiere o no seguir jugando ...
	
	
	#aqui finaliza el codigo  del pequeño juego echo en python}
	# development by BadUser97
	#ISCJUANLUIS
	#SolucionInformatica Express
	#Powered By Thonny Pyhton 2.7
