import random

class Games:
    
    def __init__(self):
        pass
    
    
    @staticmethod
    def guess_game():
        pc_player = random.randint(0,2)
        user_player = input('石头, 剪刀, 布; 请输入-->').strip()
        if str(user_player) == '石头':
            user_player = 2
        elif str(user_player) == '剪刀':
            user_player = 1
        elif str(user_player) == '布':
            user_player = 0
        # 判断输赢
        if ((user_player == 2) and (pc_player == 1)) \
                or ((user_player == 1) and (pc_player == 0)) \
                or ((user_player == 0) and (pc_player == 2)):
            return 'User Win'
        elif user_player == pc_player:
            return '平局'
        else:
            return 'PC Win'
            


# main
if __name__ == '__main__':
    while True:
        print(Games.guess_game())