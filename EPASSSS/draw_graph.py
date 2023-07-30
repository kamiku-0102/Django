import sys

import math
import numpy as np
import matplotlib.pyplot as plt

from create_function import CreateFunction




class DrawGraph:



    def __init__(self, radius):

        #おまじない
        self.figure, self.axes = plt.subplots()


        #x^2+y^2の平方根
        self.radius = radius        
        self._define_func()
        self._set_xaxis()
        



    def _define_func(self):
        function_creator = CreateFunction()
        self.y1 = function_creator.xtanx()
        self.y2 = function_creator.mxcotx()




    def draw_graph(self):
        self.y1[self.y1 > 100] = np.inf
        self.y1[self.y1 < -100] = np.inf

        self.y2[self.y2 > 100] = np.inf
        self.y2[self.y2 < -100] = np.inf        

        plt.plot(self.x, self.y1, color='r', ls='-')
        plt.plot(self.x, self.y2, color='b', ls='-.')        
        self._draw_circle()
        lim = math.ceil(self.radius)+0.5
        self._set_xaxis()
        self._set_lim(lim, lim)
        self._comp_graph()
        plt.show()

    def _set_xaxis(self):
        N = 10000
        self.x = np.linspace(0,100,N)
        

        
        
    #端の設定
    def _set_lim(self, xlim, ylim):
        plt.xlim(0,xlim)
        plt.ylim(0,ylim)
        


    #ラベルをつける
    def _comp_graph(self):
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('y')

    #円を描く
    def  _draw_circle(self):        
        draw_circle = plt.Circle((0,0), self.radius, fill=False)
        self.axes.set_aspect(1)
        self.axes.add_artist(draw_circle)


def main():
    radius = 30
    draw_graph = DrawGraph(radius)
    draw_graph.draw_graph()
    




if __name__ == "__main__":
    main()
