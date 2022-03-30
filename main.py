import sys
import pygame
import pymunk
import pymunk.pygame_util
import random
from Pipe import PipePair
heroImg = pygame.image.load('sprites/redbird-upflap.png')
#heroImg = pygame.transform.scale(heroImg,(500,500))
pipeImg = pygame.image.load('sprites/pipe-green.png')
Game = True
pipepairs = []





def main():
    score = 0
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Flappy bird")
    clock = pygame.time.Clock()
    gamespeed = 15
    space = pymunk.Space()
    space.gravity = (0.0, 900.0)
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    Hero = MakeActors(space)

    bg = pygame.image.load("sprites/bg.png")



    handler = space.add_default_collision_handler()
    handler.begin = coli_begin

    GenerateCustomPipes(Hero.body.position.x+3000,space)
    GenerateCustomPipes(Hero.body.position.x +4500, space)





    while Game:
        screen.fill((0, 0, 0))

        score += 1

        LastGeneratedPipeX = pipepairs[-1].up.body.position.x
        if Hero.body.position.y > 850:
            break
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit(0)

            pymunk.collision_handler
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and Hero.body.position.y > 100:
                Jump(Hero, 10)

        for i,pipe in enumerate(pipepairs):


            pipe.up.body.position += pymunk.Vec2d(-gamespeed, 0)
            pipe.down.body.position += pymunk.Vec2d(-gamespeed, 0)

            Imgx = pygame.transform.scale(pipeImg, (pipe.width + 30, pipe.HeightDown*2))
            screen.blit(Imgx, (pipe.down.body.position.x - 70, pipe.up.body.position.y  + pipe.HeightUp))



            Img = pygame.transform.scale(pipeImg, (pipe.width+30,pipe.HeightUp/2))
            Img = pygame.transform.rotozoom(Img, 180, 1)
            screen.blit(Img, (pipe.up.body.position.x-70 , pipe.up.body.position.y ))
            myfont = pygame.font.SysFont('Comic Sans MS', 30)
            textsurface = myfont.render("Score:" + str(score), False, (255, 255, 255))
            screen.blit(textsurface,(500,0))
            Img = pygame.transform.scale(pipeImg, (pipe.width + 30, 20 + pipe.HeightDown / 2))

            if pipe.up.body.position.x < -100:
                space.remove(pipe.up)
                space.remove(pipe.down)
                pipepairs.pop(i)
                GeneratePipes(LastGeneratedPipeX + 500, space)



        screen.blit(heroImg, (Hero.body.position.x - Hero.radius - 10, Hero.body.position.y - Hero.radius))
        space.step(1 / 60.0)

        pygame.display.flip()
        clock.tick(60)


def GenerateCustomPipes(x,screen):
    pipes = PipePair(x, screen)
    pipes.up.body.velocity_func = pipes.down.body.velocity_func = zero_gravity
    pipepairs.append(pipes)
def GeneratePipes(xHero,screen):
    xHero = int(xHero)
    MaxX = xHero + 1000
    pipes = PipePair(random.randint(xHero,MaxX),screen)
    pipes.up.body.velocity_func = pipes.down.body.velocity_func = zero_gravity
    pipepairs.append(pipes)


def coli_begin(arbiter, space, data):
    global Game
    print(data)
    Game = False
    return True

def zero_gravity(body, gravity, damping, dt):
    pymunk.Body.update_velocity(body, (0,0), damping, dt)


def background(SCREEN,BG,x_pos_bg,y_pos_bg,game_speed):
    SCREEN.blits(BG, 0, 0)






def GameOver():
    print("hello")


def MakeActors(space):
    # add_static_L(space)
    return MakeHero(space)


def add_static_L(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)  # 1
    body.position = (0, 500)
    line = pymunk.Segment(body, (0, 0), (300, 0), 5)  # 2

    line.friction = 1  # 3

    space.add(body, line)  # 4


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


def Jump(hero, val):
    mass = 30
    acceleration = 400

    hero.body.apply_impulse_at_local_point(((0, -1 * (mass * hero.body.velocity.y))), (0, 0))
    hero.body.apply_impulse_at_local_point(((0, -1 * (mass * acceleration))), (0, 0))


def PushRight(hero):
    hero.body.apply_impulse_at_local_point(((200, 0)), (0, 0))


if __name__ == '__main__':
    sys.exit(main())
