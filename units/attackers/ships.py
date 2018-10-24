import pygame as pg
from .shared import Attacker
from .shared import Unit
from assets import Images
from settings import *

class ScoutShip(Attacker, pg.sprite.Sprite):
    name = "Scout"
    src_img = Images.scout_ship_img
    price = 10
    income = 3
    speed = 1.3
    hp = 15
    hit_box_dim = TILE_SIZE // 4


class RedShip(Attacker):
    name = "R.E.D"
    src_img = Images.red_ship_img
    price = 15
    income = 7
    speed = 0.8
    hp = 30
    hit_box_dim = TILE_SIZE // 3



class FleeShip(Attacker):
    name = "Flee"
    src_img = Images.flee_ship_img
    price = 20
    income = 5
    speed = 1.2
    hp = 15
    hit_box_dim = TILE_SIZE // 6



class CargoShip(Attacker):
    name = "Cargo"
    src_img = Images.cargo_ship_img
    price = 50
    income = 25
    speed = 0.5
    hp = 50
    hit_box_dim = TILE_SIZE//2
