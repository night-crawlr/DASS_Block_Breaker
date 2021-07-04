from constants import *


class Background:
    def __init__(this):
        this.rows = game_ht
        this.cols = game_wd

    def show(this, screen):
        for i in range(this.rows[0], this.rows[1]):
            for j in range(this.cols[0], this.cols[1]):
                if(i == this.rows[0] or i == (this.rows[1]-1)):
                    screen[i][j] = '_'
                if((j == this.cols[0] or j == (this.cols[1]-1))):
                    screen[i][j] = '|'
                    if(i == this.rows[0]):
                        screen[i][j] = ' '
