import gfw
from pico2d import *
import title_state


time = 1.0

def enter():
    global image, elapsed
    image = gfw.image.load('res/logo1.png')
    elapsed = 0.0

    global logo1,logo2,logo3

    logo1 = False
    logo2 = False
    logo3 = False

def update():
    
    global elapsed
    elapsed += gfw.delta_time
    print(elapsed)
    global image,logo1,logo2,logo3
    
    if logo1 == False:
        if elapsed >= time:
            gfw.image.unload('res/logo1.png')
            image = gfw.image.load('res/logo2.png')
            elapsed = 0.0
            logo1 = True

    elif logo2 == False:
        if elapsed >= time:
            gfw.image.unload('res/logo2.png')
            image = gfw.image.load('res/logo3.png')
            elapsed = 0.0
            logo2 = True

    elif logo3 == False:
         if elapsed >= time:
             gfw.image.unload('res/logo3.png')
             logo3 = True
             gfw.change(title_state)
        

def draw():
    
    image.clip_draw_to_origin(0, 0, image.w, image.h, 0, 0, get_canvas_width() , get_canvas_height())

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
