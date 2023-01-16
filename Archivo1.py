from time import sleep

print("CARGANDO SOWFARE ..")
sleep(2)
print("CARGANDO SOWFARE ...")
sleep(2)
print("CARGANDO SOWFARE ......")
sleep(3)
print("\n\n")
print("Descarga Exitosa".center(50))
print("\n\n")


x = input("Cual es tu nombre: ")
print("\n")

c = input(f"Bienvenido Al Sistema {x} En que puedo ayudarte :  ")
print("\n")

if(c == "sistema inteligente"):
	print("Cargando Sistema Inteligente")
else:
	print("Lo siento no he entendido la pregunta".center(50).upper())