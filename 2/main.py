import sys
import time

import math
import numpy as np
import matplotlib.pyplot as plt





class SolveEnergyLevel:

    def __init__(self, m_ratio, V_0, thickness):

        #ディラック定数(J・S)
        hbar = 1.055 * 10 ** (-34)        

        #光速の2乗
        self.c_square = 8.98755179 * 10 ** (16)

        #自由電子質量
        self.m_0 = 0.511 * 10 ** 6
        self.m_0 =self._to_energy(self.m_0)

        #有効質量(eV/c^2)
        self.m = self.m_0 * m_ratio / self.c_square

        #井戸障壁高さ
        self.V_0 = V_0
        self.V_0 =self._to_energy(self.V_0)

        self.radius = self._calc_radius()


        
        
    def create_func(self):

        function_creator = CreateFunction()
        self.xtanx = function_creator.xtanx()
        self.xcotx = function_creator.xcotx()
        self.circle = function_creator.circle_equation(self.radius)
    
    #半径を計算する
    def calc_radius(self):
         return np.sqrt(2 * self.m * self.V_0 * self.a ** 2 / (self.hbar ** 2))


    def _to_energy(self, x):
        return x * 1.602 * 10 ** (-19)

        

def main():
    #問題のパラメータ
    #井戸障壁高さ
    V_0 = 4
    #シリコン層の厚さ(Å
    thickness = 30 *  10 ** (-10)
    #質量比
    m_ratio = 0.7

    solve_energy = SolveEnergyLevel(m_ratio, V_0, thickness)
    solve_energy.create_func()
    
    



if __name__ == '__main__':
    main()
    
