from pico2d import *
import random
open_canvas()
class Grass:
    #생성자 함수 초기화수행
    def __init__(self):
        # grass image load grass 객체의 속성을 정의하고 초기화
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)
        pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    grass = Grass()
    
    running = True


def updata_world():
    pass


def render_world():
    # grass 객체의 draw 메서드를 호출하여 화면에 잔디를 그린다
    clear_canvas()
    grass.draw()
    update_canvas()
    pass

reset_world()
while running:
    handle_events()
    updata_world()
    render_world()
    delay(0.05)


close_canvas()
