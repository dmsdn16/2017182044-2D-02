import gfw
from pico2d import *
from gobj import *
import title_state


def enter():
    global Manual_image
    Manual_image = gfw.image.load('res/manual.png')

def draw():
    global Manual_image
    image = Manual_image
    image.clip_draw_to_origin(0, 0, image.w, image.h, 0, 0, get_canvas_width() , get_canvas_height())

def update():
    pass

def handle_event(e):
    if (e.type,e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        gfw.change(title_state)

def exit():
    global Manual_image
    del Manual_image

def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()


     

