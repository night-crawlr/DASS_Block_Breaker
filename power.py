
import random
from constants import *
powerups = ["EP", "SP", "BM", "FB", "TB", "PG"]


class Powers:
    def __init__(this):
        this.powers = []

    # def generate_powerup(this, ball, r, c):
    #     selcted_power = random.choice(
    #         [EP(r, c), SP(r, c), FB(r, c), TB(r, c), PG(r, c)])
    #     #selcted_power = random.choice([PG(r, c)])
    #     this.powers.append(selcted_power)

    def generate_powerup(this, ball, r, c):
        selcted_power = random.choice(
            [EP(r, c), SP(r, c), FB(r, c), TB(r, c), PG(r, c)])
        #selcted_power = random.choice([SH(r, c)])
        selcted_power.row_vel = ball.ret_row_vel()
        selcted_power.col_vel = ball.ret_col_vel()
        # print(ball.ret_row_vel())
        # print(ball.ret_col_vel())
        # quit()
        selcted_power.prev_col = selcted_power.col
        selcted_power.prev_row = selcted_power.row
        this.powers.append(selcted_power)

    def remove(this, i):
        this.powers.pop(i)

    def collison_paddle(this, power, paddle, ball):
        flag = 0
        if(power.row >= paddle_row):
            for i in range(len(paddle.paddle)):
                if(power.col == paddle.col_start + i):
                    flag = 1
                    if(power.type == "EP"):
                        paddle.expand()
                    if(power.type == "SP"):
                        paddle.contract()
                    if(power.type == "FB"):
                        ball.speedup()
                    if(power.type == "TB"):
                        ball.superball()
                    if(power.type == "PG"):
                        paddle.grab()
                    if(power.type == "SH"):
                        paddle.shoot()
        return flag

    # def show(this, screen, paddle, ball):

    #     for i, power in enumerate(this.powers):
    #         screen[power.prev_row][power.prev_col] = ' '
    #         screen[power.prev_row][power.prev_col+1] = ' '
    #         if(this.collison_paddle(power, paddle, ball)):
    #             this.remove(i)
    #             continue
    #         if(power.row >= game_ht[1]):
    #             this.remove(i)
    #             continue
    #         screen[power.row][power.col] = power.type[0]
    #         screen[power.row][power.col+1] = power.type[1]
    #         power.prev_row = power.row
    #         power.prev_col = power.col
    #         power.row += power.row_vel

    def show(this, screen, paddle, ball):

        for i, power in enumerate(this.powers):
            screen[power.prev_row][power.prev_col] = ' '
            screen[power.prev_row][power.prev_col+1] = ' '
            if(this.collison_paddle(power, paddle, ball)):
                this.remove(i)
                continue
            if(power.row >= game_ht[1]):
                this.remove(i)
                continue
            screen[power.row][power.col] = power.type[0]
            screen[power.row][power.col+1] = power.type[1]
            power.prev_row = power.row
            power.prev_col = power.col
            #power.row += power.row_vel
            # updating the positions of the power up by kinematics
            power.row = power.prev_row + power.row_vel
            power.col = power.prev_col + power.col_vel
            if(power.col >= game_wd[1]-2):
                power.col = game_wd[1]-2
                power.col_vel = - power.col_vel
            if(power.col <= game_wd[0]):
                power.col = game_wd[0]
                power.col_vel = -power.col_vel
            if(power.row <= game_ht[0]):
                power.row = game_ht[0]
                power.row_vel = - power.row_vel
            power.col_vel = power.col_vel
            if(power.row_rem == int(1/gravity)):
                power.row_vel = power.row_vel + 1
                power.row_rem = 0
            else:
                power.row_rem += 1


class Power:
    def __init__(this):
        this.row = 0
        this.prev_row = 0
        this.col = 0
        this.prev_col = 0
        this.type = 0
        this.row_vel = 1
        this.col_vel = 1
        this.row_rem = 1


class EP(Power):
    def __init__(this, r, c):
        Power.__init__(this)
        this.row = r
        this.col = c
        this.type = "EP"


class SP(Power):
    def __init__(this, r, c):
        Power.__init__(this)
        this.row = r
        this.col = c
        this.type = "SP"


class FB(Power):
    def __init__(this, r, c):
        Power.__init__(this)
        this.row = r
        this.col = c
        this.type = "FB"


class TB(Power):
    def __init__(this, r, c):
        Power.__init__(this)
        this.row = r
        this.col = c
        this.type = "TB"


class PG(Power):
    def __init__(this, r, c):
        Power.__init__(this)
        this.row = r
        this.col = c
        this.type = "PG"


class SH(Power):
    def __init__(this, r, c):
        Power.__init__(this)
        this.row = r
        this.col = c
        this.type = "SH"
