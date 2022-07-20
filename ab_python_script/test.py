from calendar import c
import subprocess
import os, sys, path
import math
import interval

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

    @staticmethod
    def test():
        pass
        data_list = [[10.0, 6.0, 2.792526803190927, 3.141592653589793], [8.0, 3.0, 3.141592653589793, 3.4906585039886586]]
        l_1 = [5, 10]
        l_2 = (0, 15)
        l_index = interval.Interval(10, 6)
        l_all = interval.Interval(8,6)
        # print(l_1[0])
        va = l_index.join(l_all)
        # for i in va:
        #     print(i)
        x = min(va)
        print(type(va))
        print(va)
        print(x)
        
        


if __name__ == '__main__':
    pass
    # while True:
    # print(BaseTest.testing(defaults=4))
    # print(BaseTest.foo())
    print(BaseTest.test())
    

