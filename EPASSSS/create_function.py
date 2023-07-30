import numpy as np





class CreateFunction:

    def __init__(self, radius=None):

        #分割数
        N = 10000
        self.x = np.linspace(0, 100, N)
        self.radius = radius


    def xtanx(self):
        
        y1 = self.x * np.tan(self.x)
        y1[y1 > 100] = np.inf
        y1[y1 < -100] = np.inf

        return y1
       

    def mxcotx(self):
        
        y2 = - self.x  / np.tan(self.x)
        y2[y2 > 100] = np.inf
        y2[y2 < -100] = np.inf
        return y2



    def circle_equation(self):
        return np.sqrt(self.radius ** 2self.x ** 2)


    

