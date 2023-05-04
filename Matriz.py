import numpy
import os

package_dir = os.path.dirname(os.path.realpath(__file__))
with open(package_dir+"/Matriz.txt") as file:
    matrix = file.readlines()
    matrix = [line.strip() for line in matrix]
    file.close()
    print(matrix)

num_matrix = int(matrix[0])
print(num_matrix)

line=1
y = [] #lista vazia
for i in range(num_matrix):
    limM,colM = matrix[line].split(";")
    print(limM, " - ", colM)
    y.append(limM)
    line +=1
    for j in range(int(limM)):
        line +=1

line = 2
a = [] #outra lista vazia
try:
    for s in range(num_matrix):

        print("-----------------------------")
        for s in range(num_matrix-1):
            element = matrix[line].split(",") # element é todos os itens da lista [['1', '2', '3', '4', '5']......['1', '2']]
            print(element)
            a.append(element)# aqui ele vai colocar todos os elementos dentro de a (acho q n precisa dessa variável "a" )
            line +=1
        line +=1
except:
    print("============")
print(y)# Y = ['3', '3', '3', '2']
g = int(y[0]) # "g" é o primeiro valor de y, no caso 3
i=0
mat1 = [] # lista vazia
while i < g: #enquanto i for menor que 3
    mat1.append(a[i]) #a lista vazia vai recever o valor de "a" de acordo com " i " nesse caso sera ['1', '2', '3', '4', '5'], ['6', '7', '8', '9', '10'], ['11', '12', '13', '14', '15']
    i+=1
print("zzzzzzzzzzzzzzzzzzzzzzzz")
print(mat1)# mat1 agora ta com as listas da primeira matriz

#determinante

# lista = []
# for elemento in matriz:
#     if ";" in elemento:
#         elemento.append(lista)
#         size = lista
#         print("Nova variável criada: ", size)



#tamanho_matriz = matriz[1]
#print(tamanho_matriz)


