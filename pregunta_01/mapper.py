#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
# Compute la cantidad de registros por cada tipo del atributo `credit_history` 
# usando el algoritmo Map/Reduce.
import sys

if __name__ == "__main__":

    for row in sys.stdin:
            sys.stdout.write("{}\t1\n".format(row.split(",")[2]))
