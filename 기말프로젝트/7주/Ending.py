
import gfw
from pico2d import *
import title_state


time = 1.0

def enter():
    global image, elapsed
    image = gfw.image.load('res/end1.png')
    elapsed = 0.0

    global end1,end2,end3

    end1 = False
    end2 = False
    end3 = False

def update():
    
    global elapsed
    elapsed += gfw.delta_time
    print(elapsed)
    global image,end1,end2,end3
    
    if end1 == False:
        if elapsed >= time:
            gfw.image.unload('res/end1.png')
            image = gfw.image.load('res/end2.png')
            elapsed = 0.0
            end1 = True

    elif end2 == False:
        if elapsed >= time:
            gfw.image.unload('res/end2.png')
            image = gfw.image.load('res/end3.png')
            elapsed = 0.0
            end2 = True

    elif end3 == False:
         if elapsed >= time:
             gfw.image.unload('res/end3.png')
             end3 = True
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
