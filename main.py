import os
from screen import *
from constants import *
from paddle import *
from input import *
from ball import *
from background import *
import time
from Bricks import *
from power import *
from boss import *
os.system('clear')


whole_screen = Screen(screen_ht, screen_wd)
score = Score()
lives = Lives()
Time = HTime()
brickCollapseHeader = CollapseTime()
level = Level()
paddle = Paddle()
ball = Ball(paddle.col_start)
get = Get()
background = Background()
bricks = Bricks()
bricks.generate(total_bricks)
allPowers = Powers()
boss = Boss(paddle.col_start)
bombs = Bombs()
start_time = time.time()
render_time = time.time()
collapeseTime = time.time()
pause = 0
forward = 0
currentLevel = 1
Bosslevel = 0


def initiateBossLevel():
    global whole_screen
    global score
    global lives
    global Time
    global level
    global paddle
    global ball
    global background
    global bricks
    global start_time
    global render_time
    global allPowers

    whole_screen = Screen(screen_ht, screen_wd)
    Time = HTime()
    paddle = Paddle()
    ball = Ball(paddle.col_start)
    boss = Boss(paddle.col_start)
    bombs = Bombs()
    background = Background()
    bricks = Bricks()
    bricks.generateBosslayout(whitebricks)
    allPowers = Powers()
    start_time = time.time()
    render_time = time.time()


def boss_game():
    background.show(whole_screen.screen)
    score.show(whole_screen.screen)
    lives.show(whole_screen.screen)
    Time.show(whole_screen.screen, round(time.time() - start_time))
    level.show(whole_screen.screen)
    paddle.show(whole_screen.screen, bricks, score, allPowers, level)
    boss.show(whole_screen.screen, paddle.col_start,
              ball, bricks, score, bombs)
    bombs.show(whole_screen.screen, lives, paddle, ball, score)
    ball.show(whole_screen.screen, lives, paddle,
              bricks.bricks, score,  allPowers)
    bricks.show(whole_screen.screen)
    allPowers.show(whole_screen.screen, paddle, ball)
    check_collisions()
    whole_screen.display_screen()
    print("\033[0:0H")  # reposition the cursor


def reset():
    global Time
    global brickCollapseHeader
    global ball
    global bricks
    global allPowers
    global start_time
    global render_time
    global paddle
    global background
    global whole_screen
    global collapeseTime

    #whole_screen = Screen(screen_ht, screen_wd)
    #background = Background()
    Time = HTime()
    brickCollapseHeader = CollapseTime()
    paddle = Paddle()
    ball = Ball(paddle.col_start)
    bricks = Bricks()
    bricks.generate(total_bricks)
    allPowers = Powers()
    whole_screen = Screen(screen_ht, screen_wd)
    background = Background()
    start_time = time.time()
    render_time = time.time()
    collapeseTime = time.time()
    os.system('clear')
    # for i in range(whole_screen.r):
    #    for j in range(whole_screen.c):
    #        if(whole_screen.screen[i][j] != " "):
    #            quit()


def toggle_pause(pause):
    return (1 - pause)


def levelUp(level, score):
    global Bosslevel
    if(level.value == levels):
        over(score)
    level.value += 1
    reset()
    if(level.value == 3):
        Bosslevel = 1
        initiateBossLevel()


def check_collisions():
    # side wall collisions are done

    # paddle collison with sides
    if(paddle.col_start <= game_wd[0]):
        paddle.col_start = game_wd[0]
    if((paddle.col_start + len(paddle.paddle) - 1) >= (game_wd[1] - 1)):
        paddle.col_start = game_wd[1]-len(paddle.paddle)


def display_game(iter, lives, paddle):

    global collapeseTime

    flag = 1
    for brick in bricks.bricks:
        if(brick.ret_is_broken() == 0 and brick.ret_type() > 0):
            flag = 0
    if(flag == 1):
        levelUp(level, score)
        return
    background.show(whole_screen.screen)
    score.show(whole_screen.screen)
    lives.show(whole_screen.screen)
    Time.show(whole_screen.screen, round(time.time() - start_time))
    brickCollapseHeader.show(
        whole_screen.screen, timeToCollapse - round(time.time() - collapeseTime))
    level.show(whole_screen.screen)
    paddle.show(whole_screen.screen, bricks, score, allPowers, level)
    ball.show(whole_screen.screen, lives, paddle,
              bricks.bricks, score,  allPowers)
    if(time.time() - collapeseTime >= timeToCollapse):
        bricks.moveDown(whole_screen.screen, score)
        collapeseTime = time.time()
    bricks.show(whole_screen.screen)
    allPowers.show(whole_screen.screen, paddle, ball)
    check_collisions()
    whole_screen.display_screen()
    print("\033[0:0H")  # reposition the cursor


def handle_input(pause, forward):
    ch = input_to(get, frametransition)

    if(ch == 'd'):
        paddle.clear(whole_screen.screen)
        paddle.col_start += 2
        check_collisions()
        if(ball.ret_is_started() == 0):
            ball.clear(whole_screen.screen)
            ball.upd_col(ball.ret_col() + 2)
        else:
            if(ball.grabed == 1):
                ball.clear(whole_screen.screen)
                ball.upd_col(ball.ret_col() + 2)
    if(ch == 'a'):
        paddle.clear(whole_screen.screen)
        paddle.col_start -= 2
        check_collisions()
        if(ball.ret_is_started() == 0):
            ball.clear(whole_screen.screen)
            ball.upd_col(ball.ret_col() - 2)
        else:
            if(ball.grabed == 1):
                ball.clear(whole_screen.screen)
                ball.upd_col(ball.ret_col() - 2)
    if(ch == 'p'):
        return(toggle_pause(pause), forward)
    if(ch == 'f'):
        return (0, 1)
    if(ch == " "):
        if(ball.ret_is_started() == 0):
            ball.start()
        else:
            if(ball.grabed == 1):
                ball.resume(paddle)
    if(ch == 'i'):
        levelUp(level, score)
    if(ch == 'q'):
        over(score)
    return pause, forward


iter = 0
while(True):
    iter += 1
    pause, forward = handle_input(pause, forward)
    if(forward == 1):
        forward = 0
        pause = 1
    while(pause):
        pause, forward = handle_input(pause, forward)
    if(time.time() - render_time >= frametransition):
        if(Bosslevel):
            boss_game()
        else:
            display_game(iter, lives, paddle)
        render_time = time.time()
    # time.sleep(0.1)
    # if(ball.is_started == 0):
    #     ball.start()
