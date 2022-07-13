# -*- coding: utf-8 -*-
import os

filename = "result.txt"  # 需要进行分割的文件
# size = 10000000
size = 350000


def mk_SubFile(srcName, sub, buf):
    [des_filename, extname] = os.path.splitext(srcName)
    filename = rf'./data_dic/{str(sub)}_{des_filename}{extname}'
    print('正在生成子文件: %s' % filename)
    with open(filename, 'w', encoding='utf-8') as fout:
        fout.write(buf)
        return sub + 1


def split_By_size(filename, size):
    with open(filename, 'r', encoding='utf-8') as f:
        buf = f.read(size)
        sub = 1
        while len(buf) > 0:
            sub = mk_SubFile(filename, sub, buf)
            buf = f.read(size)
    print("ok")


if __name__ == "__main__":
    split_By_size(filename, size)
