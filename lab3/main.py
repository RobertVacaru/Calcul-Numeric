import numpy as numpy


class Node:
    def __init__(self, value, col):
        self.value = value
        self.col = col

    def print(self):
        print("{" + f'{self.col}' + ":" + f'{self.value}' + "}")


class Sparse:
    def __init__(self, list_matrix, size):
        self.list_matrix = list_matrix
        self.size = size

    def print(self):
        for i in range(self.size):
            print("Line:" + f'{i}')
            for j in range(len(self.list_matrix[i])):
                self.list_matrix[i][j].print()


def add_lines(line1, line2):
    final_line = []
    k = 0
    p = 0
    n = len(line1)
    m = len(line2)
    while True:
        if line1[k].col == line2[p].col:
            final_line.append(Node(line1[k].value + line2[p].value, line2[p].col))
            k += 1
            p += 1
        elif line1[k].col < line2[p].col:
            final_line.append(Node(line1[k].value, line1[k].col))
            k += 1
        else:
            final_line.append(Node(line2[p].value, line2[p].col))
            p += 1
        if k >= n - 1:
            break
        if p >= m - 1:
            break
    if p == m:
        while k != n:
            final_line.append(Node(line1[k].value, line1[k].col))
            k += 1
    if k == n:
        while p != m:
            final_line.append(Node(line2[p].value, line2[p].col))
            p += 1
    return final_line


def add_matrix(a, b, n):
    c = []
    for i in range(n):
        # print(a.list_matrix[0])
        # print(len(b.list_matrix))
        line = add_lines(a.list_matrix[i], b.list_matrix[i])
        c.append(line)
    return c


def get_info_txt(f):
    file = open(f, "r")
    n = file.readline()
    line = file.readline()
    matrix = numpy.zeros((int(n), int(n)))

    while line:
        line = file.readline()
        if line != '':
            line = line[:len(line) - 1]
            data = line.split(", ")
            value = float(data[0])
            i = int(data[1])
            j = int(data[2])
            if matrix[i][j] != 0:
                matrix[i][j] += value
            else:
                matrix[i][j] = value
            if j != i:
                if matrix[j][i] != 0:
                    matrix[j][i] += value
                else:
                    matrix[j][i] = value
    file.close()
    return matrix, int(n)


def generate_economic_matrix(matrix, n):
    economy_matrix = []
    for i in range(n):
        economy_matrix.append([])
    for i in range(n):
        for j in range(n):
            value = matrix[i][j]
            if value != 0:
                node = Node(value, j)
                economy_matrix[i].append(node)
    return economy_matrix


def generate_economic_trasnpose_matrix(matrix, n):
    economy_matrix = []
    for i in range(n):
        economy_matrix.append([])
    for i in range(n):
        for j in range(n):
            value = matrix[i][j]
            if value != 0:
                node = Node(value, i)
                economy_matrix[j].append(node)
    return economy_matrix


def transpose_economic_matrix(economy_matrix, n):
    transpose_matrix = []
    for i in range(n):
        transpose_matrix.append([])
    for i in range(n):
        for j in range(len(economy_matrix[i])):
            value = economy_matrix[i][j].value
            col = economy_matrix[i][j].col
            node = Node(value, i)
            transpose_matrix[int(col)].append(node)
    return transpose_matrix


def print_economy_matrix(ec, n):
    for i in range(n):
        for j in range(len(ec[i])):
            ec[i][j].print()


def compare_matrix(a, b):
    for i in range(a.size):
        for j in range(len(a.list_matrix[i])):
            if a.list_matrix[i][j].value != b.list_matrix[i][j].value:
                return False
    return True


def multiply_line_into_elem(line1, line2):
    k = 0
    p = 0
    n = len(line1)
    m = len(line2)
    sum = 0
    while True:
        if line1[k].col == line2[p].col:
            sum += line1[k].value * line2[p].value
            k += 1
            p += 1
        elif line1[k].col > line2[p].col:
            p += 1
        else:
            k += 1
        if p >= m:
            break
        if k >= n:
            break
    return sum


def multiply_matrix(a, b, n):
    final_matrix = []
    for i in range(n):
        final_matrix.append([])
    for i in range(n):
        for j in range(n):
            elem = multiply_line_into_elem(a[i], b[j])
            # print(j)
            if elem != 0:
                final_matrix[i].append(Node(elem, j))
    return final_matrix


rare_matrix, n = get_info_txt("a.txt")
ec = generate_economic_matrix(rare_matrix, n)
# print_economy_matrix(ec, n)
a = Sparse(ec, n)

rare_matrix, n = get_info_txt("b.txt")
ec = generate_economic_matrix(rare_matrix, n)
b = Sparse(ec, n)

rare_matrix, n = get_info_txt("a_plus_b.txt")
ec = generate_economic_matrix(rare_matrix, n)
a_plus_b = Sparse(ec, n)

# final_line = add_lines(a.list_matrix[0], b.list_matrix[0])
#
# for i in range(len(final_line)):
#     final_line[i].print()
# print("am ajuns\n\n")

c = add_matrix(a, b, n)
c = Sparse(c, len(c))
# c.print()
print("Compare between our a+b and file: "+f'{compare_matrix(c, a_plus_b)}')
# print (a.list_matrix)
transp_a = transpose_economic_matrix(a.list_matrix, n)
transp_a = Sparse(transp_a, n)
#transp_a.print()
#a.print()
# print(multiply_line_into_elem(a.list_matrix[0], transp_a.list_matrix[0]))
result = multiply_matrix(a.list_matrix, transp_a.list_matrix, n)
result = Sparse(result, n)
#result.print()

rare_matrix, n = get_info_txt("a_ori_a.txt")
ec = generate_economic_matrix(rare_matrix, n)
a_ori_a = Sparse(ec, n)
print("Compare between a*a and file: "+f'{compare_matrix(result, a_ori_a)}')

# rare_matrix, n = get_info_txt("atest.txt")
# ec = generate_economic_matrix(rare_matrix, n)
# atest = Sparse(ec, n)
# atest.print()
# transp_a = transpose_economic_matrix(atest.list_matrix, n)
# transp_a = Sparse(transp_a, n)
# transp_a.print()
# result = multiply_matrix(atest.list_matrix, transp_a.list_matrix, n)
# result=Sparse(result,n)
# result.print()
