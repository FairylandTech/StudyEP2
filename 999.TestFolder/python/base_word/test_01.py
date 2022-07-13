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
    filedir = rf'E:\词库'
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
            command_success = rf"MOVE {filepath} E:\temp\词库\完成"
            subprocess.call(command_success, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            # print(command_success)
        except Exception as e:
            print(e)
            command_error = rf"MOVE {filepath} E:\temp\词库\未完成"
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


if __name__ == '__main__':
    print(file_merge())
    # print(file_cut())
