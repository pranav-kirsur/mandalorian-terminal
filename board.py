import numpy as np
from colorama import Fore, Back, Style
from mandalorian import Mandalorian


class Board:
    ''' Creates grid for the game '''

    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__grid = self.__create_grid(rows, cols)
        self.__score = 0

    def __create_grid(self, rows, cols):
        return np.full((rows, cols), Back.BLUE + " ")

    def getrows(self):
        return self.__rows

    def getcols(self):
        return self.__cols

    def getscore(self):
        return self.__score

    def refresh_grid(self):
        self.__grid = self.__create_grid(self.__rows, self.__cols)

    def print_grid(self):
        ''' 
            Prints the board
        '''
        for row in self.__grid:
            print("".join(row))

    def render(self, lives, time_left):
        ''' Renders the information panel, top, grid, and ground and prints it onto the screen'''
        self.__reposition_cursor(0, 0)
        print("Score: " + str(self.__score) + "\tLives: " +
              str(lives) + "\tTime left: " + str(time_left))
        print(Back.YELLOW + (" " * self.__cols))
        self.print_grid()
        print(Back.GREEN + (" " * self.__cols) + Style.RESET_ALL)
        print(Style.RESET_ALL, end='')

    def render_object(self, game_object):
        ''' Renders the object onto the grid'''
        x = round(game_object.getx())
        y = round(game_object.gety())
        self.__grid[x: x + game_object.getheight(),
                    y:y + game_object.getwidth()] = game_object.getshape()

    def __reposition_cursor(self, x, y):
        print("\033[%d;%dH" % (x, y), end='')

    def is_touching_ground(self, game_object):
        return round(game_object.getx()) + game_object.getheight() >= self.__rows

    def is_touching_left_edge(self, game_object):
        return round(game_object.gety()) <= 0

    def is_touching_top(self, game_object):
        return round(game_object.getx()) <= 0

    def is_touching_right_edge(self, game_object):
        return round(game_object.gety()) + game_object.getwidth() >= self.__cols

    def render_wave_from_edge_till_coords(self, x, y, phase, height):
        x = int(round(x))
        y = int(round(y))
        for ycoord in range(y):
            xcoord = int(round(x + height/2*np.sin((ycoord * 50) + phase)))
            if xcoord >= 0 and xcoord < self.__rows and ycoord >= 0 and ycoord < self.__cols:
                self.__grid[xcoord, ycoord] = Back.WHITE + " "

    def compute_physics(self, game_object):

        game_object.setvx(game_object.getvx() + game_object.getax() + game_object.getgravity() -
                          (game_object.getdrag() * game_object.getvx() * game_object.getvx() * (1 if game_object.getvx() > 0 else -1)))
        game_object.setvy(game_object.getvy() + game_object.getay() -
                          (game_object.getdrag() * game_object.getvy() * game_object.getvy() * (1 if game_object.getvy() > 0 else -1)))
        game_object.setx(game_object.getx() + game_object.getvx())
        game_object.sety(game_object.gety() + game_object.getvy())

        if(self.is_touching_ground(game_object)):
            game_object.hit_ground(self.__rows)

        if(self.is_touching_top(game_object)):
            game_object.hit_top()

        if(self.is_touching_left_edge(game_object)):
            game_object.hit_left_edge()

        if(self.is_touching_right_edge(game_object)):
            game_object.hit_right_edge(self.__cols)

    def compute_coin_collisions(self, mandalorian, coins_list):
        for coin in coins_list:
            if coin.is_active():
                if (coin.getx() >= mandalorian.getx()) and (coin.gety() >= mandalorian.gety()) and (coin.getx() < mandalorian.getx() + mandalorian.getheight()) and (coin.gety() < mandalorian.gety() + mandalorian.getwidth()):
                    # collision has occurred
                    coin.collect()
                    mandalorian.collect_coin()
                    self.__score += 10

    def compute_laser_collision(self, mandalorian, laser, is_dragon_active):
        laser_squares = []
        if(laser.gettype() == 1):
            for i in range(5):
                laser_squares.append((laser.getx(), laser.gety() + i))
        elif(laser.gettype() == 2):
            for i in range(5):
                laser_squares.append((laser.getx() + i, laser.gety()))
        elif(laser.gettype() == 3):
            for i in range(5):
                laser_squares.append((laser.getx() + i, laser.gety() + i))
        elif(laser.gettype() == 4):
            for i in range(5):
                laser_squares.append((laser.getx() + 4 - i, laser.gety() + i))

        has_collision_occured = False

        for sqaure in laser_squares:
            if (sqaure[0] >= mandalorian.getx()) and (sqaure[1] >= mandalorian.gety()) and (sqaure[0] < mandalorian.getx() + mandalorian.getheight()) and (sqaure[1] < mandalorian.gety() + mandalorian.getwidth()):
                has_collision_occured = True

        should_dragon_be_destroyed = False
        if has_collision_occured:
            if not mandalorian.get_shield_state() :
                if not is_dragon_active:
                    mandalorian.loselife()
                else:
                    #dragon should be destoyed
                    should_dragon_be_destroyed = True
            laser.set_activity(False)
        return should_dragon_be_destroyed

    def compute_projectile_collision(self, bullet, object):
        bullet_squares = [(bullet.getx(), bullet.gety() + i)
                          for i in range(bullet.getwidth())]

        has_collision_occured = False

        for sqaure in bullet_squares:
            if (sqaure[0] >= object.getx()) and (sqaure[1] >= object.gety()) and (sqaure[0] < object.getx() + object.getheight()) and (sqaure[1] < object.gety() + object.getwidth()):
                has_collision_occured = True

        return has_collision_occured

    def compute_speed_boost_collision(self, mandalorian, speed_boost):
        return (speed_boost.getx() >= mandalorian.getx()) and (speed_boost.gety() >= mandalorian.gety()) and (speed_boost.getx() < mandalorian.getx() + mandalorian.getheight()) and (speed_boost.gety() < mandalorian.gety() + mandalorian.getwidth())

    def increase_score(self, increment):
        self.__score += increment
