from constants import *
import random


class Bricks:

    def __init__(this):
        this.bricks = []

    def check_valid_brick(this, r, c):

        for check_brick in this.bricks:
            for a in range(1):
                for b in range(7):
                    for a1 in range(1):
                        for b1 in range(7):
                            if(a+r == a1+check_brick.ret_row() and b+c == b1+check_brick.ret_col()):
                                return 1
        return 0
        # for i in range(7):
        #     for j in range(7):
        #         if(screen[this.row+i][this.col+j] != ' '):
        #             return 1
        # return 0

    def brick_generator(this, defalut=5):
        if(defalut == 0):
            return
        this.row = random.randint(2, game_ht[1]//1.5)
        this.col = random.randint(game_wd[0]+5, game_wd[1] - 10)
        if(this.check_valid_brick(this.row, this.col)):
            defalut -= 1
            this.brick_generator(defalut)
            return
        selected_brick = random.choice(
            [Pink(), Orange(), White(), Unbreak(), Rainbow()])
        #selected_brick = random.choice([Pink(), Unbreak()])
        selected_brick.upd_row(this.row)
        selected_brick.upd_col(this.col)
        this.bricks.append(selected_brick)

    def generateBosslayout(this, count):
        for i in range(count):
            this.unBreakBrick_generator()

    def shieldLayout(this, edge=0):
        for j in range(game_wd[0], game_wd[1]-1, 7):
            this.row = game_ht[1]//3
            this.row += edge
            this.col = j
            selected_brick = random.choice([Pink(), Orange(), White()])
            selected_brick.upd_row(this.row)
            selected_brick.upd_col(this.col)
            selected_brick.boss = levels
            this.bricks.append(selected_brick)

    def unBreakBrick_generator(this, defalut=5):
        if(defalut == 0):
            return
        this.row = random.randint(game_ht[1]//2, (2*game_ht[1])//3)
        this.col = random.randint(game_wd[0]+5, game_wd[1] - 10)
        if(this.check_valid_brick(this.row, this.col)):
            defalut -= 1
            this.brick_generator(defalut)
            return
        selected_brick = Unbreak()
        # selected_brick = Pink()
        selected_brick.upd_row(this.row)
        selected_brick.upd_col(this.col)
        this.bricks.append(selected_brick)

    def generate(this, count):
        for i in range(count):
            this.brick_generator()

    def show(this, screen):
        for brick in this.bricks:
            if(brick.ret_is_broken()):
                for i in range(1):
                    for j in range(7):
                        screen[brick.ret_row()+i][brick.ret_col()+j] = ' '
                continue
            for i in range(1):
                for j in range(7):
                    if(brick.ret_type() <= 0):
                        brick.upd_type(0)
                    if(brick.brick[0] == 4):  # rainbow brick
                        brick.upd_type(random.choice([1, 2, 3]))
                        brick.upd_points(brick.ret_type()*5)
                    screen[brick.ret_row()+i][brick.ret_col() +
                                              j] = brick.ret_type()

    def clear(this, screen, brick):
        for i in range(7):
            screen[brick.ret_row()][brick.ret_col() + i] = " "

    def moveDown(this, screen, score):
        for brick in this.bricks:
            this.clear(screen, brick)
            brick.upd_row(brick.ret_row() + 1)
            if(brick.ret_row() == paddle_row):
                over(score)


class Parent:
    '''Brick Object'''
    def __init__(this):
        this.__is_broken = 0
        this.__row = 0
        this.__col = 0
        this.__type = 0
        this.__points = 0
        this.boss = -1

    def on_collide(this, ball, score, allPowers):
        this.dec_type()
        if(this.ret_type() == 0):
            this.upd_is_broken(1)
            os.system("aplay -q ./sounds/explosion.wav &")
            score.value += this.ret_points()
            chance = random.random()
            # if(chance >= 0.6):
            if(this.boss >= 0):
                chance = 0
            if(chance > 0):
                allPowers.generate_powerup(
                    ball, this.ret_row(), this.ret_col())

    def on_super_collide(this, ball, score, allPowers):
        this.dec_type()
        this.upd_is_broken(1)
        os.system("aplay -q explosion.wav & ")
        score.value += this.ret_points()
        chance = random.random()
        # if(chance >= 0.6):brick
        if(chance >= 0):
            allPowers.generate_powerup(ball, this.ret_row(), this.ret_col())

    def ret_is_broken(this):
        return this.__is_broken

    def upd_is_broken(this, x):
        this.__is_broken = x

    def ret_row(this):
        return this.__row

    def upd_row(this, x):
        this.__row = x

    def upd_col(this, x):
        this.__col = x

    def ret_col(this):
        return this.__col

    def ret_type(this):
        return this.__type

    def dec_type(this):
        this.__type -= 1

    def upd_type(this, x):
        this.__type = x

    def ret_points(this):
        return this.__points

    def upd_points(this, x):
        this.__points = x


class Pink(Parent):

    def __init__(this):
        Parent.__init__(this)
        this.upd_type(1)
        this.upd_points(5)
        this.brick = [1 for i in range(7)]
        # ['1', '1', '1', '1', '1', '1', '1']


class Orange(Parent):

    def __init__(this):
        Parent.__init__(this)
        this.upd_type(2)
        this.upd_points(10)
        this.brick = [2 for i in range(7)]
        # ['2', '2', '2', '2', '2', '2', '2']


class White(Parent):

    def __init__(this):
        Parent.__init__(this)
        this.upd_type(3)
        this.upd_points(15)
        this.brick = [3 for i in range(7)]
#                      ['3', '3', '3', '3', '3', '3', '3']]


class Unbreak(Parent):

    def __init__(this):
        Parent.__init__(this)
        this.upd_type(0)
        this.upd_points(0)
        this.upd_is_broken(0)
        this.brick = [0 for i in range(7)]


class Rainbow(Parent):

    def __init__(this):
        Parent.__init__(this)
        this.upd_type(1)
        this.upd_points(5)
        this.past_type = 0
        this.brick = [4 for i in range(7)]

    def on_collide(this, ball, score, allPowers):
        if(this.brick[0] == 4):  # rainbow
            this.brick[0] = this.ret_type()
            return
        Parent.on_collide(this, ball, score, allPowers)

    def on_super_collide(this, ball, score, allPowers):
        if(this.brick[0] == 4):  # rainbow
            this.brick[0] = this.ret_type()
            return
        Parent.on_super_collide(this, ball, score, allPowers)
