# encoding=utf-8

import random


def guess_num():
    random_num = random.randint(1, 50)

    for i in range(1, 6):
        input_num = int(input(f'第{i}次: 输入一个1-50的数'))
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


def list_repeat():
    src_list = ['a', 'd', 'd', 's', 'a', 'x', 'z', 's', 'd', 'x', 'c']
    restful_list = list(set(src_list))
    print(restful_list)
    # return restful_list
    

if __name__ == '__main__':
    # print(list_repeat())
    a = 100
    b = 10
    if not a % b:
        print(f'{a}/{b}={a//b}')
    else:
        print(a % b)
