import pgzrun
import itertools
import random
#screen
WIDTH = 600
HEIGHT = 600
TITLE = "Ship animation"
coordinates = [(50,50),(550,50),(550,550),(50,550)]
postions = itertools.cycle(coordinates)

#actors
ship = Actor("ship 2")
block = Actor("block")
ship.pos = 300,300
block.pos = 50,50

#draw
def draw():
    screen.blit("space",(0,0))
    ship.draw()
    block.draw()

#block animaiton
def block_animation():
    animate(block,"bounce_end",duration = 1,pos = next(postions))
clock.schedule_interval(block_animation,2)

#ship target
def ship_target():
    x = random.randint(100,500)
    y = random.randint(100,500)
    ship.target = (x,y)
    target_angle = ship.angle_to(ship.target)
    animate(ship,angle = target_angle,duration = 0.5,on_finished = ship_animation)
#ship animation
def ship_animation():
    animate(ship,duration = 1,pos = ship.target,tween = "accel_decel",on_finished = ship_target)

ship_target()




pgzrun.go()

