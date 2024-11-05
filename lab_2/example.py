import curses
from dataclasses import dataclass, field
from . import environment
from .environment import draw_background, draw_tracks, draw_statusbar, \
                    draw_debris, draw_horizon, draw_car, draw_money
from . import hud
from .hud import draw_hud
from .mechanics import update_state
from .config import GAME_SIZE, FPS, BASE_SPEED
from .misc import limit_fps


@dataclass
class GameState:
    frames: int = 0
    time: float = 0.0  # seconds
    speed: float = BASE_SPEED  # coord per frame
    car: any = None
    car_x: float = 0  # range -1:1
    car_steer_tuple: tuple = None
    car_speed_tuple: tuple = None
    debris: list = field(default_factory=list)  # debris objects drawn in scene
    money: list = field(default_factory=list)  # money objects drawn in scene
    score: int = 0
    pdb: bool = False  # for testing


SCENE = [draw_statusbar, draw_hud, draw_horizon, draw_tracks,
         draw_debris, draw_car, draw_money, draw_background]
state = GameState()  # создаем экземпляр GameState


@limit_fps(fps=FPS)
def draw_scene(screen):
    for draw_element in reversed(SCENE):
        draw_element(screen, state)
    screen.refresh()


def main(screen):
    screen.resize(*GAME_SIZE)
    screen.nodelay(True)
    environment.init(screen)
    hud.init(screen)
    while True:
        draw_scene(screen)
        key = screen.getch()
        if key == ord('q'):
            break
        elif key == ord('p'):
            state.pdb = True
        else:
            update_state(key, state)
        state.frames += 1
        state.time += 1 / FPS
    screen.clear()
    screen.getkey()


def run():
    curses.wrapper(main)
