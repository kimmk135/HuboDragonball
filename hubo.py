from cs1robots import *
from alarm import *

world, scene = load_world('worlds/world.wld')

def p():
    t = alarm_get()
    print("tick:", t)
    if t == 0:
        world.remove_beeper(6, 4)

        world.add_beeper(4, 4)
        world.add_beeper(4, 4)
        world.add_beeper(4, 4)
        world.add_beeper(5, 4)
        world.add_beeper(5, 4)
        world.add_beeper(6, 4)
    elif t == 1:
        world.remove_beeper(4, 4)
        world.remove_beeper(4, 4)
        world.remove_beeper(4, 4)
    elif t == 2:
        world.remove_beeper(5, 4)
        world.remove_beeper(5, 4)
        
    world.add_beeper(1, 4)
    world.add_beeper(9, 4)

    world.update_layer()
    scene.refresh()


alarm_start(p)

hubo1 = Robot(avenue=2, street=2)
hubo2 = Robot(avenue=8, street=2, orientation="W")

while True:
    pass

alarm_end()