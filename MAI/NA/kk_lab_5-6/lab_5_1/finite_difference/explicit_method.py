def explicit_fd(main_args,
                boundary_left_args, boundary_right_args,
                initial_func,
                min_x, max_x,
                max_t,
                step_x, step_t,
                boundary_approximation_func='first_order_two_points'):
    """Solve parabolic partial differential equation with Explicit finite difference method"""
    d = {
        'first_order_two_points': _o1p2,
        'second_order_two_points': _o2p2,
        'second_order_three_points': _o2p3
    }
    f0, f1 = d[boundary_approximation_func](main_args,
                                            boundary_left_args, boundary_right_args,
                                            step_x, step_t,
                                            min_x, max_x)
    m = int(max_t / step_t) + 1
    n = int((max_x - min_x) / step_x) + 1
    u = [[None for _ in range(n)] for _ in range(m)]

    for x in range(n):
        u[0][x] = initial_func(min_x + x * step_x)

    a, b, c, f = main_args
    coef_1 = a * step_t / step_x ** 2
    coef_2 = b * step_t / (2 * step_x)
    for t in range(1, m):
        for x in range(1, n - 1):
            u[t][x] = (u[t - 1][x + 1] * (coef_1 + coef_2) +
                       u[t - 1][x] * (1 - 2 * coef_1 + c * step_t) +
                       u[t - 1][x - 1] * (coef_1 - coef_2) +
                       f(min_x + x * step_x, (t - 1) * step_t) * step_t)
        u[t][0] = f0(t * step_t, u[t][1], u[t][2], u[t - 1][0])
        u[t][n - 1] = f1(t * step_t, u[t][n - 2], u[t][n - 3], u[t - 1][n - 1])
    return u


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
    a, b, c, f = main_args
    alpha, beta, phi_0 = boundary_left_args
    gamma, delta, phi_1 = boundary_right_args

    def f_0(*args):
        t, u_1, _, u_0_prev_t = args[:4]
        a2 = 2 * a
        tmp = (a2 - b * step_x) * phi_0(t) - (a2 * alpha / step_x) * u_1 - \
              (alpha * step_x / step_t) * u_0_prev_t - alpha * step_x * f(min_x, t)
        tmp /= alpha * (c * step_x - a2 / step_x - step_x / step_t) + beta * (a2 - b * step_x)
        return tmp

    def f_1(*args):
        t, u_n1, _, u_n_prev_t = args[:4]
        a2 = 2 * a
        tmp = (a2 + b * step_x) * phi_1(t) + (a2 * gamma / step_x) * u_n1 + \
              (gamma * step_x / step_t) * u_n_prev_t + gamma * step_x * f(max_x, t)
        tmp /= gamma * (a2 / step_x + step_x / step_t - c * step_x) + delta * (a2 + b * step_x)
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
