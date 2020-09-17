from pico2d import *

os.chdir('C:\\Users\\op389\\OneDrive\\바탕 화면\\파이썬\\2017182044-2D-02\\수업내용\\3주차')

open_canvas()

grass=load_image('grass.png')
cha=load_image('run_animation.png')

x=0
frame=0

while 0<800 :
    clear_canvas()
    grass.draw(400,30)
    cha.clip_draw(frame*100,0,100,100,x,90)
    update_canvas()
    frame=(frame+1)%8
    x=x+5
    delay(0.05)
    get_events()

close_canvas()    
