import copy
import math
import sys


def read_matrix_a_from_file(matrix_file_name):
    global n, a, diagonala_principala
    file = open(matrix_file_name, 'r')
    n = int(file.readline())
    for index in range(n):
        a.append(list())
    line = file.readline()
    while line:
        line_split = line.split(", ")
        value = float(line_split[0])
        row = int(line_split[1])
        column = int(line_split[2])
        if row != column:
            a[row].append([value, column])
        else:
            diagonala_principala.append([value, row])
        line = file.readline()


def read_b_vector_from_file(b_file_name):
    global b, n
    file = open(b_file_name, 'r')
    for index in range(n):
        line = file.readline()
        b.append(float(line))


def verifica_diagonala_principala():
    global diagonala_principala, precizie, n
    if len(diagonala_principala) < n:
        print("Diagonala principala contine un numar mic de elemente nenule")
        sys.exit(0)
    for number in diagonala_principala:
        if number[0] < precizie:
            print("Elemente nule pe diagonala principala")
            sys.exit(0)


def verifica_convergenta(x, next_x):
    global precizie
    for index, value in enumerate(x):
        if abs(value - next_x[index]) > precizie:
            return False
    return True


# def suma_4(index, x):
#     global a
#     suma = 0
#     for element_matrice_rara in a[index]:
#         column = element_matrice_rara[1]
#         if column < index - 1:
#             suma += element_matrice_rara[0] * x[column]
#     return suma


# def suma_5(index, x):
#     global a, n
#     suma = 0
#     for row_index in range(index + 1, n):
#         for element_matrice_rara in a[row_index]:
#             column_index = element_matrice_rara[1]
#             if column_index == index:
#                 suma += element_matrice_rara[0] * x[row_index]
#                 break
#     return suma


def suma_jacobi(xk):
    global a, n, b, diagonala_principala
    xk1 = copy.deepcopy(b)
    for row_index in range(n):
        for element_matrice_rara in a[row_index]:
            column_index = element_matrice_rara[1]
            value = element_matrice_rara[0]
            xk1[row_index] -= value * xk[column_index]
            xk1[column_index] -= value * xk[row_index]
    for index in range(n):
        a_ii = diagonala_principala[index][0]
        xk1[index] = xk1[index] / a_ii
    return xk1


# def get_element_diagonala_principala(index):
#     global diagonala_principala
#     for element in diagonala_principala:
#         if element[1] == index:
#             return element[0]
#     print("Am gasit element nul pe diagonala principala")
#     sys.exit(0)


def metoda_jacobi():
    global n, x_solutie, b
    x_k = list()
    for index in range(n):
        x_k.append(0)
    iter = 4000
    k = 0
    while True:
        x_k_1 = suma_jacobi(x_k)
        k += 1
        # print(k)
        # print("####")
        if verifica_convergenta(x_k, x_k_1):
            x_k = copy.copy(x_k_1)
            print(x_k)
            print("Converge in numarul de pasi:" + str(k))
            break
        x_k = copy.copy(x_k_1)
        if k > iter:
            print("Nu converge in numarul de pasi " + str(k))
            break
    x_solutie = copy.copy(x_k)



def norma():
    global a, b, n, x_solutie
    b_solutie = list()
    for index in range(n):
        suma = 0
        for element_a in a[index]:
            column_index = element_a[1]
            suma += element_a[0] * x_solutie[column_index]
        suma += diagonala_principala[index][0] * x_solutie[index]

        b_solutie.append(suma)
    suma2 = 0
    for index in range(n):
        suma2 += abs(b_solutie[index] - b[index]) ** 2
    nrm = math.sqrt(suma2)
    print("Norma: " + str(nrm))


n = 0
a = list()
diagonala_principala = list()
b = list()
x_solutie = list()
precizie = 0.1 ** 5


def main():
    global x_solutie
    read_matrix_a_from_file("a_1.txt")
    read_b_vector_from_file("b_1.txt")
    verifica_diagonala_principala()
    metoda_jacobi()
    norma()


main()
