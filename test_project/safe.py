"""
input:
中心点坐标--计算时将其设置为(0,0)
障碍物坐标点[(x1,y1),(x2,y2)....]
最大半径 r
安全半径 sr
output:
扇形区域
[[(r1,θ1),(r1,θ2)
 (r2,θ1),(r2,θ2)],....]
计算逻辑
1.最大半径r进行n(100)等分,写入数组
2.以左侧水平线为0°,每次递增1°,对每个扇形区域进行编号,一圈为m(360)个格子
    可以得到每个扇形区域边界点四个顶点坐标
3.此时将所有扇形区域进行标号,共计(m*n)个
4.遍历障碍物,获得障碍物的坐标点
    随机取100个数据x(0<x<sr),100个角度值sθ(0<sθ<360),获得这100个点的坐标,并判断他们所属的扇形区域,将这些扇形区域标记为安全区
5.遍历所有被标记的扇形区域(0-360号区域也看做被标记的)
    (1)从该点开始向上查找(%360=该格子编号的为该点上面的点),直到找到下一个被标记的点为止,未找到则到边界为止
    (2)分别向左右查找,左右再向上进行查找,直到左边,右边找到了下一个被标记的点
    (3)此范围为需要筛选出的范围,获得该范围的四个顶角坐标,并保存其面积
6.删除掉面积小的,剩余的则返回

圆上点的坐标计算公式:
以圆心点坐标为(0,0)
点的坐标为(x1,y1)
弧度(与x轴正半轴的夹角)为α
则x1 = r*cos(α)
  y1 = r*sin(α)

注意事项:
1. 在扇形区域选择时,向左方向移动为减操作,向右方向移动为加操作
2. 新边旧边的定义
    后绘制的为新边,先绘制的为旧边,按照代码逻辑,左边为旧边,右边为新边
3.由于画图需要,必须新边大于旧边(+2π再和2π取模)
"""
import math

from django.http import JsonResponse
from math import pi, sin, cos, degrees
import numpy as np
import random
import cmath
import copy
import matplotlib.pyplot as plt
import json
import matplotlib
import time
import interval
import operator

def change(list_data,barrier_dict):

    # 障碍物极径列表
    barrier_point = []
    # 障碍物弧度列表
    barrier_radian = []
    # 判断极径是否在敏感点上
    for i in barrier_dict.values():
        if i is not None:
            for j in i:
                barrier_point.append(int(j[0]))
                barrier_radian.append(j[1])
    result_list_temp_1 = []
    result_list_temp_2 = []
    result_list_temp_3 = []
    result_list_temp_4 = []
    # print(f'source-->{len(result_list)}')
    for i in range(len(list_data)):
        # 负的弧度转为正的弧度
        if list_data[i][2] < 0:
            list_data[i][2] = math.radians((360.0 - (abs(list_data[i][2]) / math.pi) * 180))
            if list_data[i][3] < 0:
                list_data[i][3] = math.radians((360.0 - (abs(list_data[i][3]) / math.pi) * 180))
            else:
                pass
        elif list_data[i][3] < 0:
            list_data[i][3] = math.radians((360.0 - (abs(list_data[i][3]) / math.pi) * 180))
            if list_data[i][2] < 0:
                list_data[i][2] = math.radians((360.0 - (abs(list_data[i][2]) / math.pi) * 180))
            else:
                pass
        else:
            pass
        result_list_temp_1.append(list_data[i])
    result_list_temp_1.sort(key=operator.itemgetter(2))
    # print(f'1:负的弧度转为正的弧度-->{len(result_list_temp_1)}')
    # 极坐标中的最小极径修改
    for i in range(len(result_list_temp_1)):
        if result_list_temp_1[i][0] and result_list_temp_1[i][1] not in barrier_point:
            if result_list_temp_1[i][0] > result_list_temp_1[i][1]:
                if result_list_temp_1[i][0] > 3.0:
                    if result_list_temp_1[i][1] < 3.0:
                        result_list_temp_1[i][1] = 3.0
                    else:
                        pass
                else:
                    del result_list[i]
        result_list_temp_2.append(result_list_temp_1[i])
    # print(f'2:最小极径>3-->{len(result_list_temp_2)}')
    # ρ(大)-ρ(小)>1.5KM, 优化极径精度
    for i in range(len(result_list_temp_2)):
        if result_list_temp_2[i][0] - result_list_temp_2[i][1] > 1.5:
            result_list_temp_3.append(result_list_temp_2[i])
        else:
            pass
    for i in range(len(result_list_temp_3)):
        result_list_temp_3[i][0] = round(result_list_temp_3[i][0], 1)
        result_list_temp_3[i][1] = round(result_list_temp_3[i][1], 1)
        if result_list_temp_3[i][3] - result_list_temp_3[i][2] < 0:
            result_list_temp_3[i][3] = math.radians(360.0)
    # print(f'3:ρ(大)-ρ(小)>1.5KM, 优化极径精度-->{len(result_list_temp_3)}')
    # print(result_list_temp_3)
    # 区间去重
    for result_list_temp_3_index in range(len(result_list_temp_3)):
        line_1_temp = [(result_list_temp_3[result_list_temp_3_index][0], result_list_temp_3[result_list_temp_3_index][1]),
                       ()]
        line_2_temp = [result_list_temp_3[result_list_temp_3_index][1], result_list_temp_3[result_list_temp_3_index][2]]
        line_3_temp = [result_list_temp_3[result_list_temp_3_index][2], result_list_temp_3[result_list_temp_3_index][3]]
        line_4_temp = [result_list_temp_3[result_list_temp_3_index][3], result_list_temp_3[result_list_temp_3_index][0]]
        contrast_index = result_list_temp_3_index + 1
        start_radius = result_list_temp_3[result_list_temp_3_index][0]
        stop_radius = result_list_temp_3[result_list_temp_3_index][1]
        start_radian = result_list_temp_3[result_list_temp_3_index][2]
        stop_radian = result_list_temp_3[result_list_temp_3_index][3]
        if contrast_index < len(result_list_temp_3):
            interval_radius = interval.Interval(result_list_temp_3[contrast_index][0],
                                                result_list_temp_3[contrast_index][1])
            interval_radian = interval.Interval(result_list_temp_3[contrast_index][2],
                                                result_list_temp_3[contrast_index][3])
            line_1_contrast_temp = [result_list_temp_3[contrast_index][0], result_list_temp_3[contrast_index][1]]
            line_2_contrast_temp = [result_list_temp_3[contrast_index][1], result_list_temp_3[contrast_index][2]]
            line_3_contrast_temp = [result_list_temp_3[contrast_index][2], result_list_temp_3[contrast_index][3]]
            line_4_contrast_temp = [result_list_temp_3[contrast_index][3], result_list_temp_3[contrast_index][0]]
        else:
            contrast_index = 1
            interval_radius = interval.Interval(result_list_temp_3[contrast_index][0],
                                                result_list_temp_3[contrast_index][1])
            interval_radian = interval.Interval(result_list_temp_3[contrast_index][2],
                                                result_list_temp_3[contrast_index][3])
            line_1_contrast_temp = [result_list_temp_3[contrast_index][0], result_list_temp_3[contrast_index][1]]
            line_2_contrast_temp = [result_list_temp_3[contrast_index][1], result_list_temp_3[contrast_index][2]]
            line_3_contrast_temp = [result_list_temp_3[contrast_index][2], result_list_temp_3[contrast_index][3]]
            line_4_contrast_temp = [result_list_temp_3[contrast_index][3], result_list_temp_3[contrast_index][0]]
        if start_radian in interval_radian:
            if stop_radius == result_list_temp_3[contrast_index][1]:
                # temp_interval = interval.Interval(start_radius, stop_radius)
                # if temp_interval.overlaps(interval_radius):
                #     if start_radian == result_list_temp_3[contrast_index][2]:
                #         result_list_temp_3[contrast_index][3] = stop_radian
                pass
                # result_list_temp_3[contrast_index][1] = start_radius
            else:
                result_list_temp_3[contrast_index][2] = stop_radian
            if stop_radian == result_list_temp_3[contrast_index][3]:
                start_radius_set = (start_radius, result_list_temp_3[contrast_index][0])
                stop_radius_set = (stop_radius, result_list_temp_3[contrast_index][1])
                result_list_temp_3[contrast_index][0] = max(start_radius_set)
                result_list_temp_3[contrast_index][1] = min(stop_radius_set)
            else:
                pass
        else:
            pass
        if start_radian == result_list_temp_3[contrast_index][2] and stop_radian == result_list_temp_3[contrast_index][3]:
            temp_radius_set = (
            start_radius, stop_radius, result_list_temp_3[contrast_index][0], result_list_temp_3[contrast_index][1])
            result_list_temp_3[contrast_index][0] = max(temp_radius_set)
            result_list_temp_3[contrast_index][1] = min(temp_radius_set)
            result_list_temp_3[result_list_temp_3_index][0] = max(temp_radius_set)
            result_list_temp_3[result_list_temp_3_index][1] = min(temp_radius_set)
        if result_list_temp_3[contrast_index][2] != result_list_temp_3[contrast_index][3] and \
                result_list_temp_3[contrast_index][0] != result_list_temp_3[contrast_index][1]:
            result_list_temp_4.append(result_list_temp_3[contrast_index])
    # 列表去重
    result_list_temp_4 = [list(t) for t in set(tuple(_) for _ in result_list_temp_4)]
    # 列表排序
    result_list_temp_4.sort(key=operator.itemgetter(2))
    return result_list_temp_4


def suger(fun):
    def inner(*args, **kwargs):
        a = time.time()
        c = fun(*args, **kwargs)
        b = time.time()
        print(b - a)
        return c

    return inner


# 让极小的数转为0
def exchange_samll_to_zero(data):
    result_list = []
    for i in data:
        if -1e-15 < i < 1e-15:
            result_list.append(0)
        else:
            result_list.append(i)
    return result_list


# Create your views here.
# @suger
def safe_ground():
    # ground_r_big = float(request.POST.get('ground_r'))  # 区域整体半径 单位:公里
    ground_r_big = float(10)  # 区域整体半径 单位:公里
    # Number_of_Angle_segments = int(request.POST.get('Number_of_Angle_segments'))  # 角度分割数量
    Number_of_Angle_segments = int(18)  # 角度分割数量
    # Number_of_radius_segments = int(request.POST.get('Number_of_radius_segments'))  # 半径分割数量
    Number_of_radius_segments = int(5)  # 半径分割数量
    # 障碍物相对圆心的位置
    try:
        barrier_radius_dict_list = '{"school":1,"chemistry":1,"village":1,"government":1,"warehouse":1,"traffic":1}'
        # barrier_radius_dict = json.loads(request.POST.get('barrier_radius_dict'))
        barrier_radius_dict = json.loads(barrier_radius_dict_list)
    except Exception as e:
        return JsonResponse({"state": 400, "message": "failed", 'data': 'barrier_list参数错误'})
    # 遍历障碍物
    # barrier_dict = json.loads(request.POST.get("barrier_dict"))
    # barrier_dict_list = '{"school":[[7.499,4.537856055185257]],"chemistry":[],"village":[[6.186,5.969026041820607],[5.096,1.5009831567151235]],"government":[],"warehouse":[],"traffic":[]}'
    # barrier_dict_list = '{"school":[[7.578,4.974188368183839],[9.333,2.303834612632515]],"chemistry":[[8.276,6.213372137099813],[4.878,1.7453292519943295],[7.432,0.47123889803846897],[4.91,3.7699111843077517]],"village":[[10.386,3.3335788713091694],[5.983,0.3141592653589793],[6.262,0.5410520681182421],[4.037,4.974188368183839]],"government":[],"warehouse":[],"traffic":[]}'
    # barrier_dict_list = '{"school":[[7.578,4.974188368183839],[9.333,2.303834612632515],[7.387,4.4505895925855405],[3.201,0.8028514559173916]],"chemistry":[[8.276,6.213372137099813],[4.878,1.7453292519943295],[7.432,0.47123889803846897],[4.91,3.7699111843077517],[5.037,2.6179938779914944]],"village":[[10.386,3.3335788713091694],[5.983,0.3141592653589793],[6.262,0.5410520681182421],[5.974,5.567600313861911]],"government":[],"warehouse":[],"traffic":[]}'
    barrier_dict_list = '{"school":[[3.206,2.8623399732707004]],"chemistry":[[4.732,0.22689280275926285],[3.89,1.7453292519943295]],"village":[[3.402,2.6354471705114375],[4.133,5.270894341022875],[9.51,2.234021442552742]],"government":[[6.019,3.5779249665883754],[8.669,4.50294947014537],[8.476,0.6981317007977318]],"warehouse":[],"traffic":[]}'
    barrier_dict = json.loads(barrier_dict_list)
    # print(type(barrier_dict), barrier_dict)

    # 区分不同障碍物的安全半径
    safe_radius_school = barrier_radius_dict['school']  # 学校
    safe_radius_chemistry = barrier_radius_dict['chemistry']  # 化工
    safe_radius_village = barrier_radius_dict['village']  # 村庄
    safe_radius_government = barrier_radius_dict['government']  # 政府
    safe_radius_warehouse = barrier_radius_dict['warehouse']  # 军用仓库
    safe_radius_traffic = barrier_radius_dict['traffic']  # 交通路段

    # 所有半径列表
    ground_r_array = np.linspace(0, ground_r_big, Number_of_radius_segments + 1)  # +1是因为101个边才能构建100个扇形
    # print(ground_r_array)
    # 角度分割
    point_array = np.linspace(0, 360, Number_of_Angle_segments + 1) #

    # 保存扇形的位置,扇形编号:{左上,右上,左下,右下}
    sector_dict = {}
    # 获得所有扇形坐标,对扇形进行编号
    for ground_r in range(ground_r_array.shape[0] - 1):  # 遍历半径
        for point in range(point_array.shape[0] - 1):  # 遍历弧度
            # 初始化扇形4个参数
            # 半径
            r_s = ground_r_array[ground_r]
            r_b = ground_r_array[ground_r + 1]

            # 角度
            p_s = point_array[point]
            if point == point_array.shape[0] - 1:
                p_b = point_array[0]
            else:
                p_b = point_array[point + 1]
            # 这里的角度获得的是数值型,360-->2π,需要进行这样的转换才能进行计算
            # θ/360=x/2π---->x(弧度表示) = θ/180*π
            top_left = (r_b * cos(p_b / 180 * pi), r_b * sin(p_b / 180 * pi))  # 左上角点
            top_right = (r_b * cos(p_s / 180 * pi), r_b * sin(p_s / 180 * pi))  # 右上角点
            down_left = (r_s * cos(p_b / 180 * pi), r_s * sin(p_b / 180 * pi))  # 左下角点
            down_right = (r_s * cos(p_s / 180 * pi), r_s * sin(p_s / 180 * pi))  # 右下角点
            # 扇形编号 左下,右下,左上,右上
            sector_dict[Number_of_Angle_segments * ground_r + point] = [down_left, down_right, top_left, top_right]
            # sector_dict[Number_of_Angle_segments * ground_r + point] = [top_right, down_right, down_left, top_left]

    # 被标记的扇形,可能有重复的,故使用集合
    flag_sector_set = set()
    # 遍历障碍物
    for barrier_type, barrier_list in barrier_dict.items():
        for barrier in barrier_list:
            # 传入的为障碍物的极坐标,需要转为直角坐标
            cn1 = cmath.rect(*barrier)
            barrier_x, barrier_y = cn1.real, cn1.imag,
            # 在障碍物的安全区范围取100个点,获得这100个点相对于障碍物的坐标,然后再转换为相对于圆心的坐标,计算在哪个扇形中
            for i in range(10001):
                x = random.uniform(-eval('safe_radius_{}'.format(barrier_type)),
                                   eval('safe_radius_{}'.format(barrier_type)))
                y = random.uniform(-eval('safe_radius_{}'.format(barrier_type)),
                                   eval('safe_radius_{}'.format(barrier_type)))
                if not x ** 2 + y ** 2 <= eval('safe_radius_{}'.format(barrier_type)) ** 2:
                    continue
                coord = (x, y)
                # 将随机点相对于障碍物的坐标转换为该点相对于圆心的坐标
                coord_by_circle = (coord[0] + barrier_x, coord[1] + barrier_y)
                # coord_by_circle = (coord[0] + barrier[0], coord[1] + barrier[1])
                # 获得该坐标的极坐标(角度,半径)
                cn = complex(*coord_by_circle)
                r_temp, radian_temp = cmath.polar(cn)
                # 弧度转为角度--可能出现负值,需要模360
                temp_ponit = degrees(radian_temp) % 360
                # flag_sector = int(r_temp) * 360 + int(temp_ponit)
                # flag_sector_set.add(flag_sector)
                # 已经获得这个点的角度,半径
                # 计算这个点在哪个扇形中
                # 单圈数量*当前所在的圈层数+角度偏差
                # 当前圈数 = r_temp(当前半径)//[ground_r_big(总半径)/Number_of_radius_segments(半径分割数量)]
                # flag_sector = int(r_temp) * 360 + int(temp_ponit)
                now_turns = float(r_temp) // (float(ground_r_big) / int(Number_of_radius_segments))
                # 在当前圈时,根据角度进行编号
                now_angle = Number_of_Angle_segments / 360 * temp_ponit
                # 圈数*每圈的数量*角度偏差
                flag_sector = int(now_turns * Number_of_Angle_segments + now_angle)
                # 有可能产生的随机点在圆外面,这部分不需要采用
                if flag_sector >= Number_of_Angle_segments * Number_of_radius_segments:
                    continue
                flag_sector_set.add(flag_sector)

    # flag_sector_set:不能作业区,  这个 范围需要加上最下面的一圈
    flag_sector_set = list(flag_sector_set) + [i for i in range(Number_of_Angle_segments)]
    # 保存所有4个点上的扇形的编号
    big_sector_list = []
    big_sector_dict = {}

    # 构建数组,可视化圆形区域
    temp = np.zeros((10, 18))
    for flag_sector in flag_sector_set:
        # print([flag_sector // Number_of_Angle_segments, flag_sector % Number_of_Angle_segments])
        temp[flag_sector // Number_of_Angle_segments, flag_sector % Number_of_Angle_segments] = 1

    def get_point_location(point):
        return (point // Number_of_Angle_segments, point % Number_of_Angle_segments)

    # 遍历被标记的格子
    for flag_sector in flag_sector_set:
        # for flag_sector in [0]:
        # print(flag_sector)
        # (1)从该点开始向上查找(+360 等于该格子编号的为该点上面的点),直到找到下一个被标记的点为止,未找到则到边界为止
        # (2)分别向左右查找,左右再向上进行查找,直到左边,右边找到了下一个被标记的点
        # (3)此范围为需要筛选出的范围,获得该范围的四个顶角坐标,并保存其面积
        # top_gird, left_gird, right_gird = 0, 0, 0
        # 1.向上查找  top_gird:上方的点
        # 循环标志
        recycling_symbol = 1
        while True:
            new_grid = flag_sector + Number_of_Angle_segments * recycling_symbol
            top_gird = new_grid
            # 找到了上面被标记的点,那么就返回
            if new_grid in flag_sector_set:
                # 找到的那一行不能取,向前退一行
                top_gird -= Number_of_Angle_segments
                break
            # 或者到顶了
            if new_grid > Number_of_Angle_segments * Number_of_radius_segments - 1:
                # 击中的那一行不选择,后退一行
                top_gird -= Number_of_Angle_segments
                break
            recycling_symbol += 1
        # 被标记区域上面还有被标记的,那么是不可能有面积的
        if top_gird == flag_sector:
            continue
        # 2.向左查找,同时需要向左边的上方查找 new_grid_left 标记左边的点
        # 起始点为top_gird左边的点
        left_flag = False
        left_flag_sector = copy.deepcopy(top_gird)
        # 向左移动的数量:
        left_move_count = 0
        for i in range(1, Number_of_Angle_segments + 1):
            recycling_symbol = 0
            # 获得标记点左边的点  只能在本圈中查找,即如果整除为0时,将数字加360,继续筛选
            if left_flag_sector // Number_of_Angle_segments == (left_flag_sector - 1) // Number_of_Angle_segments:
                left_flag_sector -= 1
            else:
                left_flag_sector = left_flag_sector - 1 + Number_of_Angle_segments
            # if left_flag_sector % Number_of_Angle_segments == 0:
            #     left_flag_sector += Number_of_Angle_segments
            while True:
                new_grid = left_flag_sector - Number_of_Angle_segments * recycling_symbol
                left_gird = new_grid
                if new_grid in flag_sector_set:
                    # 可能找到最底部了(和障碍物在一行的格子,这是不能取的)
                    if new_grid // Number_of_Angle_segments == flag_sector // Number_of_Angle_segments:
                        break
                    else:
                        # 找到了左边上面被标记的格子,那么返回,并不继续向左查找了
                        left_flag = True
                        break
                # 或者到底部(选择障碍物所在的行)
                if new_grid // Number_of_Angle_segments == flag_sector // Number_of_Angle_segments:
                    break
                recycling_symbol += 1
            left_move_count += 1
            if left_flag:
                # 在当前列找到了,所以当前列不能取
                # 同样需要判断-1后是否会跳到下一行去了

                if left_flag_sector // Number_of_Angle_segments == (top_gird) // Number_of_Angle_segments:
                    left_flag_sector += 1
                else:
                    left_flag_sector = left_flag_sector + 1 - Number_of_Angle_segments
                # 等于圆分隔数*半径分隔数时,需要退一行
                if left_flag_sector == Number_of_Angle_segments * Number_of_radius_segments:
                    left_flag_sector -= Number_of_Angle_segments

                # left_flag_sector += 1
                break

        # 3.向右查找,同时需要向右边的上方查找 new_grid_right 右边被标记的点
        right_flag = False
        right_flag_sector = copy.deepcopy(top_gird)
        # 向右移动点的数量
        right_move_count = 0
        for i in range(1, Number_of_Angle_segments + 1):
            recycling_symbol = 0
            # 获得标记点右边的点 只能在本圈中查找,即如果整除为0时,将数字减360,继续筛选
            if right_flag_sector // Number_of_Angle_segments == (right_flag_sector + 1) // Number_of_Angle_segments:
                right_flag_sector += 1
            else:
                right_flag_sector = right_flag_sector + 1 - Number_of_Angle_segments
            # if right_flag_sector % Number_of_Angle_segments == 0:
            #     right_flag_sector += Number_of_Angle_segments

            while True:
                new_grid = right_flag_sector - Number_of_Angle_segments * recycling_symbol
                right_gird = new_grid
                if new_grid in flag_sector_set:
                    if new_grid // Number_of_Angle_segments == flag_sector // Number_of_Angle_segments:
                        break
                    # 找到了左边上面被标记的格子,那么返回,并不继续向左查找了
                    right_flag = True
                    break
                # 或者到顶了
                if new_grid // Number_of_Angle_segments == flag_sector // Number_of_Angle_segments:
                    break
                recycling_symbol += 1
            right_move_count += 1
            if right_flag:
                # 在当前列找到了,所以当前列不能取
                # 同样需要判断-1后是否会跳到下一行去了
                if right_flag_sector // Number_of_Angle_segments == (right_flag_sector - 1) // Number_of_Angle_segments:
                    right_flag_sector -= 1
                else:
                    right_flag_sector = right_flag_sector - 1 + Number_of_Angle_segments
                if right_flag_sector == Number_of_Angle_segments * Number_of_radius_segments:
                    right_flag_sector -= Number_of_Angle_segments

                # right_flag_sector -= 1
                break
        # 四个点位置:左下,右下(距离作业点最近的下边界)
        #            左上,右上(距离作业点最远的下边界)
        # 添加保存第五个数据,扫过的格子的数量.原因:使用极坐标计算相对位置,可能会出错,直接减的话可能会减错范围
        safe_area = (
            # 左下
            (flag_sector // Number_of_Angle_segments) * Number_of_Angle_segments +
            left_flag_sector % Number_of_Angle_segments + Number_of_Angle_segments,
            # 右下
            (flag_sector // Number_of_Angle_segments) * Number_of_Angle_segments +
            right_flag_sector % Number_of_Angle_segments + Number_of_Angle_segments,
            # 左上              右上          移动的格子数量 因为2边都多算了1个,需要减掉
            left_flag_sector, right_flag_sector, right_move_count + left_move_count - 1)
        big_sector_list.append(safe_area)
        # 保存  障碍点:4个边界
        big_sector_dict[flag_sector] = safe_area

    # 定义角度的转换,因为极坐标转换出来是[-π,π],我们的角度是[0,2π],
    # 需要进行转换,将转换出来小于0的数据x,使用(2π-θ)进行替代
    def angle_conversion(angle):
        if angle < 0:
            return 2 * pi + angle
        else:
            return angle

    filter_set = set()
    # key_list = []
    iter_dict = {}
    for index, value in big_sector_dict.items():
        if value not in filter_set:
            filter_set.add(value)
            # key_list.append(index)
            iter_dict[index] = value

    # 返回的数据
    result_list = []
    # 保存所有面积,画一个直方图
    temp_list = []
    # 遍历符合的扇形区域,计算其面积
    # 扇形面积计算公式:角度制:（n/360）πR²
    # 用左边减去右边(新边减去旧边)
    # for big_sector in key_list:
    for big_sector in iter_dict.keys():
        # for big_sector in big_sector_list:
        # 1.4个坐标转为极坐标,分别取对应的点,计算角度和半径,再计算面积
        # 小扇形保存:左下,右下,左上,右上
        # 先取出所属的扇形,再取出所属的位置
        # 如果没有进行左右移动(即count为1),即只有一列数据,那么左右需要选择扇形的左右(注意新旧的区分)
        if not big_sector_dict[big_sector][4] == 1:
            # 左上点
            sector_left_up = sector_dict[big_sector_dict[big_sector][2]][2]
            # 左下点
            sector_left_down = sector_dict[big_sector_dict[big_sector][0]][0]
            # # 右上点
            # sector_right_up = sector_dict[big_sector_dict[big_sector][3]][3]
            # # 右下点
            # sector_right_down = sector_dict[big_sector_dict[big_sector][1]][1]
            # 右上点
            sector_right_up = sector_dict[big_sector_dict[big_sector][3]][2]
            # 右下点
            sector_right_down = sector_dict[big_sector_dict[big_sector][1]][0]
        else:
            # 左上点
            sector_left_up = sector_dict[big_sector_dict[big_sector][2]][3]
            # 左下点
            sector_left_down = sector_dict[big_sector_dict[big_sector][0]][1]
            # 右上点
            sector_right_up = sector_dict[big_sector_dict[big_sector][3]][2]
            # 右下点
            sector_right_down = sector_dict[big_sector_dict[big_sector][1]][0]
        # 直角坐标转极坐标
        # 获得四个顶点对应的极坐标
        # 半径,弧度
        # 左上
        polar_coordinates_sector_left_up_r, polar_coordinates_sector_left_up_radian = cmath.polar(
            complex(*sector_left_up))
        # 左下
        polar_coordinates_sector_left_down_r, polar_coordinates_sector_left_down_radian = cmath.polar(
            complex(*sector_left_down))
        # 右上
        polar_coordinates_sector_right_up_r, polar_coordinates_sector_right_up_radian = cmath.polar(
            complex(*sector_right_up))
        # 右下
        polar_coordinates_sector_right_down_r, polar_coordinates_sector_right_down_radian = cmath.polar(
            complex(*sector_right_down))
        # 面积计算  180*弧度/π
        # 移动格子的数量  数量乘以当初设置的角度分割度数,就是实际的扇形圆周角度数
        count = big_sector_dict[big_sector][4]
        point_temp = count / Number_of_Angle_segments
        # 计算大扇形面积
        # 使用弧度制计算  180*弧度/π
        # S_big = ((angle_conversion(polar_coordinates_sector_left_up_radian) - angle_conversion(
        #     polar_coordinates_sector_right_up_radian)) * (polar_coordinates_sector_left_up_r) ** 2) * 1 / 2
        # # 计算小扇形面积
        # S_small = ((angle_conversion(polar_coordinates_sector_left_up_radian) - angle_conversion(
        #     polar_coordinates_sector_right_up_radian)) * (polar_coordinates_sector_left_down_r) ** 2) * 1 / 2
        # 使用角度制计算  （n/360）πR²
        S_big = pi * (polar_coordinates_sector_left_up_r ** 2) * point_temp
        # 计算小扇形面积
        S_small = pi * (polar_coordinates_sector_left_down_r ** 2) * point_temp

        S_sector = abs(S_big) - abs(S_small)
        # if S_sector > 5000:
        #     print(big_sector)
        #     print(S_sector)
        # 保存4个点的坐标,面积----左下,右下,左上,右上,面积  不选取这个了
        # print(sector_left_down, sector_right_down)
        # temp_sector = [sector_left_down, sector_right_down, sector_left_up, sector_right_up, S_sector]
        # 绘图需要处理,必须新边大于旧边
        difference = polar_coordinates_sector_right_up_radian - polar_coordinates_sector_left_up_radian
        if difference < 0:
            polar_coordinates_sector_right_up_radian += 2 * pi
        # polar_coordinates_sector_left_up_radian = (polar_coordinates_sector_left_up_radian + 2 * pi) % 2 * pi
        # polar_coordinates_sector_right_up_radian = (polar_coordinates_sector_right_up_radian + 2 * pi) % 2 * pi
        # 保存外圆半径,内圆半径,左角度(旧边),右角度(新边)
        temp_sector = [polar_coordinates_sector_left_up_r, polar_coordinates_sector_left_down_r,
                       polar_coordinates_sector_left_up_radian, polar_coordinates_sector_right_up_radian]
        # polar_coordinates_sector_right_up_radian,polar_coordinates_sector_left_up_radian]
        result_list.append(temp_sector)
        temp_list.append(S_sector)

    # matplotlib.use('Agg')
    # matplotlib.rcParams['font.family'] = 'SimHei'
    # matplotlib.rcParams['axes.unicode_minus'] = False
    # plt.hist(temp_list, 100)
    # plt.show()
    # [print(i) for i in result_list]
    res_data = {"state": 200, "message": "Successfully", 'data': result_list}
    # print(result_list)
    f_1 = change(result_list, barrier_dict=barrier_dict)
    # f_2 = change(f_1, barrier_dict=barrier_dict)
    # f_3 = change(f_2, barrier_dict=barrier_dict)
    [print(i) for i in f_1]

    # 返回值
    f_1 = {"state": 200, "message": "Successfully", 'data': f_1}
    return f_1
    # return JsonResponse(data=res_data, json_dumps_params={'ensure_ascii': False})
    # return res_data


if __name__ == '__main__':
    # for num in range(10):
    #     if num == 9:
    #         print(safe_ground())
    #     else:
    #         safe_ground()
    print(safe_ground())



