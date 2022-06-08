import subprocess
import os, sys, path
import math

class BaseTest:

    def __init__(self):
        pass

    @staticmethod
    def testing():
        pass
        num = int(input('输入一个正整数:'))
        sqrt = math.sqrt(num)
        status_code = True
        # num = 1
        for i in range(2, num):
            if num % i == 0:
                status_code = False
                break
        if status_code and num != 1:
            print(True)
        else:
            print(False)


if __name__ == '__main__':
    # while True:
    BaseTest.testing()


