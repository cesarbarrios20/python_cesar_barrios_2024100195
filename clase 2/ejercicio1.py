'''
Crear un programa que pida dos numeros
y obtenga como resultado cual de ellos es par o si
ambos los on
'''
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

if((num1 % 2 == 0)and (num2 % 2 == 0)):
    print("Ambos numero son pares")
elif((num1 % 2 == 0) and (num2 % 2 != 0)):
    print(f"{num1} es par")
    print(f"{num2} es impar")
elif((num1 % 2 != 0) and (num2 % 2 == 0)):
    print(f"{num1} es impar")
    print(f"{num2} es par")
else:
    print("Ambos numero son impares")