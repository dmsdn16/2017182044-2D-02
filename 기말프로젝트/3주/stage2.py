import gfw
from pico2d import *
from Map import *

time = 1.0

def enter():
    global image, elapsed
    image = gfw.image.load('../res/clear.png')
    elapsed = 0.0

    global clear,map

    clear = False
   
    map = Map()

def update():
    
    global elapsed, clear , image
    elapsed += gfw.delta_time
    
    
    if clear == False:
        if elapsed >= time:
            gfw.image.unload('../res/clear.png')
            
            clear = True

    
            

def draw():
    
    global clear
    image.clip_draw_to_origin(0, 0, image.w, image.h, 0, 0, get_canvas_width() , get_canvas_height())

    if clear == True:
        map.draw()
def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
def exit():
    global image
    del image

def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
     gfw.run_main()
