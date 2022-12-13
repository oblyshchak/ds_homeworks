import copy

class Matrix:
    def __init__(self, data):
        self.matrix = data

    def print_matrix(self):
        print(self.matrix)

    def checking(self, matrix_a, matrix_b):
        matrix_a = copy.deepcopy(matrix_a)
        matrix_b = copy.deepcopy(matrix_b)
        if len(matrix_a) != len(matrix_b):
            if len(matrix_a) > len(matrix_b):
                dif = len(matrix_a) - len(matrix_b)
                matrix_b.extend([[0]]*dif)
            else:
                dif = len(matrix_b) - len(matrix_a)
                matrix_a.extend([[0]]*dif)

        for row_a in matrix_a:
            for row_b in matrix_b:
                if len(row_a)>len(row_b):
                    dif = len(row_a) - len(row_b)
                    row_b.extend([0]*dif)
                else:
                    dif = len(row_b) - len(row_a)
                    row_a.extend([0]*dif)

        return matrix_a, matrix_b

    def sum_matrix(self, data):
        matrix, data = self.checking(self.matrix, data.matrix)
        result_matrix = []
        for n in range(len(matrix)):
            row_in_first = matrix[n]
            row_in_second = data[n]
            adding = []
            for i in range(len(row_in_first)):
                adding.append(row_in_first[i] + row_in_second[i])
            result_matrix.append(adding)
        return Matrix(result_matrix)

    def subtraction(self, data):
        matrix, data = self.checking(self.matrix, data.matrix)
        result_matrix = []
        for n in range(len(matrix)):
            row_in_first = matrix[n]
            row_in_second = data[n]
            adding = []
            for i in range(len(row_in_first)):
                adding.append(row_in_first[i] - row_in_second[i])
            result_matrix.append(adding)

        return Matrix(result_matrix)

    def transpose(self):
        matrix = copy.deepcopy(self.matrix)
        result = []
        # [[1, 2],    [[1, 3, 5], [2, 4, 6]], len = 2
        # [3, 4],
        # [5, 6]], len = 3
        number_future_rows = len(matrix[0])
        number_future_columns = len(matrix)
        for i in range(number_future_rows):
            result.append([])
        for empty_list in result:
            empty_list.extend([0]*number_future_columns)

        for i in range(len(result)):
            for k in range(len(result[i])):
                result[i][k] = matrix[k][i]
        return Matrix(result)

    def multi_number(self, number):
        result_matrix = []
        for row in self.matrix:
            new_row = []
            for value in row:
                new_row.append(number * value)
            result_matrix.append(new_row)

        return Matrix(result_matrix)

    def multiplication(self, data):
        #Check quantity columns in matrix A and check is matrix or not
        for i in range(len(self.matrix) - 1):
            quantity_columns_A = len(self.matrix[i])
            if len(self.matrix[i]) != len(self.matrix[i+1]):
                raise Exception (f"{self.matrix} is not support rules matrix")
        quantity_rows_A = len(self.matrix)

         #Check quantity rows in matrix B and check is matrix or not
        quantity_rows_in_B = len(data.matrix)
        for i in range(len(data.matrix) - 1):
            quantity_columns_B = len(data.matrix[i])
            if len(data.matrix[i]) != len(data.matrix[i+1]):
                raise Exception (f"{data.matrix} is not support rules matrix")
        if quantity_columns_A == quantity_rows_in_B:
            #create empty matrix for result multiplication
            result_matrix = []
            for i in range(quantity_rows_A):
                #create new row for matrix
                add = []
                for k in range(quantity_columns_B):
                    new_val = 0
                    for j in range(quantity_columns_A):
                        new_val += self.matrix[i][j] * data.matrix[j][k]
                    add.append(new_val)
                result_matrix.append(add)
            return Matrix(result_matrix)
        else:
            raise Exception ("matrix are not supported multiplication")


a = Matrix([
    [1, 2],
    [4, 6],
    [8, 90]
    ])
b = Matrix([
    [10, 20, 30],
    [40, 50, 60],
    [80, 10, 90]
    ])

a.transpose()
v = b.transpose()
v.print_matrix()
c = a.subtraction(b)
c.print_matrix()
a.sum_matrix(b)
a.multiplication(b)
b.multi_number(8)