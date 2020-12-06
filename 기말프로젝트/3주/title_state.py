import gfw
from pico2d import *
import game_state
import manual
import stage2

def enter():
    global image, count
    image = []
    for n in range(1, 4):
        image.append(gfw.image.load_image('../res/Menu%d.png' % n))
    count = 0

def update():
    pass

def draw():
    global image, count
    image[count].clip_draw_to_origin(0,0, 1920, 1080, 0, 0, get_canvas_width(), get_canvas_height())

     #image.clip_draw_to_origin(0, 0, image.w, image.h, 0, 0, get_canvas_width() , get_canvas_height())

def handle_event(e):
    global count

    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        if count == 0:
            
           gfw.push(game_state)

        elif count == 1:
            gfw.push(manual)
        elif count == 2:
            gfw.quit()
        
    elif(e.type, e.key) == (SDL_KEYDOWN, SDLK_DOWN):
        if count != 2:
            count += 1
        elif count == 2:
            count = 0
    elif(e.type, e.key) == (SDL_KEYDOWN, SDLK_UP):
        if count == 0:
            count = 2
        elif count != 0:
            count -= 1
        
def exit():
    global image
    del image

def pause():
    pass
def resume():
    pass
    
if __name__ == '__main__':
    gfw.run_main()
