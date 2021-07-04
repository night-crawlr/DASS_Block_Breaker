import random
from constants import *


class Boss:
    def __init__(this, paddle_col):
        this.boss = ["        _,--=--._        ",
                     "      ,'...._....`.      ",
                     "     -...._(_)_o...-     ",
                     "____'..../_  _/]....`____",
                     " (+):::::::::::::::::(+) ",
                     "  (+).#############.(+)  ",
                     "      .,..........'      ",
                     "        ` -= - -'        "]
        this.row = game_ht[0]+4
        this.col = paddle_col
        this.col_vel = -2
        this.size = 25
        this.health = 100
        this.shield1 = 0
        this.shield2 = 0
        this.lastBombTime = 0

    def collision_ball(this, ball, bricks, score):
        for i in range(len(this.boss)):
            for j in range(this.size):
                if(this.boss[i][j] == ' '):
                    continue
                if ((ball.ret_row() == this.row + i) and (ball.ret_col() == this.col + j)):
                    ball.upd_row_vel(- ball.ret_row_vel())
                    ball.upd_col_vel(- ball.ret_col_vel())
                    this.health -= decreseBy
                    if(this.health <= 0):
                        score.value += 100
                        over(score)
                    if(this.health <= layout1at and this.shield1 == 0):
                        this.shield1 = 1
                        bricks.shieldLayout()
                    if(this.health <= layout2at and this.shield2 == 0):
                        this.shield2 = 1
                        bricks.shieldLayout(2)
                    break

    def move(this, paddle_col, ball, bricks, score, bombs):
        if(time.time() - this.lastBombTime >= nextBombDuration):
            bombs.genrate_bomb(this)
            this.lastBombTime = time.time()
        ball_row_vel = ball.ret_row_vel()
        # if you require special
        # if(ball_row_vel >= 0):
        this.col = paddle_col
        # else:
        #     this.col += this.col_vel
# else
        if(this.col + this.size >= game_wd[1]):
            rem = this.col + this.size - game_wd[1]
            this.col -= rem
            this.col_vel = -this.col_vel
        if(this.col <= game_wd[0]):
            this.col = game_wd[0]
            this.col_vel = -this.col_vel

        this.collision_ball(ball, bricks, score)

    def clear(this, screen):
        for i in range(len(this.boss)):
            for j in range(this.size):
                screen[this.row+i][this.col+j] = ' '

    def show(this, screen, paddle_col, ball, bricks, score, bombs):
        this.clear(screen)
        this.move(paddle_col, ball, bricks, score, bombs)
        for i in range(len(this.boss)):
            for j in range(this.size):
                screen[this.row+i][this.col+j] = this.boss[i][j]

        # showing health bar
        per = this.health
        status = (per/100) * game_wd[1]-game_wd[0]
        status = int(status)
        for j in range(game_wd[1]-game_wd[0]):
            screen[game_ht[0]][game_wd[0]+j] = ' '
        for j in range(status):
            screen[game_ht[0]][game_wd[0]+j] = 'g'
        if(this.health <= 20):
            score.value += 100
            over(score)


class Bombs:
    def __init__(this):
        this.bombs = []

    def genrate_bomb(this, Boss):
        bomb = Bomb(Boss)
        this.bombs.append(bomb)

    def clear(this, screen):
        for bomb in this.bombs:
            screen[bomb.row][bomb.col] = ' '

    def remove(this, i):
        this.bombs.pop(i)

    def move(this, lives, paddle, ball, score, screen):
        this.clear(screen)
        for i, bomb in enumerate(this.bombs):
            bomb.row += bomb.row_vel
            if(bomb.row >= paddle.row):
                bomb.row = paddle.row
                if(paddle.col_start <= bomb.col and bomb.col <= paddle.col_start + paddle.paddle_size - 1):
                    ball.handle_life_dec(screen, lives, paddle, score)
                else:
                    this.remove(i)

    def show(this, screen, lives, paddle, ball, score):
        this.move(lives, paddle, ball, score, screen)
        for bomb in this.bombs:
            screen[bomb.row][bomb.col] = bomb.char


class Bomb:
    def __init__(this, Boss):
        this.row = Boss.row + len(Boss.boss)
        this.col = Boss.col + (Boss.size//2)
        this.row_vel = bombVel
        this.char = 'Y'
