name = input("Ingresa un nombre: ")

question = name + "¿cuantos años tienes? "

print("¡Hola "+ name+"!")
age = input(question)  

if int(age) >= 18:
    print("Fuaaa ya eres ¡MAYOR!")
else:
    print('Aun eres pequeño')                          