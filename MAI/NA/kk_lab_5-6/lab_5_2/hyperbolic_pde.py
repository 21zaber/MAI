"""Hyperbolic partial differential equation"""

from lab_5_2.finite_difference.explicit_method import explicit_fd
from lab_5_2.finite_difference.implicit_method import implicit_fd


class HyperbolicPDE:
    """Solve hyperbolic partial differential equation

    Equation:
        d^2U/dt^2 = a^2 * d^2U/dx^2 + b * dU/dx + c * U + e * dU/dt + f(x, t)

        alpha * dU/dx(l_1, t) + beta * U(l_1, t) = phi_0(t)
        gamma * dU/dx(l_2, t) + delta * U(l_2, t) = phi_1(t)

        U(x, 0) = psi_1(x)
        dU/dt(x, 0) = psi_2(x)

        x in [0, l]
        t in [0, T]
    """

    def __init__(self,
                 a, b, c, e, f,
                 alpha, beta, phi_0,
                 gamma, delta, phi_1,
                 psi_1, psi_2,
                 min_x, max_x,
                 max_t):
        self.main_args = (a, b, c, e, f)
        self.boundary_left_args = (alpha, beta, phi_0)
        self.boundary_right_args = (gamma, delta, phi_1)
        self.initial_args = (psi_1, psi_2)
        self.max_x = max_x
        self.min_x = min_x
        self.max_t = max_t

    def solve_explicit_method(self, step_x, step_t, boundary_approximation_func, initial_approximation_order):
        return explicit_fd(self.main_args,
                           self.boundary_left_args,
                           self.boundary_right_args,
                           self.initial_args,
                           self.min_x, self.max_x,
                           self.max_t,
                           step_x, step_t,
                           boundary_approximation_func,
                           initial_approximation_order)

    def solve_implicit_method(self, step_x, step_t, boundary_approximation_func, initial_approximation_order):
        return implicit_fd(self.main_args,
                           self.boundary_left_args,
                           self.boundary_right_args,
                           self.initial_args,
                           self.min_x, self.max_x,
                           self.max_t,
                           step_x, step_t,
                           boundary_approximation_func,
                           initial_approximation_order)

    def solve(self, step_x, step_t, scheme_type, boundary_approximation_func, initial_approximation_order):
        if scheme_type == 'explicit':
            return self.solve_explicit_method(step_x, step_t, boundary_approximation_func, initial_approximation_order)
        if scheme_type == 'implicit':
            return self.solve_implicit_method(step_x, step_t, boundary_approximation_func, initial_approximation_order)

if __name__ == '__main__':
    pass
