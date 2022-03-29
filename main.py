import sys
import pygame
import pymunk
import pymunk.pygame_util
import random


def main():
    pygame.init()
    screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
    pygame.display.set_caption("Flappy bird")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, 900.0)
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    Hero =   MakeActors(space)
    CanJump= True
    ct = 0
    IsJumping = False
    JumpVal = 300
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and CanJump and Hero.body.position.y > 100:
                Jump(Hero,10)
















        screen.fill((255,255,255))

        space.debug_draw(draw_options)
        space.step(1/50.0)

        pygame.display.flip()
        clock.tick(50)


def MakeActors(space):

    #add_static_L(space)
    return MakeHero(space)

def add_static_L(space):
    body = pymunk.Body(body_type = pymunk.Body.STATIC) # 1
    body.position = (0, 500)
    line = pymunk.Segment(body, (0, 0), (300, 0), 5) # 2

    line.friction = 1 # 3


    space.add(body,line) # 4


def MakeHero(space):
    mass = 30
    radius = 25
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
    body = pymunk.Body(mass, inertia)
    x = random.randint(115, 350)
    body.position = x, 200
    shape = pymunk.Circle(body, radius, (0, 0))
    shape.elasticity = 0.95
    shape.friction = 0.9
    space.add(body, shape)
    return shape
def Jump(hero,val):

    mass = 30
    acceleration = 400

    hero.body.apply_impulse_at_local_point(((0, -1 *( mass *hero.body.velocity.y))),(0,0))
    hero.body.apply_impulse_at_local_point(((0, -1 * (mass *acceleration))), (0, 0))






if __name__ == '__main__':
    sys.exit(main())