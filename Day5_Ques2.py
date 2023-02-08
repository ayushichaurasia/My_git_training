# Ques 2: Create arithmetics class to calculate avg, mean, mode and standard deviation


import numpy as np


class Arithmetic:
    def __init__(self, data):
        self.data = np.array(data)

    def average(self):
        return np.mean(self.data)

    def mean(self):
        return np.mean(self.data)

    def mode(self):
        return np.argmax(np.bincount(data))

    def standard_deviation(self):
        return np.std(self.data)


data = np.array(input("Enter numbers: ").split(), dtype=int)
ar = Arithmetic(data)

print("Average:", ar.average())
print("Mean:", ar.mean())
print("Mode:", ar.mode())
print("Standard deviation:", ar.standard_deviation())