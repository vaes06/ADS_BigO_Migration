# ADS_BigO_Migration
Curso Ambientes de desarrollo de software. Migración de repositorio BigOnotation a python.

# Complejidad logarítmica O(log n)
Son los algoritmos que presentan mayor rápidez. Por definición, un problema de complejidad O(logx n) necesita una número de 
 pasos igual al exponente de la base X tal que X**exponente = n. En otras palabras el exponente es el número de pasos que el algoritmo 
 necesita para encontrar el resultado. Sin importar cual sea la base X el log n siempre va a ser considerablemente menor que n. 
 Ejemplo: log2 (2 000 000) = 20.93 ,  log10 (2 000 000) = 6.30 Un problema que en complejidad O(n) tomaría 2 000 000 de pasos sólo necesita
 21 pasos en base 2  o 7 pasos en base 10. A pesar de ser la opción ideal para desarrollar un algoritmo, no siempre se puede aplicar
 ya que puede que se necesite que se cumplan ciertos requisitos, como es el caso de la búsqueda binaraia, que necesita que la lista a la 
 que se le va a aplicar el algoritmo se encuentre odernada.

# Complejidad exponencial O(c**N)
Se dá en el caso del algoritmo recursivo de los números de Fibonacci. Comienza con un número de pasos cortos, pero como en cada iteración 
tiene que calcular todos los números anteriores dos veces, la complejidad de cáculo se incrementa de manera rápida, de manera exponencial.
A diferencia de la complejidad logarítmica, la cual requiere un número bajo de pasos para un n mucho mayor, la complejidad exponencial requiere un número c**n de pasos, un múmero mucho mayor al n. Como se mencionó antes, en el algoritmo recursivo de Fibonacci, se realizan dos iteraciones en cada paso tiene una complejidad O(2**n). Para un n de tamaño 25 se requieren 33 554 432 de pasos. Si un algoritmo presenta esta complejidad es importante no usarlo o buscar otras alternativas.
