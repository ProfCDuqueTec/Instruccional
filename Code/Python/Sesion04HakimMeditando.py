import numpy

numeros = numpy.zeros(5) # crear un arreglo de 5 elementos todos en 0

nombre = "Camilo"

i = 0
mensaje = "Hakim>> Dame un número entero para la posición [ " + str(i) + " ] ?\n" + nombre + ">> " 
numeros[i] = int(input(mensaje))

i = 1
mensaje = "Hakim>> Dame un número entero para la posición [ " + str(i) + " ] ?\n" + nombre + ">> " 
numeros[i] = int(input(mensaje))

i = 2
mensaje = "Hakim>> Dame un número entero para la posición [ " + str(i) + " ] ?\n" + nombre + ">> " 
numeros[i] = int(input(mensaje))

i = 3
mensaje = "Hakim>> Dame un número entero para la posición [ " + str(i) + " ] ?\n" + nombre + ">> " 
numeros[i] = int(input(mensaje))

i = 4
mensaje = "Hakim>> Dame un número entero para la posición [ " + str(i) + " ] ?\n" + nombre + ">> " 
numeros[i] = int(input(mensaje))

print("Hakim>> El arreglo de números es:")
print(numeros)

print("Hakim>> Las tareas que puedo hacer por ti son:")
print("Tarea\t\t\t\t\tOpción")
print("Dimensiones del arreglo\t\t..[1]")
print("Ordenar el arreglo\t\t\t..[2]")
print("Máximo del arreglo\t\t\t..[3]")
print("Mínimo del arreglo\t\t\t..[4]")
print("# de Ceros en el arreglo\t\t..[5]")
mensaje = "Hakim>> Qué quieres que haga?\n" + nombre + ">> "
opcion = int(input(mensaje))

if opcion == 1:
  dim = numpy.size(numeros)
  print("Hakim>> La dimensión del arreglo es:")
  print(dim)
elif opcion == 2:
  num2 = numpy.sort(numeros)
  print("Hakim>> El arreglo ordenado es:")
  print(num2)
elif opcion == 3:
  maxi = numpy.argmax(numeros)
  print("Hakim>> El maximo es: %d " % numeros[maxi])
  print("Hakim>> y esta en posicion %d" % maxi)
elif opcion == 4:
  mini = numpy.argmin(numeros)
  print("Hakim>> El minimo es: %d " % numeros[mini])
  print("Hakim>> y esta en posicion %d" % mini)
elif opcion == 5:
  numzeros = numpy.size(numeros) - numpy.count_nonzero(numeros)
  print("Hakim>> Hay %d ceros " % numzeros)
else:
  print("Hakim>> Con esa opción voy a descansar... Jajaja")