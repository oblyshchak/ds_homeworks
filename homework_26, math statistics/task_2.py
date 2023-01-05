import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class MathStat():
    def __init__(self, sample: list):
        self.sample = sample

    def get_frequency(self):
        values_frequency = {}
        for number in sorted(self.sample):
            if number not in values_frequency:
                values_frequency[number] = 1
            else:
                values_frequency[number] += 1
        return values_frequency

    def get_relative_frequency(self):
        # w = n_i/n
        relative_frequency = {}
        sum_v = 0
        for key, value in self.get_frequency().items():
            relative_frequency[key] = value/len(self.sample)
            sum_v += value/len(self.sample)
        if sum_v == 1:
            return relative_frequency

    def get_size(self):
        return max(self.sample) - min(self.sample)

    def get_median(self):
        first = len(self.sample)//2
        second = len(self.sample)//2 + 1
        if len(self.sample) % 2 == 0:
            median = (sorted(self.sample)[first] + sorted(self.sample)[second])//2
        else:
            median = sorted(self.sample)[first]

        return median

    def get_mode(self):
        max_frequency = max(self.get_frequency().values())
        for key, value in self.get_frequency().items():
            if value == max_frequency:
                return key

    def get_sample_average(self):
        x = [i for i in self.get_frequency().keys()]
        n = [i for i in self.get_frequency().values()]
        av_sum = 0
        for i in range(len(x)):
            av_sum += x[i] * n[i]

        return av_sum * (1/len(self.sample))

    def sample_dispersion(self):
        average = self.get_sample_average()
        x = [i for i in self.get_frequency().keys()]
        n = [i for i in self.get_frequency().values()]
        v_sum = 0
        for i in range(len(x)):
            v_sum += n[i] * (x[i]-average)**2

        return v_sum * (1/len(self.sample))

    def standard_deviation(self):
        dispersion = self.sample_dispersion()
        return dispersion**0.5

    def get_Empirical_distribution_function(self):
        x = [i for i in self.get_relative_frequency().keys()]
        n = self.get_relative_frequency().values()
        empirical_dist_func = {}
        f_x = []
        sum = 0
        for v in n:
            sum += v
            f_x.append(sum)

        for i in range(len(f_x)):
            empirical_dist_func[f_x[i]] = x[i]

        return empirical_dist_func


obj = MathStat([10, 13, 10, 9, 9, 12, 12, 6, 7, 9, 8, 9, 11, 9, 14, 13, 9, 8, 8, 7, 10, 10, 11, 11, 11, 12, 8, 7, 9 ,10, 14, 13, 8, 8, 9, 10, 11, 11, 12, 12])



class Draw:
    def __init__(self, obj: MathStat):
        self.obj = obj

    def empirical_dist_func(self):
        data = self.obj.get_Empirical_distribution_function()
        y = [i for i in data.keys()]
        x = [i for i in data.values()]
        plt.style.use('seaborn')
        plt.xlabel('X - axis')
        plt.ylabel('F*(x) - axis')
        plt.step(x, y)
        plt.show()


    def polygon_of_frequencies(self):
        data = self.obj.get_frequency()
        x = [i for i in data.keys()]
        n = [i for i in data.values()]
        plt.plot(x, n, color='green', linestyle='dashed', linewidth = 3,
                 marker='o', markerfacecolor='blue', markersize=12)
        plt.ylim(0)
        plt.xlim(0)
        plt.xlabel('Xi - axis')
        plt.ylabel('Ni - axis')
        plt.title('Frequency polygons')
        plt.show()

    def relative_polygon(self):
        data = self.obj.get_relative_frequency()
        x = [i for i in data.keys()]
        n = [i for i in data.values()]
        plt.plot(x, n, color='green', linestyle='dashed', linewidth = 3,
                 marker='o', markerfacecolor='blue', markersize=12)
        plt.ylim(0)
        plt.xlim(0)
        plt.xlabel('Xi - axis')
        plt.ylabel('Wi - axis')
        plt.title('Frequency polygons')
        plt.show()

    def table(self):
        data_1 = self.obj.get_frequency()
        data_2 = self.obj.get_relative_frequency()
        x = [i for i in data_1.keys()]
        n = [i for i in data_1.values()]
        w = [i for i in data_2.values()]
        data = {'X = x_i' : x,
                'Ni' : n,
                'Wi' : w}
        result = pd.DataFrame.from_dict(data, orient='index', columns=range(1, 10))
        return result




draw_ob = Draw(obj)
draw_ob.polygon_of_frequencies()
draw_ob.relative_polygon()
draw_ob.empirical_dist_func()
print(draw_ob.table())




