# coding: utf-8


import math
import numbers
import re
import time
import logging
import datetime
import string

logging.basicConfig(level=logging.DEBUG,
                    filename='./topic_error.log',
                    format='%(asctime)s %(levelname)-4s %(pathname)s %(lineno)d %(message)s',
                    )


class Topics:

    def __init__(self):
        pass

    @classmethod
    def case_001(cls):
        """
        有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
        :return: 
        """
        count: int = 0
        space: list = list()
        for h in range(1, 5):
            for m in range(1, 5):
                for s in range(1, 5):
                    if h != m != s and h != s:
                        result = int(f'{h}{m}{s}')
                        space.append(result)
                        count += 1
        return count, space

    @classmethod
    def case_002(cls, i: float):
        """
        企业发放的奖金根据利润提成
        利润(I)低于或等于10万元时，奖金可提10%; 利润高于10万元，低于20万元时，低于10万元的部分按10%提成; 高于10万元的部分，可提成7.5%;
        20万到40万之间时，高于20万元的部分，可提成5%; 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%
        高于100万元时，超过100万元的部分按1%提成
        从键盘输入当月利润I，求应发放奖金总数？
        :return: 
        """
        arr = [100, 60, 40, 20, 10, 0]
        rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
        r = 0
        for index in range(0, 6):
            if i > arr[index]:
                r += (i - arr[index]) * rat[index]
                i = arr[index] + 1
        return round((r * 10000), 2)

    @classmethod
    def case_003(cls):
        """
        一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
        :return: 
        """
        num = 0
        while True:
            num += 1
            if math.sqrt(100 + num) % 1 == 0:
                if math.sqrt(100 + 168 + num) % 1 == 0:
                    break
        return num

    @classmethod
    def case_004(cls, year, month, day):
        """
        输入某年某月某日，判断这一天是这一年的第几天？
        :return: 
        """
        try:
            result = time.strptime(f'{year}{month}{day}', '%Y%m%d').tm_yday
            return result
        except Exception as error:
            logging.exception(error)
            return error

    @classmethod
    def case_005(cls, x, y, z: float):
        """
        输入三个整数x,y,z，请把这三个数由小到大输出。
        :return: 
        """
        try:
            list_spaces = [x, y, z]
            list_spaces.sort()
            return tuple(list_spaces)
        except Exception as error:
            logging.exception(error)
            return error

    @classmethod
    def case_006(cls, n=10):
        """
        斐波那契数列
        输出前 10 个斐波那契数列
        :return: 
        """
        list_spaces = []
        a, b = 1, 1
        for i in range(n - 1):
            list_spaces.append(a)
            a, b = b, a + b
        return list_spaces

    @classmethod
    def case_007(cls):
        """
        将一个列表的数据复制到另一个列表中。
        :return: 
        """
        src_list = [1, 2, [3, 4], (5, 6), {'index': 7}, {8, 9}]
        target_list = src_list.copy()
        return target_list

    @classmethod
    def case_008(cls):
        """
        输出 9*9 乘法口诀表
        :return: 
        """
        for i in range(1, 9 + 1):
            for j in range(1, 9 + 1):
                print(f'{j}x{i}={i * j}\t', end='')
                if i == j:
                    break
            print('\n', end='')
        return True

    @classmethod
    def case_009(cls):
        """
        暂停一秒输出。
        :return: 
        """
        time.sleep(1)
        return 0

    @classmethod
    def case_010(cls):
        """
        暂停一秒输出，并格式化当前时间。
        :return: 
        """
        result = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        time.sleep(1)
        return result

    @classmethod
    def case_011(cls):
        """
        有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
        :return: 
        """
        # 第一个月的数量
        month_1 = 1
        # 第二个月的数量
        month_2 = 1
        result = []
        for i in range(1, 13):
            result.append(month_1)
            result.append(month_2)
            if (i % 3) == 0:
                pass
            # 第三个月的数量
            month_1 = month_1 + month_2
            # 第四个月的数量
            month_2 = month_1 + month_2
        return result

    @classmethod
    def case_012(cls):
        """
        判断101-200之间有多少个素数，并输出所有素数。
        :return: 
        """
        result = []
        status = True
        for num_1 in range(101, 201):
            for num_2 in range(2, num_1):
                if num_1 % num_2 == 0:
                    status = False
                    break
            if status is True:
                result.append(num_1)
            else:
                status = True
        return result, len(result)

    @classmethod
    def case_013(cls):
        """
        打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
        :return: 
        """
        result = []
        for index in range(100, 1000):
            high = index // 100
            medium = index // 10 % 10
            low = index % 10
            if index == math.pow(high, 3) + math.pow(medium, 3) + math.pow(low, 3):
                result.append(index)
        return result

    @classmethod
    def case_014(cls, number: int):
        """
        将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
        :return: 
        程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
        (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
        (2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
        (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
        """
        result = f'{number}='
        status = True
        while status:
            for index in range(2, number + 1):
                if not number % index:
                    if index == number:
                        status = False
                        result += str(index)
                    else:
                        s = str(index) + '*'
                        result += s
                        number = number // index
                    break
        return result

    @classmethod
    def case_015(cls, grade: int):
        """
        利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
        :return: 
        """
        if grade >= 90:
            return 'A'
        elif 60 <= grade <= 89:
            return 'B'
        else:
            return 'C'

    @classmethod
    def case_016(cls):
        """
        输出指定格式的日期。
        使用datatime模块
        :return: 
        """
        # 只有日期 没有时间
        result = datetime.date.today().strftime('%Y-%m-%d')
        return result

    @classmethod
    def case_017(cls, date: str):
        """
        输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
        :return: 
        """
        # init 
        letters = 0
        spaces = 0
        digits = 0
        other_chars = 0
        for index in date:
            if index.isalpha():
                letters += 1
            elif index.isspace():
                spaces += 1
            elif index.isdigit():
                digits += 1
            else:
                other_chars += 1
        result = f'字母: {letters}, 空格: {spaces}, 数字 {digits}, 其他字符: {other_chars}'
        return result

    @classmethod
    def case_018(cls, digit: int, number: int):
        """
        求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)
        :param digit: a
        :param number: 数量
        :return: 
        """
        digits_sum = 0
        for index in range(1, number + 1):
            digits = int(str(digit) * index)
            digits_sum += digits
        return digits_sum

    @classmethod
    def case_019(cls):
        """
        一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
        :return: 
        """
        result = []
        for digit_index in range(2, 1000):
            digits_sum = 1
            for index in range(2, digit_index):
                if digit_index % index == 0:
                    digits_sum += index
            if digits_sum == digit_index:
                result.append(digit_index)
        return result

    @classmethod
    def case_020(cls):
        """
        球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
        :return: 
        """
        height = 100
        long = height
        for index in range(1, 11):
            height /= 2
            if index == 10:
                pass
            else:
                long += height * 2
        result = f'高度： {height}, 经过的距离： {long}'
        return result


if __name__ == '__main__':
    cut_line = '-' * 50
    print(f'case_001: {Topics.case_001()}\n{cut_line}')
    print(f'case_002: {Topics.case_002(i=23)}\n{cut_line}')
    print(f'case_003: {Topics.case_003()}\n{cut_line}')
    print(f'case_004: {Topics.case_004(year=2021, month=12, day=31)}\n{cut_line}')
    print(f'case_005: {Topics.case_005(x=2, y=1, z=3)}\n{cut_line}')
    print(f'case_006: {Topics.case_006()}\n{cut_line}')
    print(f'case_007: {Topics.case_007()}\n{cut_line}')
    print(f'case_008: {Topics.case_008()}\n{cut_line}')
    print(f'case_009: {Topics.case_009()}\n{cut_line}')
    print(f'case_010: {Topics.case_010()}\n{cut_line}')
    print(f'case_011: {Topics.case_011()}\n{cut_line}')
    print(f'case_012: {Topics.case_012()}\n{cut_line}')
    print(f'case_013: {Topics.case_013()}\n{cut_line}')
    print(f'case_014: {Topics.case_014(number=496)}\n{cut_line}')
    print(f'case_015: {Topics.case_015(grade=88)}\n{cut_line}')
    print(f'case_016: {Topics.case_016()}\n{cut_line}')
    print(f'case_017: {Topics.case_017(date="abc 123 ,./ ")}\n{cut_line}')
    print(f'case_018: {Topics.case_018(digit=4, number=4)}\n{cut_line}')
    print(f'case_019: {Topics.case_019()}\n{cut_line}')
    print(f'case_020: {Topics.case_020()}\n{cut_line}')
