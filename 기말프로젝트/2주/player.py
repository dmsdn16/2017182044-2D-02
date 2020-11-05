from pico2d import *
import gfw_image
from gobj import *
import helper

class Player:
     KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):  (-1,  0),
        (SDL_KEYDOWN, SDLK_RIGHT): ( 1,  0),
        (SDL_KEYDOWN, SDLK_DOWN):  ( 0, -1),
        (SDL_KEYDOWN, SDLK_UP):    ( 0,  1),
        (SDL_KEYUP, SDLK_LEFT):    ( 1,  0),
        (SDL_KEYUP, SDLK_RIGHT):   (-1,  0),
        (SDL_KEYUP, SDLK_DOWN):    ( 0,  1),
        (SDL_KEYUP, SDLK_UP):      ( 0, -1),
    }
     KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
     image = None

     def __Init__(self):
         self.pos = get_canvas_width()//2 ,get_canvas_height()//2

         if image==None:
            Player.image = gfw_image.load(RES_DIR + '/character.png')

       
     def draw(self):
        Player.image = gfw_image.load(RES_DIR + '/character.png')
        self.image.draw(550,500)


   
  