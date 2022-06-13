from calendar import c
import subprocess
import os, sys, path
import math

class BaseTest:

    def __init__(self):
        pass

    @staticmethod
    def testing(defaults=None):
        pass
        if type(defaults) == int:
            result = math.factorial(defaults)
            return result
        else:
            return_value = '参数有误'
            return return_value
            
    @staticmethod
    def foo():
        pass
        f_m = int(input('M:'))
        f_n = int(input('N:'))
        return_value = BaseTest.testing(defaults=f_m) // BaseTest.testing(defaults=f_n) // BaseTest.testing(defaults=(f_m-f_n))
        return return_value
        
        


if __name__ == '__main__':
    pass
    # while True:
    # print(BaseTest.testing(defaults=4))
    print(BaseTest.foo())
    

