from common.matrix import Matrix
from common.matrix import Vector
from common.tridiagonal_matrix_algorithm import TDMA


def implicit_fd(main_args,
                boundary_left_args,
                boundary_right_args,
                initial_args,
                min_x, max_x,
                max_t,
                step_x, step_t,
                boundary_approximation_func='first_order_two_points',
                initial_approximation_order=1):
    """Solve hyperbolic partial differential equation with Implicit finite difference method"""
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

    a, b, c, e, f = main_args
    psi_1, psi_2 = initial_args

    m = int(max_t / step_t) + 1
    n = int((max_x - min_x) / step_x) + 1

    u = [[None for _ in range(n)] for _ in range(m)]

    init_second_layer_func = _get_init_second_layer_func(initial_approximation_order,
                                                         main_args,
                                                         initial_args,
                                                         step_t)

    for x in range(n):
        u[0][x] = psi_1(min_x + x * step_x)
        u[1][x] = init_second_layer_func(min_x + x * step_x, u[0][x])

    A = b / (2 * step_x) - (a / step_x) ** 2
    B = 1 / step_t ** 2 + 2 * (a / step_x) ** 2 - c - e / step_t
    C = - b / (2 * step_x) - (a / step_x) ** 2
    X = 2 / step_t ** 2 - e / step_t
    Y = - 1 / step_t ** 2

    matrix_u_t = Matrix(size=(n, 3))
    for i in range(1, n - 1):
        matrix_u_t[i] = [A, B, C]
    complete_matrix(matrix_u_t)

    for t in range(2, m):
        v = Vector(size=(n, 1))
        for x in range(1, n - 1):
            v[x] = f(min_x + x * step_x, t * step_t) + u[t - 1][x] * X + u[t - 2][x] * Y
        complete_vector(v, t * step_t, matrix_u_t, u[t - 1][0], u[t - 1][-1], u[t - 2][0], u[t - 2][-1])
        u[t] = list(TDMA(mtrx=matrix_u_t, vec=v).solve())

    return u


def _get_init_second_layer_func(approximation_order, main_args, initial_args, step_t):
    a, b, c, e, f = main_args
    psi_1, psi_2 = initial_args
    psi_1_1 = psi_1.get_derivative('x')
    psi_1_2 = psi_1_1.get_derivative('x')
    if approximation_order == 1:
        def _f(x, prev_u):
            return step_t * psi_2(x) + prev_u
    else:
        def _f(x, prev_u):
            return (prev_u * (1 + step_t ** 2 * c / 2) +
                    psi_2(x) * (step_t + step_t ** 2 * e / 2) +
                    step_t ** 2 / 2 * (a ** 2 * psi_1_2(x) + b * psi_1_1(x) + f(x, 0)))
    return _f


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
    a, b, c, e, f = main_args
    alpha, beta, phi_0 = boundary_left_args
    gamma, delta, phi_1 = boundary_right_args

    def complete_matrix(*args):
        m, = args[:1]

        a2 = a ** 2

        z = alpha * step_x ** 2 / step_t
        m[0][1] = (-2 * alpha * a2 -
                   z / step_t +
                   z * e +
                   alpha * step_x ** 2 * c +
                   2 * beta * (step_x * a2 - step_x ** 2 * b))
        m[0][2] = 2 * alpha * a2

        z = gamma * step_x ** 2 / step_t
        m[-1][0] = 2 * gamma * a2
        m[-1][1] = (-2 * gamma * a2 -
                    z / step_t +
                    z * e +
                    gamma * step_x ** 2 * c -
                    2 * delta * (step_x * a2 + step_x ** 2 * b))

    def complete_vector(*args):
        v, t, _, u_0_prev_t, u_n_prev_t, u_0_prev_prev_t, u_n_prev_prev_t = args[:7]

        a2 = a ** 2

        z = alpha * step_x ** 2 / step_t
        v[0] = (2 * (step_x * a2 - step_x ** 2 * b) * phi_0(t) -
                alpha * step_x ** 2 * f(min_x, t) +
                u_0_prev_t * (z * e - 2 * z / step_t) +
                u_0_prev_prev_t * (z / step_t))

        z = gamma * step_x ** 2 / step_t
        v[-1] = (-2 * (step_x * a2 + step_x ** 2 * b) * phi_1(t) -
                 gamma * step_x ** 2 * f(max_x, t) +
                 u_n_prev_t * (z * e - 2 * z / step_t) +
                 u_n_prev_prev_t * (z / step_t))

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
        m[-1][0] = k1 - k * m[-2][0]
        m[-1][1] = k2 - k * m[-2][1]

    def complete_vector(*args):
        v, t, m = args[:3]

        k = (-alpha / (2 * step_x)) / m[1][2]
        v[0] = phi_0(t) - k * v[1]
        k = (gamma / (2 * step_x)) / m[-2][0]
        v[-1] = phi_1(t) - k * v[-2]

    return complete_matrix, complete_vector


if __name__ == '__main__':
    pass
