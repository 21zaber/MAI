from common.matrix import Matrix
from common.matrix import Vector


class TDMA:
    def __init__(self, mtrx=Matrix((1, 1)), vec=Vector((1, 1))):
        if mtrx.size[1] == 3:
            self.__mtrx = mtrx.copy()
            self.__mtrx[0][0] = 0
            self.__mtrx[self.__mtrx.size[0]-1][-1] = 0
        else:
            self.__mtrx = self.__to_compact_view(mtrx)
        self.__vector = vec
        self.__need_logging = False

    def __str__(self):
        s = ""
        for i in range(1, 3):
            s += "{}*x{} + ".format(self.__mtrx[0][i], i)
        s = s[:-2] + "= {}\n".format(self.__vector[0])
        for i in range(1, self.__mtrx.size[0] - 1):
            for j in range(self.__mtrx.size[1]):
                s += "{}*x{} + ".format(self.__mtrx[i][j], j+i)
            s = s[:-2] + "= {}\n".format(self.__vector[i])
        for i in range(0, 2):
            s += "{}*x{} + ".format(self.__mtrx[-1][i], i - 1 + self.__mtrx.size[0])
        s = s[:-2] + "= {}\n".format(self.__vector[-1])
        return s

    def log(self, flag=False):
        self.__need_logging = flag

    # don't work if mtrx is 1x1, but who cares
    @staticmethod
    def __to_compact_view(mtrx):
        new_mtrx = Matrix((mtrx.size[0], 3))
        for i in range(2):
            new_mtrx[0][i+1] = mtrx[0][i]
            new_mtrx[mtrx.size[0] - 1][-i - 2] = mtrx[mtrx.size[0] - 1][-i - 1]
        shift = 0
        for i in range(1, mtrx.size[0]-1):
            for j in range(0, 3):
                new_mtrx[i][j] = mtrx[i][j + shift]
            shift += 1
        return new_mtrx

    def solve(self):
        if self.need_logging:
            print(self)

        x = Vector((self.__mtrx.size[0], 1))
        a, b, c = self.__mtrx[0]
        d = self.__vector[0]
        pq_list = [(-c/b, d/b)]  # pq_list[i][0] = P_i, pq_list[i][1] = Q_i
        
        if self.need_logging:
            print("P{0} = {1}, Q{0} = {2}".format(1, pq_list[0][0], pq_list[0][1]))
        
        for i in range(1, self.__mtrx.size[0]):
            a, b, c = self.__mtrx[i]
            d = self.__vector[i]
            tmp = b + a * pq_list[i-1][0]
            p = -c / tmp
            q = (d - a * pq_list[i-1][1]) / tmp
            pq_list.append((p, q))
            
            if self.need_logging:
                print("P{0} = {1}, Q{0} = {2}".format(i+1, pq_list[i][0], pq_list[i][1]))
            
        x[-1] = pq_list[-1][1]
        
        if self.need_logging:
            print("\nx{0} = Q{0} = {1}".format(x.size[0], x[-1]))
            
        for i in range(x.size[0]-2, -1, -1):
            x[i] = pq_list[i][0] * x[i+1] + pq_list[i][1]

        if self.need_logging:
            for i in range(x.size[0]-2, -1, -1):
                print("x{0} = P{0} * x{1} + Q{0} = {2} * {3} + {4} = {5}".
                      format(i+1, i+2, pq_list[i][0], x[i+1], pq_list[i][1], x[i]))
            print()

        return x

    @property
    def need_logging(self):
        return self.__need_logging
