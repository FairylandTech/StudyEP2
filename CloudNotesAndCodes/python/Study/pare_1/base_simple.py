# coding=utf-8


class BaseSimple:

    def __init__(self):
        pass

    @staticmethod
    def var_sum(num_1, num_2):
        return f'{num_1}和{num_2}两数之和为: {num_1 + num_2}'

    @staticmethod
    def data_type(data):
        return f'\"{data}\"的数据类型为: {type(data)}'

    class StrMore:

        def __init__(self):
            pass

        @staticmethod
        def str_long(data):
            return f'字符串\"{data}\"的长度为: {len(data)}'

        @staticmethod
        def str_step(data):
            return data




if __name__ == '__main__':
    # 1. 两数相加
    print('1. 两数相加\n', BaseSimple.var_sum(num_1=4, num_2=6))
    # 2. 数据类型: int, float, bool ,str, list, tuple, dict, set
    print('2. 数据类型\n', BaseSimple.data_type(data=False))
    # 3. 字符串
    ## 3.1 字符串的转义
    """
    \n, 换行符
    \t, 横向制表位
    \v, 纵向制表位
    \r, 回车: Enter
    \b, 退格: BackSpace
    \f, 换页
    
    """
    ## 3.2 字符串的基本运算
    ### 3.2.1 字符串长度
    print('3. 字符串长度\n', BaseSimple.StrMore.str_long("long_data"))
    ### 3.2.2 字符串切片
    '''
    - 格式: [开始:结束:步长]  步长起始为1, 开始起始为0
    eg :
    [0:6]: 左闭右开区间 >>> 0 1 2 3 4 5
    [2:7:2]: [2:7]左闭右开区间 >>> 2 3 4 5 6, 步长为2 >>> 2 4 6
    [3:]: 从3开始直到结束 >>> 3 4 5 6 7 8 9
    [:5]: 从0开始到4结束 >>> 0 1 2 3 4
    [2::3]: 从2开始到结束 >>> 2 3 4 5 6 7 8 9, 步长为3 >>> 2 5 8
    '''
    print('3. 字符串切片\n', f'原字符串: {BaseSimple.StrMore.str_step("0123456789")}',BaseSimple.StrMore.str_step("0123456789")[2::3])






