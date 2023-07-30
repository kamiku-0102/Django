import sys
import time

import math
import numpy as np

from create_function import CreateFunction


class NewtonMethod:


    def solve(self,ini, epsilon):
        n = 1
        x = ini
        while True:
            if self._df(x) == 0:
                continue
            x = x - self._f(x)/self._df(x)
            n += 1

            if abs(self._f(x)) < epsilon:
                break

            time.sleep(0.5)
            print(x)

        print(f"x = {x}, n = {n}")
        return x

        




    def _f(self, x):
        try:
            return np.sqrt(25.70485 ** 2 - x ** 2) - x * np.tan(x)
        except:
            print(x)
            sys

    def _df(self, x):

        try:
            return - x / np.sqrt(25.70485 ** 2 - x ** 2) - np.tan(x) + x/(np.cos(x) **2)

        except:
            print(x)
            sys

        


        

def main():
    newton_method = NewtonMethod()
    newton_method.solve(3, 0.01)
    
if __name__ == '__main__':
    main()

