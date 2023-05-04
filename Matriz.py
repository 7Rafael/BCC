import numpy
import os

package_dir = os.path.dirname(os.path.realpath(__file__))
with open("Matriz.txt") as file:
    num_matrix = int(file.readline())
    print( "Tem ", num_matrix," Matrizes:" )
    matrixName = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    
    matrixes = []
    matrix_x = []
    
    linha = 1
    for i in range(num_matrix):
        limM, colM = file.readline().strip().split(';')
        print( "O número de linhas e colunas da matrix", matrixName[i], "é:", limM, "-", colM + ":")

        a = []
        for i in range(int(limM)):
            element = file.readline().strip().split(',')
            a.append(element)
        matrix = numpy.array(a, dtype=float)
        print( 'Temos a matrix', matrixName[i], 'com os seguintes valores: \n', '-------------------- \n', matrix, '--------------------' )
        if matrix.shape[0] == matrix.shape[1]:
            det = numpy.linalg.det(matrix)
            print( 'O determinante da matriz', matrixName[i], ' é: ', det)
            if det == 0:
                print( 'a', matrixName[i], 'apresenta um det igual a zero, assim não é possível calcular a inversa')
            else:
                print( 'a matrix', matrixName[i], 'apresenta sua inversão sendo igual a', numpy.linalg.inv(matrix))
        else:
            print( 'Não da para calculcar a det: ', matrixName[i])
            print( 'Não da para calcular a inversão de: ', matrixName[i])

        matrixes.append(matrix)
        matrix_x.append(matrixName[i])
        linha += 1

    for i in range(num_matrix - 1):
        if matrixes[i].shape[1] == matrixes[i+1].shape[0]:
            result = numpy.dot(matrixes[i], matrixes[i+1])
            matrix_x.append(matrix_x[i] + matrix_x[i+1])
            matrixes.append(result)
            print( 'A multiplicação das matrixes', matrix_x[i], 'e', matrix_x[i+1], 'resultou na matrix', matrix_x[i] + matrix_x[i+1], '\n', '-------------------- \n', result, '--------------------' )
        else:
            print( 'Não foi possível multiplicar as matrixes', matrix_x[i], 'e', matrix_x[i+1])
