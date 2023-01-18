import numpy as np
import pandas as pd


class Hypothesis:
    def __init__(self, x, n):
        self.x = np.array(x)
        self.n = np.array(n)

    def get__x_i(self):
        x_i = []
        for interval in self.x:
            x_i.append(np.average(interval))

        return x_i

    def get_general_n(self):
        return sum(self.n)

    def mean(self):
        x_i = self.get__x_i()
        n_sum = self.get_general_n()
        mean_x = sum(x_i[i]*self.n[i] for i in range(len(x_i)))/n_sum
        return mean_x

    def dispersion(self):
        mean_x = self.mean()
        n_sum = self.get_general_n()
        x_i = self.get__x_i()
        multi = sum((x_i[i])**2 * self.n[i] for i in range(len(x_i)))
        result = multi / n_sum - mean_x**2
        return result

    def standard_deviation(self):
        return self.dispersion() ** 0.5

    def get_z(self):
        z_i = []
        for interval in self.x:
            z_i.append((interval[1] - self.mean())/self.standard_deviation())
        return z_i[0:-1]

    def get_pi(self):
        f_z = np.array([-0.5, -0.491, -0.459, -0.368, -0.187, 0.055, 0.279, 0.419, 0.479, 0.497])
        f_z_i = np.array([-0.491, -0.459, -0.368, -0.187, 0.055, 0.279, 0.419, 0.479, 0.497, 0.5])
        pi = f_z_i - f_z
        return pi[0:-1]

    def for_k_emp(self):
        pi = self.get_pi()
        n_i_v = [round(self.get_general_n()* pi[i], 3) for i in range(len(pi))]
        result = [round((self.n[i] - n_i_v[i])**2 / n_i_v[i], 3) for i in range(len(n_i_v))]
        return result

    def k_empirical(self):
        k_emp = round(sum(self.for_k_emp()), 3)
        return k_emp


class Draw:
    def __init__(self, object: Hypothesis):
        self.object = obj

    def table_av(self):
        mean = self.object.mean()
        dispersion = self.object.dispersion()
        st_d = self.object.standard_deviation()
        data = {'mean' : mean,
                'dispersion' : dispersion,
                'standard deviation' : st_d}

        result = pd.DataFrame.from_dict(data, orient='index')
        return result

    def table_for_hyp(self):
        data = {
            'array' : [interval for interval in self.object.x],
            'n_i' : self.object.n,
            'x_i' : self.object.get__x_i(),
            'Pi' : self.object.get_pi(),
            '(ni - ni`)^2 / ni`' : self.object.for_k_emp()

        }

        table = pd.DataFrame(data, index=range(1, 10))
        return table





array = [[0, 24], [24, 48], [48, 72], [72, 96], [96, 120], [120, 144], [144, 168], [162, 192], [192, 216]]
n_i = [1, 2, 4, 6, 12, 16, 6, 2, 1]
obj = Hypothesis(array, n_i)
print(obj.k_empirical())
table = Draw(obj)
table.table_for_hyp()