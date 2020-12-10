
import gfw
from pico2d import *
import final



def enter():
    global a
    a = False
   

def update():
    global a

    if a:
        print(00000000)
        gfw.change(final)

    if not a:
        a = True
   
def draw():
    pass

def handle_event(e):
    pass

def exit():
    for n in gfw.world.all_objects():
        gfw.world.remove(n)

def pause():
    pass

def resume():
    pass
    
if __name__ == '__main__':
     gfw.run_main()

