import random
import sys
import pygame
import pymunk
import pymunk.pygame_util
import random

class PipePair:
    FullLength = 1000
    width = 150
    GroundLevel = 1000
    Gap = 200
    HeightUp =-1
    HeightDown = -1


    def __init__(self, x, space):
        self.x = x
        self.space = space
        self.MakePipes()

    def MakePipes(self):
        H = random.randint(300, self.FullLength - 500)

        self.HeightUp = H

        x =self.create_rectangle(self.space, self.x, 0, self.width, H)
        y =self.create_rectangle(self.space, self.x, H + self.Gap, self.width, self.FullLength - (H + self.Gap))

        self.HeightDown = self.FullLength - (H + self.Gap)

        self.up = x
        self.down =y

    def create_rectangle(self, space, pos_x, pos_y, width, height):
        body = pymunk.Body(1,2)

        body.position = (pos_x, pos_y)
        shape = pymunk.Poly.create_box(body, (width, height))

        space.add(body, shape)
        return shape
