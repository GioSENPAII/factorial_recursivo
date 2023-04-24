def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)

print(factorial_recursivo(5))

#De acuerdo al teorema del Maestro este algoritmo tiene una complejidad de O(logn) ya que primero "a" tiene una cantidad de llamados recursivos de 1, después n/b es igual a n
#por lo tanto b=1 y finalmente tenemos que O(1) ya que las operaciones son en tiempo constante, por lo tanto c=0
#Finalmente sustituyendo tenemos que O(logn).
