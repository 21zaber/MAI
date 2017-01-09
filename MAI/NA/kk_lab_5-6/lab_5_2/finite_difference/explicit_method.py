def explicit_fd(main_args,
                boundary_left_args,
                boundary_right_args,
                initial_args,
                min_x, max_x,
                max_t,
                step_x, step_t,
                boundary_approximation_func='first_order_two_points',
                initial_approximation_order=1):
    """Solve hyperbolic partial differential equation with Explicit finite difference method"""
    d = {
        'first_order_two_points': _o1p2,
        'second_order_two_points': _o2p2,
        'second_order_three_points': _o2p3
    }
    f0, f1 = d[boundary_approximation_func](main_args,
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

    A = (2 - e * step_t) / (2 * step_t ** 2)
    B = ((a / step_x) ** 2 - b / (2 * step_x)) / A
    C = (2 / step_t ** 2 + c - 2 * (a / step_x) ** 2) / A
    D = ((a / step_x) ** 2 + b / (2 * step_x)) / A
    E = (-2 - step_t * e) / (2 - step_t * e)

    for t in range(2, m):
        for x in range(1, n - 1):
            u[t][x] = (B * u[t - 1][x - 1] + C * u[t - 1][x] + D * u[t - 1][x + 1] + E * u[t - 2][x] +
                       f(min_x + x * step_x, (t - 1) * step_t))
        u[t][0] = f0(t * step_t, u[t][1], u[t][2], u[t - 1][0], u[t - 2][0])
        u[t][n - 1] = f1(t * step_t, u[t][n - 2], u[t][n - 3], u[t - 1][n - 1], u[t - 2][n - 1])

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

    def f_0(*args):
        t, u_1 = args[:2]
        return (step_x * phi_0(t) - alpha * u_1) / (beta * step_x - alpha)

    def f_1(*args):
        t, u_n1 = args[:2]
        return (step_x * phi_1(t) + gamma * u_n1) / (gamma + delta * step_x)

    return f_0, f_1


def _o2p2(main_args, boundary_left_args, boundary_right_args, step_x, step_t, min_x, max_x):
    a, b, c, e, f = main_args
    alpha, beta, phi_0 = boundary_left_args
    gamma, delta, phi_1 = boundary_right_args

    def f_0(*args):
        t, u_1, _, u_0_prev_t, u_0_prev_prev_t = args[:5]
        z = alpha * step_x ** 2 / step_t
        a2 = a ** 2
        tmp = (u_1 * (-2 * alpha * a2) +
               u_0_prev_t * (z * e - 2 * z / step_t) +
               u_0_prev_prev_t * (z / step_t) +
               phi_0(t) * 2 * (step_x * a2 - step_x ** 2 * b) +
               f(min_x, t) * (-alpha * step_x ** 2))
        tmp /= (-2 * alpha * a2 -
                z / step_t +
                z * e +
                step_t * z * c +
                2 * beta * (step_x * a2 - step_x ** 2 * b))
        return tmp

    def f_1(*args):
        t, u_n1, _, u_n_prev_t, u_n_prev_prev_t = args[:5]
        z = gamma * step_x ** 2 / step_t
        a2 = a ** 2
        tmp = (u_n1 * (-2 * gamma * a2) +
               u_n_prev_t * (z * e - 2 * z / step_t) +
               u_n_prev_prev_t * (z / step_t) +
               phi_1(t) * -2 * (step_x * a2 + step_x ** 2 * b) +
               f(max_x, t) * (-gamma * step_x ** 2))
        tmp /= (-2 * gamma * a2 -
                z / step_t +
                z * e +
                step_t * z * c +
                -2 * delta * (step_x * a2 + step_x ** 2 * b))
        return tmp

    return f_0, f_1


def _o2p3(main_args, boundary_left_args, boundary_right_args, step_x, step_t, min_x, max_x):
    alpha, beta, phi_0 = boundary_left_args
    gamma, delta, phi_1 = boundary_right_args

    def f_0(*args):
        t, u_1, u_2 = args[:3]
        return (2 * step_x * phi_0(t) + alpha * (-4 * u_1 + u_2)) / (2 * step_x * beta - 3 * alpha)

    def f_1(*args):
        t, u_n1, u_n2 = args[:3]
        return (2 * step_x * phi_1(t) + gamma * (4 * u_n1 - u_n2)) / (2 * step_x * delta + 3 * gamma)

    return f_0, f_1


if __name__ == '__main__':
    pass
