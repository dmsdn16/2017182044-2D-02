import gfw
from pico2d import *
from gobj import *

Class CD: # 카운트 다운
    def __init__(self):
         global font,CountDown
         font = gfw.font.load('res/ConsolaMalgun.ttf', 35)

         self.cd_color = (255,255,255)
         CountDown = 20

   def update(self):
       if SDL_KEYDOWN:
           CountDown -= 1
   def draw(self):




   
