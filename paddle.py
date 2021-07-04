import random
from constants import *
from bullets import *


class Paddle:
    def __init__(this):
        this.paddle_size = 14
        this.paddle = ['{', '{', '{', '{', '{', '{', '{',
                       '{', '{', '{', '{', '{', '{', '{']  # 11 sized  40,0 to 40,13
        this.vels = [-6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6]
        this.row = paddle_row
        this.col_start = random.randint(game_wd[0], game_wd[1]-20)
        this.power = 0  # can be 1,2,3
        this.power_timer = 0
        this.is_shoot = 0
        this.shoot_time = 0
        this.bulletManager = Bullets()
        this.cannon = ' '

    def create_vels(this, len):
        vels = []
        for i in range(len):
            j = i+1
            vels.append(j - (len//2))
        return vels

    def expand(this, flag=0):
        if(this.paddle_size == paddle_size):
            this.paddle_size = Ex_paddle_size
            this.paddle = ['}' for i in range(this.paddle_size)]
        elif(this.paddle_size == small_paddle_size):
            this.paddle_size = paddle_size
            this.paddle = ['{' for i in range(this.paddle_size)]
        this.vels = this.create_vels(this.paddle_size)
        if(flag == 0):
            this.power = 1
            this.power_timer = time.time()
        else:
            this.power = 0

    def contract(this, flag=0):
        if(this.paddle_size == paddle_size):
            this.paddle_size = small_paddle_size
            this.paddle = ['}' for i in range(this.paddle_size)]
        elif(this.paddle_size == Ex_paddle_size):
            this.paddle_size = paddle_size
            this.paddle = ['{' for i in range(this.paddle_size)]
        this.vels = this.create_vels(this.paddle_size)
        if(flag == 0):
            this.power = 2
            this.power_timer = time.time()
        else:
            this.power = 0

    def shoot(this):
        this.shoot_time = time.time()
        this.is_shoot = 1
        this.cannon = '^'

    def grab(this):
        this.power = 3
        this.power_timer = time.time()

    def reset(this, screen):
        this.clear(screen)
        this.paddle_size = paddle_size
        this.paddle = ['{' for i in range(this.paddle_size)]
        this.vels = this.create_vels(this.paddle_size)
        this.col_start = random.randint(game_wd[0], game_wd[1]-20)
        this.power = 0
        this.power_timer = 0
        this.is_shoot = 0
        this.shoot_time = 0

    def clear(this, screen):
        # for j in range(len(this.paddle)):
        #     screen[this.row][this.col_start + j] = ' '
        for j in range(game_wd[0]+1, game_wd[1]-2):
            screen[this.row][j] = ' '
        screen[this.row-1][this.col_start] = ' '
        screen[this.row-1][this.col_start + len(this.paddle) - 1] = ' '

    def show(this, screen, bricks, score, allPowers, level):
        this.clear(screen)
        if(time.time() - this.power_timer >= timer_time and this.power != 0):
            if(this.power == 1):
                this.contract(flag=1)
            if(this.power == 2):
                this.expand(flag=1)
        if(time.time() - this.shoot_time >= timer_time and this.is_shoot == 1):
            this.is_shoot = 0
            this.cannon = ' '
        if(this.is_shoot == 1):
            this.bulletManager.generate_bullet(this)

        this.bulletManager.show(screen, bricks, score, allPowers, level)
        for j in range(len(this.paddle)):
            screen[this.row][this.col_start + j] = this.paddle[j]
        screen[this.row-1][this.col_start] = this.cannon
        screen[this.row-1][this.col_start + len(this.paddle) - 1] = this.cannon
