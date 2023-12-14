
import math

radio=float(input("Ingrese el radio: "))
perimetro=2*math.pi*radio
perimetro="{:.2f}".format(perimetro)
#esto es para mostrar solo dos decimales
area=math.pi*radio**2
area="{:.2f}".format(area)
#esto es para mostrar solo dos decimales

print("El perimetro es: "+str(perimetro))
print("El area es: "+str(area))