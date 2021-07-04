from constants import *
import random
import json


class Ball:
    def __init__(this, paddle_left_colom):
        this.__row = ball_row
        this.__colum = paddle_left_colom + random.randint(0, 13)
        this.__ball = 'O'
        this.__col_vel = 0  # colum per 0.1sec
        this.__row_vel = 0  # row per 0.1sec
        this.__is_started = 0
        this.power = [0, 0]  # can be 1 and 2
        this.power_timer = 0
        this.before = 'P'
        this.after = 'A'
        this.stored_row_vel = 0
        this.stored_col_vel = 0
        this.grabed = 0

    def ret_row(this):
        return this.__row

    def upd_row(this, x):
        this.__row = x

    def ret_col(this):
        return this.__colum

    def upd_col(this, x):
        this.__colum = x

    def ret_ball(this):
        return this.__ball

    def upd_ball(this, x):
        this.__ball = x

    def ret_row_vel(this):
        return this.__row_vel

    def upd_row_vel(this, x):
        this.__row_vel = x

    def ret_col_vel(this):
        return this.__col_vel

    def upd_col_vel(this, x):
        this.__col_vel = x

    def ret_is_started(this):
        return this.__is_started

    def upd_is_started(this, x):
        this.__is_started = x

    def reset(this, paddle_left_colom):
        this.upd_row(ball_row)
        this.upd_col(paddle_left_colom + random.randint(0, 13))
        this.upd_col_vel(0)
        this.upd_row_vel(0)
        this.upd_is_started(0)
        this.power_timer = 0
        this.power = [0, 0]

    def clear(this, screen):
        screen[this.ret_row()][this.ret_col()] = ' '
        # for tracing while debugging
        # screen[this.ret_row() - this.ret_row_vel()][this.ret_col() -
        #                                             this.ret_col_vel()] = ' '
        # screen[this.ret_row() + this.ret_row_vel()][this.ret_col() +
        #                                             this.ret_col_vel()] = ' '

    def inc_speed(this, x):
        if(this.ret_row_vel() >= 0):
            this.upd_row_vel(this.ret_row_vel() + x)
        if(this.ret_row_vel() < 0):
            this.upd_row_vel(this.ret_row_vel() - x)
        if(this.ret_col_vel() >= 0):
            this.upd_col_vel(this.ret_col_vel() + x)
        if(this.ret_col_vel() < 0):
            this.upd_col_vel(this.ret_col_vel() - x)

    def show(this, screen, lives, paddle, bricks, score, allPowers):
        if(this.power != [0, 0] and (time.time() - this.power_timer >= timer_time)):
            if(this.power[0] == 1):
                this.inc_speed(-1)
                this.power[0] = 0
            if(this.power[1] == 1):
                this.power[1] = 0

        this.move(screen, lives, paddle, bricks, score, allPowers)
        screen[this.ret_row()][this.ret_col()] = this.ret_ball()
        # for tracing while debugging
        # screen[this.ret_row() - this.ret_row_vel()][this.ret_col() -
        #                                             this.ret_col_vel()] = this.before
        # screen[this.ret_row() + this.ret_row_vel()][this.ret_col() +
        #                                             this.ret_col_vel()] = this.after

    def start(this):
        this.upd_is_started(1)
        this.upd_col_vel(random.choice([-1, 1]))
        # this.upd_row_vel(random.choice([-2, 2]))
        this.upd_row_vel(-2)

    def resume(this, paddle):
        this.upd_row_vel(this.stored_row_vel-1)
        this.upd_col_vel(this.stored_col_vel-1)
        this.grabed = 0
        paddle.power = 0

    def move(this, screen, lives, paddle, bricks, score,  allPowers):
        this.clear(screen)
        this.upd_row(this.ret_row() + this.ret_row_vel())
        this.upd_col(this.ret_col() + this.ret_col_vel())
        this.handle_collisions(screen, lives, paddle, bricks, score, allPowers)

    def handle_life_dec(this, screen, lives, paddle, score):
        screen[this.ret_row()][this.ret_col()] = ' '
        if(lives.value == 1):
            over(score)
        lives.dec_life()
        paddle.reset(screen)
        this.reset(paddle.col_start)

    def predict_path(this):
        # convention is going horizontal first and then vertical
        tobereturned = []
        past_row = this.ret_row() - this.ret_row_vel()
        past_col = this.ret_col() - this.ret_col_vel()
        if(this.ret_row_vel() > 0):
            for i in range(this.ret_row_vel() + 1):
                tobereturned.append([past_row+i, past_col])
        elif(this.ret_row_vel() < 0):
            for i in range(-(this.ret_row_vel()) + 1):
                tobereturned.append([past_row-i, past_col])
        if(this.ret_col_vel() >= 0):
            for i in range(1, this.ret_col_vel() + 1):
                tobereturned.append([past_row+this.ret_row_vel(), past_col+i])
        elif(this.ret_col_vel() < 0):
            for i in range(1, -(this.ret_col_vel()) + 1):
                tobereturned.append([past_row+this.ret_row_vel(), past_col-i])

        return tobereturned

    def handle_collisions(this, screen, lives, paddle, bricks, score, allPowers):
        # with up wall
        if(this.ret_row() <= game_ht[0]):
            this.upd_row(game_ht[0])
            this.upd_row_vel(-(this.ret_row_vel()))
            os.system("aplay -q ./sounds/laser.wav &")
        # with right wall
        if(this.ret_col() >= (game_wd[1]-1)):
            this.upd_col(game_wd[1]-1)
            this.upd_col_vel(-(this.ret_col_vel()))
            os.system("aplay -q ./sounds/laser.wav &")
        # with left wall
        if(this.ret_col() <= game_wd[0]):
            this.upd_col(game_wd[0])
            this.upd_col_vel(-(this.ret_col_vel()))
            os.system("aplay -q ./sounds/laser.wav &")
        # with down wall
        # if(this.row >= (game_ht[1]-1)):
        #     this.row = game_ht[1]-1
        #     this.row_vel = -(this.row_vel)
        if(this.ret_is_started() != 0):
            if(this.ret_row() >= (game_ht[1]-1)):
                this.upd_row(game_ht[1]-1)
                this.handle_life_dec(screen, lives, paddle, score)

        # paddle collision with ball
        if(paddle.power != 3):
            if(this.ret_is_started() != 0):
                for j in range(len(paddle.paddle)):
                    if((this.ret_row() >= (ball_row)) and (this.ret_col() == (paddle.col_start+j))):
                        os.system("aplay -q ./sounds/laser.wav &")
                        this.upd_row(ball_row)
                        this.upd_col_vel(this.ret_col_vel() + paddle.vels[j])
                        this.upd_row_vel(- (this.ret_row_vel()))
        else:
            if(this.grabed == 0):
                for j in range(len(paddle.paddle)):
                    if((this.ret_row() >= (ball_row)) and (this.ret_col() == (paddle.col_start+j))):
                        os.system("aplay -q ./sounds/laser.wav &")
                        this.upd_row(ball_row)
                        this.upd_col_vel(this.ret_col_vel() + paddle.vels[j])
                        this.upd_row_vel(- (this.ret_row_vel()))
                        this.stored_row_vel = 1+this.ret_row_vel()
                        this.stored_col_vel = 1+this.ret_col_vel()
                        this.upd_row_vel(0)
                        this.upd_col_vel(0)
                        this.grabed = 1

        # collsions with bricks
        flag_collision = 0
        ball_moment_array = this.predict_path()
        for brick in bricks:
            if(brick.ret_is_broken()):
                continue
            brick_array = []
            for i in range(7):
                brick_array.append([brick.ret_row(), brick.ret_col()+i])
            # for i in range(9):
            #     for j in range(3):
            #         brick_array.append(
            #             [brick.ret_row()-1+j, brick.ret_col()-1+i])
            for i, a in enumerate(ball_moment_array):
                for j, b in enumerate(brick_array):
                    if(flag_collision == 1):
                        continue
                    if(a == b):
                        if(this.power[1] == 0):
                            os.system("aplay -q ./sounds/laser.wav &")
                            brick.on_collide(this, score, allPowers)
                            if(ball_moment_array[i-1][0] == b[0]):  # rows are equal
                                this.upd_row(ball_moment_array[i-1][0])
                                this.upd_col(ball_moment_array[i-1][1])
                                this.upd_col_vel(- (this.ret_col_vel()))
                            if(ball_moment_array[i-1][1] == b[1]):  # cols are equal
                                this.upd_row(ball_moment_array[i-1][0])
                                this.upd_col(ball_moment_array[i-1][1])
                                this.upd_row_vel(- (this.ret_row_vel()))

                            this.upd_row(this.ret_row() + this.ret_row_vel())
                            this.upd_col(this.ret_col() + this.ret_col_vel())
                        else:
                            os.system("aplay -q ./sounds/laser.wav & &")
                            brick.on_super_collide(this, score, allPowers)
                        flag_collision = 1

    def speedup(this):
        this.inc_speed(1)
        this.power[0] = 1
        this.power_timer = time.time()

    def superball(this):
        this.power[1] = 1
        this.power_timer = time.time()
