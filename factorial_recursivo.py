def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)

print(factorial_recursivo(5))

#Este algoritmo no puedo ser analizado con el teroema del Maestro ya que en primer lugar no se tiene un arreglo y termina en orden exponencial de acuerdo a la Big O.
