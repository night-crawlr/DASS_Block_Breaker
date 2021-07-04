from constants import *
import random


class Bullets:
    def __init__(this):
        this.bullets = []

    def generate_bullet(this, paddle):
        bullet = Bullet()
        bullet.start(paddle)
        this.bullets.append(bullet)

    def collison_top(this, bullet):
        if(bullet.row1 <= game_ht[0] or bullet.row2 <= game_ht[0]):
            return 1
        return 0

    def remove(this, i):
        this.bullets.pop(i)

    def handle_collisions(this, bullet, bricks, score, allPowers):
        for brick in bricks.bricks:
            if(brick.ret_is_broken() == 1 and brick.brick[0] != 0):
                continue
            flag1 = 0
            flag2 = 0
            if(bullet.row1 <= brick.ret_row() and ((brick.ret_col() <= bullet.col_1) and (bullet.col_1 <= brick.ret_col() + 7 - 1)) and bullet.is_broken1 == 0):
                brick.on_collide(bullet, score, allPowers)
                bullet.is_broken1 = 1
                bullet.row1 = brick.ret_row() + 1
                bullet.char1 = ' '
                flag1 = 1
            if(bullet.row2 <= brick.ret_row() and ((brick.ret_col() <= bullet.col_2) and (bullet.col_2 <= brick.ret_col() + 7 - 1)) and bullet.is_broken2 == 0):
                brick.on_collide(bullet, score, allPowers)
                bullet.is_broken2 = 1
                bullet.row2 = brick.ret_row() + 1
                bullet.char2 = ' '
                flag2 = 1
            if(flag1 or flag2):
                break

    def show(this, screen, bricks, score, allPowers, level):
        # if(this.bullets == [] and level.value != 1):
        #     quit()
        for i, bullet in enumerate(this.bullets):
            if(bullet.is_broken1 == 1 and bullet.is_broken2 == 1):
                screen[bullet.row1][bullet.col_1] = ' '
                screen[bullet.row2][bullet.col_2] = ' '
                this.remove(i)
            screen[bullet.row1][bullet.col_1] = ' '
            screen[bullet.row2][bullet.col_2] = ' '
            if(this.collison_top(bullet)):
                this.remove(i)
                continue
            bullet.row1 += bullet.row_vel
            bullet.row2 += bullet.row_vel
            this.handle_collisions(bullet, bricks, score, allPowers)
            if(bullet.is_broken1 != 1):
                screen[bullet.row1][bullet.col_1] = level.value
            if(bullet.is_broken2 != 1):
                screen[bullet.row2][bullet.col_2] = level.value


class Bullet:
    def __init__(this):
        this.row1 = 0
        this.row2 = 0
        this.col_1 = 0
        this.col_2 = 0
        this.is_broken1 = 0
        this.is_broken2 = 0
        this.char1 = "T"
        this.char2 = "T"
        this.row_vel = -2

    def ret_row_vel(this):
        return this.row_vel

    def ret_col_vel(this):
        return 0

    def start(this, paddle):
        this.row1 = paddle_row-2
        this.row2 = paddle_row-2
        this.col_1 = paddle.col_start
        this.col_2 = paddle.col_start + paddle.paddle_size-1
