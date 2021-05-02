#Ejercicio 3, de la pagina 31: 2.15 EJERCICIOS 
"""Pedir horas y tarifa por hora
   para ver el salario bruto """

smsHoras = "Buenas, por favor ingrese la cantidad de horas de trabajo: \n"
smsTarifa = "Ahora ingrese la tarifa por hora : \n"
smsSalario = "El salario bruto es de:"

Horas = input(smsHoras)
Tarifa = input(smsTarifa)

Horas = float(Horas)
Tarifa = float(Tarifa)

Salario = Horas * Tarifa 
Salario = round(Salario)      #"round" para redondear numeros

print(smsSalario, Salario)

