from pico2d import *
os.chdir('C:\\Users\\op389\\OneDrive\\바탕 화면\\파이썬\\2017182044-2D-02\\수업내용\\3주차')
open_canvas()

grass=load_image('grass.png')
cha = load_image('character.png')


x=0

while x<800:
    clear_canvas_now()
    grass.draw_now(400,30)
    cha.draw_now(x,90)
    x=x+2
    delay(0.01)

close_canvas()    

    



