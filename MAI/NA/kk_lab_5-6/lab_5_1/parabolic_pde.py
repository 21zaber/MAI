#!/usr/bin/python3.5

"""Parabolic partial differential equation"""

from common.matrix import Matrix
from common.matrix import Vector
from common.tridiagonal_matrix_algorithm import TDMA


class ParabolicPDE:
    """
        Solve parabolic partial differential equation

        Equation:
            dU/dt = a * d^2U/dx^2 + b * dU/dx + c * U + f(x, t)

            alpha0 * dU/dx(0, t) + beta0 * U(0, t) = phi0(t)
            alpha1 * dU/dx(max_x, t) + beta1 * U(max_x, t) = phi1(t)

            U(x, 0) = psi(x)

            x in [min_x, max_x]
            t in [0, max_t]
    """

    class Border:
        """
            Border function:
                alpha * dU/dx(0, t) + beta * U(0, t) = phi_0(t)

        """
        def __init__(self, alpha, beta, phi):
            self.alpha = alpha
            self.beta = beta
            self.phi = phi


    def __init__(self,
                 a, b, c, f,
                 alpha0, beta0, phi0,
                 alpha1, beta1, phi1,
                 psi,
                 min_x, max_x, max_t):

        self.a, self.b, self.c = a, b, c
        self.f = f
        self.lborder = self.Border(alpha0, beta0, phi0)
        self.rborder = self.Border(alpha1, beta1, phi1)
        self.initial_func = psi
        self.max_x = max_x
        self.min_x = min_x
        self.min_t = 0
        self.max_t = max_t
        self.methods = {
                        'explicit': self._explicit_solve,
                        'implicit': self._implicit_solve,
                        'cr-nic': self._cn_solve,
                       }

    def solve(self, scheme_type='explict', approx_type='1o2p', step_x=0, step_t=0):
        return self.methods[scheme_type](approx_type, step_x, step_t)

    def _explicit_solve(self, approx_type, step_x, step_t):
        def approx(pde):
            if approx_type == '1o2p':
                def l(t=None, u1=None, u2=None, ul=None):
                    border = pde.lborder
                    alpha, beta, phi = border.alpha, border.beta, border.phi

                    t = step_x * phi(t) - alpha * u1
                    t /= beta * step_x - alpha
                    return t
                def r(t=None, u1=None, u2=None, ul=None):
                    border = pde.rborder
                    alpha, beta, phi = border.alpha, border.beta, border.phi

                    t = step_x * phi(t) + alpha * ul
                    t /= beta * step_x + alpha
                    return t

                return l, r
            if approx_type == '2o2p':
                def l(t=None, u1=None, u2=None, ul=None):
                    border = pde.lborder
                    a, b, c, f = pde.a, pde.b, pde.c, pde.f
                    alpha, beta, phi = border.alpha, border.beta, border.phi

                    t = (a * 2 - b * step_x) * phi(t) - (a * 2 * alpha / step_x) * u1 - \
                          (alpha * step_x / step_t) * ul - alpha * step_x * f(self.min_x, t)
                    t /= alpha * (c * step_x - a * 2 / step_x - step_x / step_t) + beta * (a * 2 - b * step_x)
                    return t
                def r(t=None, u1=None, u2=None, ul=None):
                    border = pde.rborder
                    a, b, c, f = pde.a, pde.b, pde.c, pde.f
                    alpha, beta, phi = border.alpha, border.beta, border.phi

                    t = (a * 2 + b * step_x) * phi(t) + (a * 2 * alpha / step_x) * u1 + \
                          (alpha * step_x / step_t) * ul + alpha * step_x * f(self.min_x, t)
                    t /= alpha * (-c * step_x + (a * 2) / step_x + step_x / step_t) + beta * (a * 2 + b * step_x)
                    return t

                return l, r
            if approx_type == '2o3p':
                def l(t=None, u1=None, u2=None, ul=None):
                    border = pde.lborder
                    alpha, beta, phi = border.alpha, border.beta, border.phi

                    t = 2 * step_x * phi(t) + alpha * (-4 * u1 + u2)
                    t /= 2 * step_x * beta - 3 * alpha
                    return t
                def r(t=None, u1=None, u2=None, ul=None):
                    border = pde.rborder
                    alpha, beta, phi = border.alpha, border.beta, border.phi

                    t = 2 * step_x * phi(t) + alpha * (4 * u1 - u2)
                    t /= 2 * step_x * beta + 3 * alpha
                    return t

                return l, r

        l, r = approx(self) # borders
        a, b, c, f = self.a, self.b, self.c, self.f

        m = int((self.max_t - self.min_t) / step_t) + 1
        n = int((self.max_x - self.min_x) / step_x) + 1
        xs = [self.min_x + i * step_x for i in range(n)]
        ts = [self.min_t + i * step_t for i in range(m)]

        u = [[0 for i in range(n)] for i in range(m)]
        u[0] = [self.initial_func(x) for x in xs]

        k1 = (a * step_t) / (step_x * step_x)
        k2 = (b * step_t) / (2 * step_x)
        for ti in range(1, m):
            for xi in range(1, n-1):
                u[ti][xi] =(u[ti-1][xi+1] * (k1 + k2) +
                            u[ti-1][xi]   * (1 - 2 * k1 + c * step_t) +
                            u[ti-1][xi-1] * (k1 - k2) +
                            f(xs[xi], ts[ti-1]) * step_t)
            u[ti][0]  = l(ts[ti], u[ti][1], u[ti][2], u[ti-1][0])
            u[ti][-1] = r(ts[ti], u[ti][-2], u[ti][-3], u[ti-1][-1])

        return u

    def _implicit_solve(self, approx_type, step_x, step_t):
        def approx(pde):
            if approx_type == '2o2p':
                def cv(v, t, m, u0, ul):
                    a, b, c, f = pde.a, pde.b, pde.c, pde.f

                    v[0]  = (2 * a - b * step_x) * pde.lborder.phi(t)
                    v[0] -= pde.lborder.alpha * step_x * (u0 / step_t + f(pde.min_x, t))
                    v[-1]  = (2 * a - b * step_x) * pde.rborder.phi(t)
                    v[-1] -= pde.rborder.alpha * step_x * (u0 / step_t + f(pde.min_x, t))

                def cm(m):
                    a, b, c, f = pde.a, pde.b, pde.c, pde.f
                    lb, rb = pde.lborder, pde.rborder

                    m[0][1] =(lb.alpha * step_x * c +
                              lb.beta * (2 * a - b * step_x) -
                              (2 * a * lb.alpha) / step_x -
                              (lb.alpha * step_x) / step_t)
                    m[0][2] = (2 * a * lb.alpha) / step_x

                    m[-1][1] =(rb.alpha * step_x * c +
                               rb.beta * (2 * a + b * step_x) -
                               (2 * a * rb.alpha) / step_x +
                               (rb.alpha * step_x) / step_t)
                    m[-1][0] = (2 * a * rb.alpha) / step_x

                return cm, cv
            if approx_type == '1o2p':
                def cv(v, t, m, u0, ul):
                    v[0]  = step_x * pde.lborder.phi(t)
                    v[-1] = step_x * pde.rborder.phi(t)

                def cm(m):
                    m[0][1] = step_x * pde.lborder.beta - pde.lborder.alpha
                    m[0][2] = pde.lborder.alpha
                    m[-1][1] = step_x * pde.rborder.beta - pde.rborder.alpha
                    m[-1][0] = -pde.rborder.alpha

                return cm, cv
            if approx_type == '2o3p':
                def cv(v, t, m, u0, ul):
                    lb, rb = pde.lborder, pde.rborder

                    k = (-lb.alpha / (2 * step_x)) / m[1][2]
                    v[0] = lb.phi(t) - k * v[1]
                    k = (rb.alpha / (2 * step_x)) / m[-2][0]
                    v[-1] = rb.phi(t) - k * v[-2]

                def cm(m):
                    lb, rb = pde.lborder, pde.rborder

                    k = (-lb.alpha / (2 * step_x)) / m[1][2]
                    k1 = lb.beta - 3 * lb.alpha / (2 * step_x)
                    k2 = 2 * lb.alpha / step_x
                    m[0][1] = k1 - k * m[1][0]
                    m[0][2] = k2 - k * m[1][1]

                    k = (rb.alpha / (2 * step_x)) / m[-2][0]
                    k1 = -2 * rb.alpha / step_x
                    k2 = 3 * rb.alpha / (2 * step_x) + rb.beta
                    m[-1][0] = k1 - k * m[-2][1]
                    m[-1][1] = k2 - k * m[-2][2]

                return cm, cv
        
        cm, cv = approx(self)
        a, b, c, f = self.a, self.b, self.c, self.f

        m = int((self.max_t - self.min_t) / step_t) + 1
        n = int((self.max_x - self.min_x) / step_x) + 1
        xs = [self.min_x + i * step_x for i in range(n)]
        ts = [self.min_t + i * step_t for i in range(m)]

        u = [[] for i in range(m)]
        u[0] = [self.initial_func(x) for x in xs]
        
        k1 = b * step_t / (2 * step_x) - a * step_t / step_x ** 2
        k2 = 2 * a * step_t / step_x ** 2 - c * step_t + 1
        k3 = -b * step_t / (2 * step_x) - a * step_t / step_x ** 2

        U = Matrix(size=(n, 3))
        for i in range(1, n - 1):
            U[i] = [k1, k2, k3]
        cm(U)

        for ti in range(1, m):
            v = Vector(size=(n, 1))
            for xi in range(1, n-1):
                v[xi] = u[ti-1][xi] + step_t * f(xs[xi], ts[ti])
            cv(v, ts[ti], U, u[ti-1][0], u[ti-1][-1])
            u[ti] = list(TDMA(U, v).solve())

        return u

    def _cn_solve(self, approx_type, step_x, step_t):
        def approx(pde):
            if approx_type == '2o2p':
                def cv(v, t, m, u0, ul):
                    a, b, c, f = pde.a, pde.b, pde.c, pde.f

                    v[0]  = (2 * a - b * step_x) * pde.lborder.phi(t)
                    v[0] -= pde.lborder.alpha * step_x * (u0 / step_t + f(pde.min_x, t))
                    v[-1]  = (2 * a - b * step_x) * pde.rborder.phi(t)
                    v[-1] -= pde.rborder.alpha * step_x * (u0 / step_t + f(pde.min_x, t))

                def cm(m):
                    a, b, c, f = pde.a, pde.b, pde.c, pde.f
                    lb, rb = pde.lborder, pde.rborder

                    m[0][1] =(lb.alpha * step_x * c +
                              lb.beta * (2 * a - b * step_x) -
                              (2 * a * lb.alpha) / step_x -
                              (lb.alpha * step_x) / step_t)
                    m[0][2] = (2 * a * lb.alpha) / step_x

                    m[-1][1] =(rb.alpha * step_x * c +
                               rb.beta * (2 * a + b * step_x) -
                               (2 * a * rb.alpha) / step_x +
                               (rb.alpha * step_x) / step_t)
                    m[-1][0] = (2 * a * rb.alpha) / step_x

                return cm, cv
            if approx_type == '1o2p':
                def cv(v, t, m, u0, ul):
                    v[0]  = step_x * pde.lborder.phi(t)
                    v[-1] = step_x * pde.rborder.phi(t)

                def cm(m):
                    m[0][1] = step_x * pde.lborder.beta - pde.lborder.alpha
                    m[0][2] = pde.lborder.alpha
                    m[-1][1] = step_x * pde.rborder.beta - pde.rborder.alpha
                    m[-1][0] = -pde.rborder.alpha

                return cm, cv
            if approx_type == '2o3p':
                def cv(v, t, m, u0, ul):
                    lb, rb = pde.lborder, pde.rborder

                    k = (-lb.alpha / (2 * step_x)) / m[1][2]
                    v[0] = lb.phi(t) - k * v[1]
                    k = (rb.alpha / (2 * step_x)) / m[-2][0]
                    v[-1] = rb.phi(t) - k * v[-2]

                def cm(m):
                    lb, rb = pde.lborder, pde.rborder

                    k = (-lb.alpha / (2 * step_x)) / m[1][2]
                    k1 = lb.beta - 3 * lb.alpha / (2 * step_x)
                    k2 = 2 * lb.alpha / step_x
                    m[0][1] = k1 - k * m[1][0]
                    m[0][2] = k2 - k * m[1][1]

                    k = (rb.alpha / (2 * step_x)) / m[-2][0]
                    k1 = -2 * rb.alpha / step_x
                    k2 = 3 * rb.alpha / (2 * step_x) + rb.beta
                    m[-1][0] = k1 - k * m[-2][1]
                    m[-1][1] = k2 - k * m[-2][2]

                return cm, cv
        
        cm, cv = approx(self)
        a, b, c, f = self.a, self.b, self.c, self.f
        theta = 0.5

        m = int((self.max_t - self.min_t) / step_t) + 1
        n = int((self.max_x - self.min_x) / step_x) + 1
        xs = [self.min_x + i * step_x for i in range(n)]
        ts = [self.min_t + i * step_t for i in range(m)]

        u = [[] for i in range(m)]
        u[0] = [self.initial_func(x) for x in xs]
        
        A = a * (1 - theta) / step_x ** 2 - b * (1 - theta) / (2 * step_x)
        B = c * (1 - theta) - 2 * a * (1 - theta) / step_x ** 2 - 1 / step_t
        C = a * (1 - theta) / step_x ** 2 + b * (1 - theta) / (2 * step_x)

        X = b * theta / (2 * step_x) - a * theta / step_x ** 2
        Y = 2 * a * theta / step_x ** 2 - c * theta - 1 / step_t
        Z = - a * theta / step_x ** 2 - b * theta / (2 * step_x)

        U = Matrix(size=(n, 3))
        for i in range(1, n - 1):
            U[i] = [A, B, C]
        cm(U)

        for ti in range(1, m):
            v = Vector(size=(n, 1))
            for xi in range(1, n-1):
                v[xi] =(u[ti-1][xi-1] * X +
                       u[ti-1][xi]   * Y +
                       u[ti-1][xi+1] * Z +
                       (theta - 1) * f(xs[xi], ts[ti]) -
                       theta * f(xs[xi], ts[ti-1]))
            cv(v, ts[ti], U, u[ti-1][0], u[ti-1][-1])
            u[ti] = list(TDMA(U, v).solve())

        return u

if __name__ == '__main__':
    print('test')
