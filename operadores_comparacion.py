"""
Operadores de comparación en Python
OR ( cuando al menos una condicion es verdadera)
AND ( cuando todas las condiciones son verdaderas)
== : Igual a
!= : Diferente de
>  : Mayor que
<  : Menor que
>= : Mayor o igual que
<= : Menor o igual que
"""
# ejemplo con el operador OR
a = 5
b = 3
c = 8
if a > b or a > c:
    print(f"{a} es mayor que {b} o {c}")
else:
    print(f"{a} no es mayor que {b} ni {c}")