# encoding=utf-8

import random

random_num = random.randint(1, 50)

for i in range(1, 6):
    input_num = int(input(f'第{i}次: 输入一个数'))
    if 1 <= input_num <= 50:
        if input_num == random_num:
            print('猜对了')
            break
        elif input_num < random_num:
            print('猜小了')
        else:
            print('猜大了')
    else:
        print('输入错误, 请重新输入')
    if i == 5:
        print('次数已用完')