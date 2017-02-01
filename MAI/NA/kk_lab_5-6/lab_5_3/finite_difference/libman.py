from lab_5_3.finite_difference.base_iteration import BaseIteration


class Libman(BaseIteration):
    def fill_border_1(self):
        alpha, beta, phi = self.bound_1
        k1 = alpha / self.step_x
        k2 = beta - k1
        y = 0
        for j in range(self.m + 1):
            self.u[0][j] = (phi(y) - k1 * self.prev_u[1][j]) / k2
            y += self.step_y

    def fill_border_2(self):
        alpha, beta, phi = self.bound_2
        k1 = alpha / self.step_x
        k2 = beta + k1
        y = 0
        for j in range(self.m + 1):
            self.u[self.n][j] = (phi(y) + k1 * self.prev_u[self.n - 1][j]) / k2
            y += self.step_y

    def fill_border_3(self):
        alpha, beta, phi = self.bound_3
        k1 = alpha / self.step_y
        k2 = beta - k1
        x = 0
        for i in range(self.n + 1):
            self.u[i][0] = (phi(x) - k1 * self.prev_u[i][1]) / k2
            x += self.step_x

    def fill_border_4(self):
        alpha, beta, phi = self.bound_4
        k1 = alpha / self.step_y
        k2 = beta + k1
        x = 0
        for i in range(self.n + 1):
            self.u[i][self.m] = (phi(x) + k1 * self.prev_u[i][self.m - 1]) / k2
            x += self.step_x

    def fill_inside(self):
        f = self.main_args[3]

        for i in range(1, self.n):
            for j in range(1, self.m):
                self.u[i][j] = (self.prev_u[i - 1][j] * self.A +
                                self.prev_u[i][j - 1] * self.B +
                                self.prev_u[i][j + 1] * self.C +
                                self.prev_u[i + 1][j] * self.D -
                                f(i * self.step_x, j * self.step_y)) / self.E


if __name__ == '__main__':
    pass
