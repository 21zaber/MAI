from lab_5_3.finite_difference.seidel import Seidel


class SOR(Seidel):
    """ Successive over-relaxation (SOR) method """
    def __init__(self, *args, **kwargs):
        self.relax = 1
        if 'relax' in kwargs:
            self.relax = kwargs['relax']
            del kwargs['relax']
        super().__init__(*args, **kwargs)

    def iterate(self):
        super().iterate()
        for i in range(self.n + 1):
            for j in range(self.m + 1):
                self.u[i][j] = self.u[i][j] * self.relax + self.prev_u[i][j] * (1 - self.relax)


if __name__ == '__main__':
    pass
