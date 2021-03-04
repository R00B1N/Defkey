#!/usr/bin/python

#importamos los modulos que vamos a utilizar.
import os
import time
import wpspin
import subprocess
from colorama import Fore, init
init()

os.system('cls')

print(Fore.RED)

banner = """
██████╗ ███████╗███████╗██╗  ██╗███████╗██╗   ██╗
██╔══██╗██╔════╝██╔════╝██║ ██╔╝██╔════╝╚██╗ ██╔╝
██║  ██║█████╗  █████╗  █████╔╝ █████╗   ╚████╔╝ 
██║  ██║██╔══╝  ██╔══╝  ██╔═██╗ ██╔══╝    ╚██╔╝  
██████╔╝███████╗██║     ██║  ██╗███████╗   ██║   
╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝   
"""

print(banner)
print(Fore.GREEN)
print("Created by Blackster\n")
print("This tool was created for purposes only.")

print(Fore.CYAN)

#Creamos una funcion para nuestro menu principal.
def switch():
	menu = """
1-Generar password Router Movistar.
2-Generar password Router ZTE.
3-Generar Password Router Huawei.
4-Generar Password Router DirecTV.
"""
	print(menu)

#Creamos otra funcion para nuestros condicionales.
def switch_1():
	switch()
	ask = int(input("Escoge una opcion>> "))
	#Este es el primer condicional de la funcion.
	if ask==1:
		menu = """
		1- Un solo pin + password por defecto.
		2- Todos los pines + password por defecto.
		"""
		print(menu)
		ask_1 = int(input("Escoge una opcion >> "))
		if ask_1==1:
			mac = str(input("Introduce aqui tu MAC >> "))
			mov = 'M'
			convert = (mov+mac.upper())
			import subprocess
			print(Fore.GREEN)
			#Se llama el subprocess para que la consola pueda cumplir con el comando proporcionado.
			subprocess.call(f'wpspin {mac}', shell=True)
			con_1 = convert[0:3]
			con_2 = convert[4:6]
			con_3 = convert[7:9]
			con_4 = convert[10:12]
			con_5 = convert[13:15]
			con_6 = convert[16:18]
			con_all = (con_1+con_2+con_3+con_4+con_5+con_6)

			#Hacemos la conversion inversa de la contraseña generada anteriormente.
			p_1 = convert[4:6]
			p_2 = convert[0:3]
			p_3 = convert[10:12]
			p_4 = convert[7:9]
			p_5 = convert[16:18]
			p_6 = convert[13:15]
			password = (mov+p_1+p_2+p_3+p_4+p_5+p_6)
			print(Fore.GREEN)
			#se imprime la salida del condicional.
			print("\nTu password por defecto para esta MAC es >> " + con_all + " << O prueba tambien con " + password)


		elif ask_1==2:
			mac = str(input("Introduce aqui tu MAC >> "))
			mov = 'M'
			convert = (mov+mac.upper())
			import subprocess
			print(Fore.GREEN)
			subprocess.call(f'wpspin -A {mac}', shell=True)
			con_1 = convert[0:3]
			con_2 = convert[4:6]
			con_3 = convert[7:9]
			con_4 = convert[10:12]
			con_5 = convert[13:15]
			con_6 = convert[16:18]
			con_all = (con_1+con_2+con_3+con_4+con_5+con_6)
			print(Fore.GREEN)
			#se imprime la salida del condicional.
			print("\nTu password por defecto para esta MAC es >> " + con_all)

	#Segundo condicional de esta funcion.
	elif ask==2:
		menu = """
		1- Un solo pin + password por defecto.
		2- Todos los pines + password por defecto.
		"""
		print(menu)
		ask_2 = int(input("Escoge una opcion >> "))
		if ask_2==1:
			mac = str(input("Introduce aqui tu MAC >> "))
			zte = 'Z'
			convert = (zte+mac.upper())
			import subprocess
			print(Fore.GREEN)
			subprocess.call(f'wpspin {mac}', shell=True)
			con_1 = convert[0:3]
			con_2 = convert[4:6]
			con_3 = convert[7:9]
			con_4 = convert[10:12]
			con_5 = convert[13:15]
			con_6 = convert[16:18]
			con_all = (con_1+con_2+con_3+con_4+con_5+con_6)
			print(Fore.GREEN)
			print("\nTu password por defecto para esta MAC es >> " + con_all)

		elif ask_2==2:
			mac = str(input("Introduce aqui tu MAC >> "))
			zte = 'Z'
			convert = (zte+mac.upper())
			import subprocess
			print(Fore.GREEN)
			subprocess.call(f'wpspin -A {mac}', shell=True)
			con_1 = convert[0:3]
			con_2 = convert[4:6]
			con_3 = convert[7:9]
			con_4 = convert[10:12]
			con_5 = convert[13:15]
			con_6 = convert[16:18]
			con_all = (con_1+con_2+con_3+con_4+con_5+con_6)
			print(Fore.GREEN)
			#se imprime la salida del condicional.
			print("\nTu password por defecto para esta MAC es >> " + con_all)

	#tercer condicional de la funcion.
	elif ask==3:
		menu = """
		1- Un solo pin + password por defecto.
		2- Todos los pines + password por defecto.
		"""
		print(menu)
		ask_3 = int(input("Escoge una opcion >> "))
		if ask_3==1:
			mac = str(input("Introduce aqui tu MAC >> "))
			Hua = 'H'
			convert = (Hua+mac.upper())
			import subprocess
			print(Fore.GREEN)
			subprocess.call(f'wpspin {mac}', shell=True)
			con_1 = convert[0:3]
			con_2 = convert[4:6]
			con_3 = convert[7:9]
			con_4 = convert[10:12]
			con_5 = convert[13:15]
			con_6 = convert[16:18]
			con_all = (con_1+con_2+con_3+con_4+con_5+con_6)
			print(Fore.GREEN)
			print("\nTu password por defecto para esta MAC es >> " + con_all)

		elif ask_3==2:
			mac = str(input("Introduce aqui tu MAC >> "))
			Hua = 'H'
			convert = (Hua+mac.upper())
			import subprocess
			print(Fore.GREEN)
			subprocess.call(f'wpspin -A {mac}', shell=True)
			con_1 = convert[0:3]
			con_2 = convert[4:6]
			con_3 = convert[7:9]
			con_4 = convert[10:12]
			con_5 = convert[13:15]
			con_6 = convert[16:18]
			con_all = (con_1+con_2+con_3+con_4+con_5+con_6)
			print(Fore.GREEN)
			#se imprime la salida del condicional.
			print("\nTu password por defecto para esta MAC es >> " + con_all)

	#Cuarto condicional para nuestra funcion.
	elif ask==4:
		menu = """
		1- Un solo pin + password por defecto.
		2- Todos los pines + password por defecto.
		"""
		print(menu)
		ask_4 = int(input("Escoge una opcion >> "))
		if ask_4==1:
			mac = str(input("Introduce aqui tu MAC >> "))
			Dtv = 'D'
			convert = (Dtv+mac.upper())
			import subprocess
			print(Fore.GREEN)
			subprocess.call(f'wpspin {mac}', shell=True)
			con_1 = convert[0:3]
			con_2 = convert[4:6]
			con_3 = convert[7:9]
			con_4 = convert[10:12]
			con_5 = convert[13:15]
			con_6 = convert[16:18]
			con_all = (con_1+con_2+con_3+con_4+con_5+con_6)
			print(Fore.GREEN)
			#se imprime la salida del condicional.
			print("\nTu password por defecto para esta MAC es >> " + con_all)

		elif ask_4==2:
			mac = str(input("Introduce aqui tu MAC >> "))
			Dtv = 'D'
			convert = (Dtv+mac.upper())
			import subprocess
			print(Fore.GREEN)
			subprocess.call(f'wpspin -A {mac}', shell=True)
			con_1 = convert[0:3]
			con_2 = convert[4:6]
			con_3 = convert[7:9]
			con_4 = convert[10:12]
			con_5 = convert[13:15]
			con_6 = convert[16:18]
			con_all = (con_1+con_2+con_3+con_4+con_5+con_6)
			print(Fore.GREEN)
			print("\nTu password por defecto para esta MAC es >> " + con_all)

switch_1() #se llama a la funcion en general para que se pueda cumplir todas las condiciones.