from lab_5_3.finite_difference.libman import Libman


class Seidel(Libman):
    def fill_inside(self):
        f = self.main_args[3]
        for i in range(1, self.n):
            for j in range(1, self.m):
                self.u[i][j] = (self.u[i - 1][j] * self.A +
                                self.u[i][j - 1] * self.B +
                                self.prev_u[i][j + 1] * self.C +
                                self.prev_u[i + 1][j] * self.D -
                                f(i * self.step_x, j * self.step_y)) / self.E

    def fill_border_2(self):
        alpha, beta, phi = self.bound_2
        k1 = alpha / self.step_x
        k2 = beta + k1
        y = 0
        for j in range(self.m + 1):
            self.u[self.n][j] = (phi(y) + k1 * self.u[self.n - 1][j]) / k2
            y += self.step_y

    def fill_border_4(self):
        alpha, beta, phi = self.bound_4
        k1 = alpha / self.step_y
        k2 = beta + k1
        x = 0
        for i in range(self.n + 1):
            self.u[i][self.m] = (phi(x) + k1 * self.u[i][self.m - 1]) / k2
            x += self.step_x

    def iterate(self):
        self.fill_border_1()
        self.fill_border_3()
        self.fill_inside()
        self.fill_border_2()
        self.fill_border_4()
        self.cur_iter_num += 1


if __name__ == '__main__':
    pass
