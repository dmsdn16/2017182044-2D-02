
from pico2d import *

os.chdir('C:\\Users\\Administrator\\Desktop\\파이썬')


def handle_events():
	global running
	events = get_events()
	for event in events:
		if event.type==SDL_QUIT:
			running =False
		elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			running = False



open_canvas()

grass = load_image('grass.png')
cha=load_image('character.png')

x=0
running =True

while running:
    clear_canvas()
    grass.draw(400,30)
    cha.draw(x,90)
    update_canvas()

    handle_events()

    x=x+2

    delay(0.1)

