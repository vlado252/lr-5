import math
a = float(input("Введи значение первого основания:"))
b = float(input("Введи значение второго основания:"))
c = float(input("Введи значение одной стороны:"))
d = float(input("Введи значение второй стороны:"))
p = (a+b+c+d)/2
print("Полупериметр = ",p)
S =((a+b)/(math.fabs(a-b)))*(math.sqrt((p-a)*(p-b)*(p-a-c)*(p-a-d)))
print("Площадь трапеции = ",S)