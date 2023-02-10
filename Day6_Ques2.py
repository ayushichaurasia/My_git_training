import statistics as st
from collections import Counter

class Arithmetic:

    @staticmethod
    def avg(num):
        return sum(num)/len(num)

    @staticmethod
    def mean(num):
        return Arithmetic.avg(num)

    @staticmethod
    def mode(num):
        return st.mode(num)

    @staticmethod
    def standard_deviation(num):
        return st.stdev(num)

num = list(map(int, input("Please enter numbers:").split()))
ar = Arithmetic()
print(ar.avg(num))
print(ar.mean(num))
print(ar.mode(num))
print(ar.standard_deviation(num))
