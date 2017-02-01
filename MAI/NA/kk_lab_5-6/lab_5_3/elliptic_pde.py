"""Elliptic partial differential equation"""

from lab_5_3.finite_difference.libman import Libman
from lab_5_3.finite_difference.seidel import Seidel
from lab_5_3.finite_difference.sor import SOR


class EllipticPDE:
    """Solve elliptic partial differential equation

    Equation:
        d^2U/dx^2 + d^2U/dy^2 + b_x * dU/dx + b_y * dU/dy + c * U + f(x, y) = 0

        alpha_1 * dU/dx(0, y) + beta_1 * U(0, y) = phi_1(y)
        alpha_2 * dU/dx(l_x, y) + beta_2 * U(l_x, y) = phi_2(y)
        alpha_3 * dU/dy(x, 0) + beta_3 * U(x, 0) = phi_3(x)
        alpha_4 * dU/dy(x, l_y) + beta_4 * U(x, l_y) = phi_4(x)

        x in [0, l_x]
        y in [0, l_y]
    """

    def __init__(self,
                 b_x, b_y, c, f,
                 alpha_1, beta_1, phi_1,
                 alpha_2, beta_2, phi_2,
                 alpha_3, beta_3, phi_3,
                 alpha_4, beta_4, phi_4,
                 max_x, max_y,
                 step_num_x, step_num_y):
        self.main_args = (b_x, b_y, c, f)
        self.bound_1 = (alpha_1, beta_1, phi_1)
        self.bound_2 = (alpha_2, beta_2, phi_2)
        self.bound_3 = (alpha_3, beta_3, phi_3)
        self.bound_4 = (alpha_4, beta_4, phi_4)
        self.max_x = max_x
        self.max_y = max_y
        self.n = step_num_x
        self.m = step_num_y

    def libman(self):
        return Libman(self.main_args,
                      self.bound_1, self.bound_2, self.bound_3, self.bound_4,
                      self.max_x, self.max_y,
                      self.n, self.m)

    def seidel(self):
        return Seidel(self.main_args,
                      self.bound_1, self.bound_2, self.bound_3, self.bound_4,
                      self.max_x, self.max_y,
                      self.n, self.m)

    def sor(self, relax):
        return SOR(self.main_args,
                   self.bound_1, self.bound_2, self.bound_3, self.bound_4,
                   self.max_x, self.max_y,
                   self.n, self.m,
                   relax=relax)


if __name__ == '__main__':
    from math import *

    e = EllipticPDE(0, 0, 1, lambda x, y: 0,
                    1, 0, lambda y: cos(y),
                    1, -1, lambda y: 0,
                    0, 1, lambda x: x,
                    0, 1, lambda x: 0,
                    max_x=1, max_y=pi / 2,
                    step_num_x=20, step_num_y=10)
    l = [e.libman(), e.seidel(), e.sor(1.2), e.sor(1.7)]
    for i in l:
        i.solve(1e-7)
        print(i.final_eps)
        print(i.cur_iter_num)
        print()
