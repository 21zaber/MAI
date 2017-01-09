from math import sqrt
from cmath import sqrt as csqrt
import copy


class Matrix:
    def __init__(self, size=(0, 0), mtrx=None):
        self.size = tuple(size)
        if mtrx is None:
            self.mtrx = [[0 for _ in range(size[1])] for _ in range(size[0])]
        else:
            self.mtrx = copy.deepcopy(mtrx)

    def __str__(self):
        s = ""
        for row in self.mtrx:
            for elem in row:
                s += str(elem) + "  "
            s += "\n"
        return s

    def set_size(self, size):
        if size[1] > self.size[1]:
            for row in self.mtrx:
                row += [0. for _ in range(self.size[1], size[1])]
        if size[0] > self.size[0]:
            for i in range(self.size[0], size[0]):
                self.mtrx.append([0. for _ in range(size[1])])
        self.size = tuple(size)

    def fill(self, *args):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.mtrx[i][j] = args[i * self.size[1] + j]

    def __iadd__(self, other):
        if self.size != other.size:
            raise ValueError("wrong size: {}x{} and {}x{}".format(*(self.size + other.size)))
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.mtrx[i][j] += other.mtrx[i][j]
        return self

    def __add__(self, other):
        res = Matrix(self.size, self.mtrx)
        res += other
        return res

    def __isub__(self, other):
        if self.size != other.size:
            raise ValueError("wrong size: {}x{} and {}x{}".format(*(self.size + other.size)))
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.mtrx[i][j] -= other.mtrx[i][j]
        return self

    def __sub__(self, other):
        res = Matrix(self.size, self.mtrx)
        res -= other
        return res

    def __imul__(self, num):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.mtrx[i][j] *= num
        return self

    def __mul__(self, other):
        if self.size[1] != other.size[0]:
            raise ValueError("wrong size: {}x{} and {}x{}".format(*(self.size + other.size)))
        res = Matrix([self.size[0], other.size[1]])
        for i in range(res.size[0]):
            for j in range(res.size[1]):
                for k in range(self.size[1]):
                    res.mtrx[i][j] += self.mtrx[i][k] * other.mtrx[k][j]
        return res

    def norm_inf(self):
        if self.size[0] == 0 or self.size[1] == 0:
            raise ValueError("wrong size: {}x{}".format(*self.size))
        norm = sum(map(abs, self.mtrx[0]))
        for i in range(1, len(self.mtrx)):
            sum_row = sum(map(abs, self.mtrx[i]))
            if sum_row > norm:
                norm = sum_row
        return norm

    def norm_2(self):
        sum_pow_2 = 0
        for row in self.mtrx:
            sum_pow_2 += sum(map(lambda x: x**2, row))
        return sqrt(sum_pow_2) if type(sum_pow_2) is not complex else csqrt(sum_pow_2)

    def normalize(self):
        n = self.norm_2()
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.mtrx[i][j] /= n
        return self

    def __getitem__(self, row):
        return self.mtrx[row]

    def __setitem__(self, key, value):
        self.mtrx[key] = value

    def __iter__(self):
        return iter(self.mtrx)

    @staticmethod
    def parse(file_name):
        mtrx_file = open(file_name)
        matrix = Matrix()
        matrix.mtrx = []
        n = 0
        m = 0
        for line in mtrx_file:
            if m == 0:
                m = len(line.split())
            matrix.mtrx.append(list(map(float, line.split())))
        n = len(matrix.mtrx)
        matrix.size = n, m
        mtrx_file.close()
        return matrix

    def copy(self):
        return copy.deepcopy(self)

    def exchange_rows(self, row_1, row_2):
        for i in range(self.size[1]):
            tmp = self.mtrx[row_1][i]
            self.mtrx[row_1][i] = self.mtrx[row_2][i]
            self.mtrx[row_2][i] = tmp
        return self

    def exchange_cols(self, col_1, col_2):
        for i in range(self.size[0]):
            tmp = self.mtrx[i][col_1]
            self.mtrx[i][col_1] = self.mtrx[i][col_2]
            self.mtrx[i][col_2] = tmp
        return self

    def append_col(self, col):
        if col.size[0] != self.size[0]:
            raise ValueError("wrong size: {}x{}".format(*self.size))
        self.size = (self.size[0], self.size[1] + col.size[1])
        for i, row in enumerate(self.mtrx):
            row += col[i]

    def transpose(self):
        t_m = Matrix((self.size[1], self.size[0]))
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                t_m[j][i] = self.mtrx[i][j]
        return t_m

    def scalar_product(self, vec):
        sc_pr = 0
        for i in range(self.size[0]):
            sc_pr += self.mtrx[i][0] * vec[i][0]
        return sc_pr
        
    @staticmethod
    def identity(size):
        e = Matrix(size)
        for i in range(min(*size)):
            e[i][i] = 1.
        return e


class Vector(Matrix):
    def __init__(self, size=(0, 0), mtrx=None):
        if size != (0, 0):
            if size[0] != 1 and size[1] != 1:
                raise ValueError('vector must have size 1xN or Nx1')
        super().__init__(size, mtrx)
        self.iter_pos = 0

    def __getitem__(self, key):
        if self.size[0] == 1:
            return self.mtrx[0][key]
        else:
            return self.mtrx[key][0]

    def __setitem__(self, key, value):
        if self.size[0] == 1:
            self.mtrx[0][key] = value
        else:
            self.mtrx[key][0] = value

    def __iter__(self):
        self.iter_pos = 0
        return self

    def __next__(self):
        if self.size[0] == 1:
            if self.iter_pos == self.size[1]:
                raise StopIteration
        else:
            if self.iter_pos == self.size[0]:
                raise StopIteration
        self.iter_pos += 1
        return self[self.iter_pos - 1]

    def transpose(self):
        t_v = Vector((self.size[1], self.size[0]))
        for i, val in enumerate(self):
            t_v[i] = val
        return t_v
