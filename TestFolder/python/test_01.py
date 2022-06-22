from calendar import c
import subprocess
import os, sys, path
import math
import interval


class BaseTest:

    def __init__(self):
        """
        Constructor
        """
        pass

    @staticmethod
    def testing(default=None):
        """
        This function is used to test the program.
        :param default:
        :return: None
        """
        pass

    @staticmethod
    def factorial(default=None):
        """
        阶乘函数
        :param default:
        :return:
        """
        try:
            return math.factorial(default)
        except Exception as e:
            print(e)


    @staticmethod
    def fibonacci_sequence():
        """
        Fibonacci sequence
        :return:
        """
        a, b = 0, 1
        for _ in range(20):
            a, b = b, a + b
            print(a, end=' ')
        return 'Done'


if __name__ == '__main__':
    """
    This is the main function.
    """
    print(BaseTest.fibonacci_sequence())


