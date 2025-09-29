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

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = 400
        self.frame = 0
        self.dir = 1
    def draw(self):
        self.image.clip_draw(self.frame * 100,0,100,100,self.x,90)
    def updata(self):
        self.x += 5
        self.frame += (self.frame + 1) % 8

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

#게임 렌더링
def reset_world():
    global running
    global grass
    global boy
    grass = Grass()
    boy = Boy()
    
    running = True

#게임 로직
def updata_world():
    boy.updata()
    pass


def render_world():
    # grass 객체의 draw 메서드를 호출하여 화면에 잔디를 그린다
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
    pass

reset_world()
while running:
    handle_events()
    updata_world()
    render_world()
    delay(0.05)


close_canvas()
