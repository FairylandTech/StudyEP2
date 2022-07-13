# coding=utf-8
import os
import subprocess
import time, datetime
#
import cut_file


# 文件合并
def file_merge():
    # 开始时间
    start_time = datetime.datetime.now()
    # 获取目标文件夹的路径
    # filedir = rf'D:\File\docs\词库\搜狗输入法\搜狗词库-TXT版本'
    # WorkSpaceDir
    filedir = rf'D:\File\docs\词库\搜狗输入法\搜狗词库-TXT版本'
    # 获取当前文件夹中的文件名称列表
    filenames = os.listdir(filedir)
    # 打开当前目录下的result.txt文件，如果没有则创建
    f = open(rf'./result.txt', 'w', encoding='utf-8')
    # 先遍历文件名
    for filename in filenames:
        filepath = filedir + '\\' + filename
        try:
            # 遍历单个文件，读取行数
            for line in open(filepath, 'r', encoding='utf-8'):
                # 写入新文件
                f.writelines(line)
            # f.write('\n')
            # command_success = rf"MOVE {filepath} D:\File\docs\词库\搜狗输入法\完成合并"
            # WorkSpaceDir
            command_success = rf"MOVE {filepath} D:\File\docs\词库\搜狗输入法\完成合并"
            subprocess.call(command_success, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            # print(command_success)
        except Exception as e:
            print(e)
            # command_error = rf"MOVE {filepath} D:\File\docs\词库\搜狗输入法\未完成合并"
            # WorkSpaceDir
            command_error = rf"MOVE {filepath} D:\File\docs\词库\搜狗输入法\未完成合并"
            subprocess.call(command_error, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            print(command_error)
            pass
    f.close()
    # 结束时间
    stop_time = datetime.datetime.now()
    run_time = stop_time - start_time
    return run_time


# 文件拆分
def file_cut():
    for index in range(600):
        save_name = rf'data_dic\cat{str(index + 1)}.txt'
        save_data = open(file=save_name, mode='w', encoding='utf-8')
        for line in open(file='result.txt', mode='r', encoding='utf-8'):
            save_data.write(line)
            file_size = round(os.path.getsize(save_name) / 1024)
            if file_size >= 1010:
                break

    return True


def bin_to_text():
    pass


if __name__ == '__main__':
    pass
    # print(file_merge())
    # print(file_cut())

    bin_to_text()
