from common.matrix import Matrix
from common.matrix import Vector
from common.tridiagonal_matrix_algorithm import TDMA


def implicit_fd(main_args,
                boundary_left_args, boundary_right_args,
                initial_func,
                min_x, max_x,
                max_t,
                step_x, step_t,
                boundary_approximation_func='first_order_two_points'):
    """Solve parabolic partial differential equation with Implicit finite difference method"""

    d = {
        'first_order_two_points': _o1p2,  # o - order, p - points
        'second_order_two_points': _o2p2,
        'second_order_three_points': _o2p3
    }
    (complete_matrix,
     complete_vector) = d[boundary_approximation_func](main_args,
                                                       boundary_left_args, boundary_right_args,
                                                       step_x, step_t,
                                                       min_x, max_x)

    m = int(max_t / step_t) + 1
    n = int((max_x - min_x) / step_x) + 1
    u = [None for _ in range(m)]
    u[0] = [initial_func(min_x + x * step_x) for x in range(n)]

    a, b, c, f = main_args

    k1 = b * step_t / (2 * step_x) - a * step_t / step_x ** 2
    k2 = 2 * a * step_t / step_x ** 2 - c * step_t + 1
    k3 = -b * step_t / (2 * step_x) - a * step_t / step_x ** 2

    matrix_u_t = Matrix(size=(n, 3))
    for i in range(1, n - 1):
        matrix_u_t[i] = [k1, k2, k3]
    complete_matrix(matrix_u_t)

    for t in range(1, m):
        v = Vector(size=(n, 1))
        for x in range(1, n - 1):
            v[x] = u[t - 1][x] + step_t * f(min_x + x * step_x, t * step_t)
        complete_vector(v, t * step_t, matrix_u_t, u[t-1][0], u[t-1][-1])
        u[t] = list(TDMA(mtrx=matrix_u_t, vec=v).solve())

    return u


def _o1p2(main_args, boundary_left_args, boundary_right_args, step_x, step_t, min_x, max_x):
    alpha, beta, phi_0 = boundary_left_args
    gamma, delta, phi_1 = boundary_right_args

    def complete_matrix(*args):
        m, = args[:1]

        m[0][1] = step_x * beta - alpha
        m[0][2] = alpha
        m[-1][0] = -gamma
        m[-1][1] = gamma + step_x * delta

    def complete_vector(*args):
        v, t = args[:2]

        v[0] = step_x * phi_0(t)
        v[-1] = step_x * phi_1(t)

    return complete_matrix, complete_vector


def _o2p2(main_args, boundary_left_args, boundary_right_args, step_x, step_t, min_x, max_x):
    a, b, c, f = main_args
    alpha, beta, phi_0 = boundary_left_args
    gamma, delta, phi_1 = boundary_right_args

    def complete_matrix(*args):
        m, = args[:1]

        m[0][1] = (alpha * step_x * c -
                   2 * a * alpha / step_x -
                   alpha * step_x / step_t +
                   beta * (2 * a - b * step_x))

        m[0][2] = 2 * a * alpha / step_x

        m[-1][0] = -2 * a * gamma / step_x
        m[-1][1] = (2 * a * gamma / step_x +
                    gamma * step_x / step_t -
                    gamma * c * step_x +
                    delta * (2 * a + b * step_x))

    def complete_vector(*args):
        v, t, _, u_0_prev_t, u_n_prev_t = args[:5]

        v[0] = (2 * a - b * step_x) * phi_0(t)
        v[0] -= alpha * step_x * (u_0_prev_t / step_t + f(min_x, t))

        v[-1] = (2 * a + b * step_x) * phi_1(t)
        v[-1] += gamma * step_x * (u_n_prev_t / step_t + f(max_x, t))

    return complete_matrix, complete_vector


def _o2p3(main_args, boundary_left_args, boundary_right_args, step_x, step_t, min_x, max_x):
    alpha, beta, phi_0 = boundary_left_args
    gamma, delta, phi_1 = boundary_right_args

    def complete_matrix(*args):
        m, = args[:1]

        k = (-alpha / (2 * step_x)) / m[1][2]
        k1 = beta - 3 * alpha / (2 * step_x)
        k2 = 2 * alpha / step_x
        m[0][1] = k1 - k * m[1][0]
        m[0][2] = k2 - k * m[1][1]

        k = (gamma / (2 * step_x)) / m[-2][0]
        k1 = -2 * gamma / step_x
        k2 = 3 * gamma / (2 * step_x) + delta
        m[-1][0] = k1 - k * m[-2][1]
        m[-1][1] = k2 - k * m[-2][2]

    def complete_vector(*args):
        v, t, m = args[:3]

        k = (-alpha / (2 * step_x)) / m[1][2]
        v[0] = phi_0(t) - k * v[1]
        k = (gamma / (2 * step_x)) / m[-2][0]
        v[-1] = phi_1(t) - k * v[-2]

    return complete_matrix, complete_vector


if __name__ == '__main__':
    pass
