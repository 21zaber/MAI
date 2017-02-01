from copy import deepcopy


MAX_ITERATION_NUM = 5000


class BaseIteration:
    def __init__(self,
                 main_args,
                 bound_1,
                 bound_2,
                 bound_3,
                 bound_4,
                 max_x, max_y,
                 n, m):
        self.main_args = main_args
        self.bound_1 = bound_1
        self.bound_2 = bound_2
        self.bound_3 = bound_3
        self.bound_4 = bound_4
        self.max_x = max_x
        self.max_y = max_y
        self.n = n
        self.m = m

        self.step_x = max_x / n
        self.step_y = max_y / m

        b_x, b_y, c, f = self.main_args
        self.A = b_x / (2 * self.step_x) - self.step_x ** -2
        self.B = b_y / (2 * self.step_y) - self.step_y ** -2
        self.C = -b_y / (2 * self.step_y) - self.step_y ** -2
        self.D = -b_x / (2 * self.step_x) - self.step_x ** -2
        self.E = c - 2 / self.step_x ** 2 - 2 / self.step_y ** 2

        self.prev_u = None
        self.u = [[1] * (m + 1) for _ in range(n + 1)]

        self.max_iter_num = MAX_ITERATION_NUM
        self.cur_iter_num = 0

        self.final_eps = None

    def fill_border_1(self):
        pass

    def fill_border_2(self):
        pass

    def fill_border_3(self):
        pass

    def fill_border_4(self):
        pass

    def fill_inside(self):
        pass

    def fill_border(self):
        self.fill_border_1()
        self.fill_border_2()
        self.fill_border_3()
        self.fill_border_4()

    def iterate(self):
        self.fill_inside()
        self.fill_border()
        self.cur_iter_num += 1

    def solve(self, eps):
        while self.cur_iter_num <= self.max_iter_num:
            self.prev_u = deepcopy(self.u)
            self.iterate()
            if BaseIteration.norm(self.u, self.prev_u) <= eps:
                break
        self.final_eps = BaseIteration.norm(self.u, self.prev_u)
        return self.u

    @staticmethod
    def norm(a, b):
        lam = lambda x, y: abs(x - y)
        res = max(map(lam, a[0], b[0]))
        for i in range(1, min(len(a), len(b))):
            res = max(res, max(map(lam, a[i], b[i])))
        return res

if __name__ == '__main__':
    pass
