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
    def updata(self):
        pass

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = random.randrange(0,400)
        self.frame = random.randrange(0,8)


    def draw(self):
        self.image.clip_draw(self.frame * 100,0,100,100,self.x,90)


    def updata(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8

class Zombie:
    def __init__(self):
        self.image = load_image('zombie_run_animation.png')
        self.x, self.y = 100, 170
        self.frame = 0


    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width,0,frame_width,frame_height,
                             self.x,self.y, frame_width //2 , frame_height // 2)

    def updata(self):
        self.x += 5
        self.frame = (self.frame + 1) % 10

class Small_Ball:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x = random.randint(0, 800)
        self.y = 599
        self.fall_speed = random.randint(5, 20)

    def updata(self):
        # 45는 grass 높이
        if self.y - self.fall_speed < 45 + self.image.h / 2:
            self.y = 45 + self.image.h / 2
        else:
            self.y -= self.fall_speed
    def draw(self):
        self.image.draw(self.x, self.y)


class Big_Ball:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x = random.randint(0, 800)
        self.y = 599
        self.fall_speed = random.randint(5, 20)
    def updata(self):
        # 45는 grass 높이
        if self.y - self.fall_speed < 45 + self.image.h / 2:
            self.y = 45 + self.image.h / 2
        else:
            self.y -= self.fall_speed
    def draw(self):
        self.image.draw(self.x, self.y)


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
    global world # world list

    world = [] # 하나도 객체가 없는 월드
    grass = Grass()
    world.append(grass) # 땅을 만들고 월드에 추가

    team = [Boy() for i in range(11)]
    world += team # 월드에 소년들 추가, 리스트기 떄문에 더한다.

    zombie = Zombie()
    world.append(zombie)


    Sballs = [Small_Ball() for i in range(10)]
    world += Sballs
    Bballs = [Big_Ball() for i in range(10)]
    world += Bballs

    running = True

#게임 로직
def updata_world():
    [game_object.updata() for game_object in world]

def render_world():
    # grass 객체의 draw 메서드를 호출하여 화면에 잔디를 그린다
    clear_canvas()
    [game_object.draw() for game_object in world]
    update_canvas()

reset_world()
while running:
    handle_events()
    updata_world()
    render_world()
    delay(0.05)


close_canvas()
