import arcade
from math import cos, sin
import math
from time import sleep
import random

WINDOW_TITLE = "Back to the Front"
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720
SPRITE_SCALING = 1
BASIC_SPEED = 10
BASIC_ANGLE = 5
BATTERIES_COUNT = 15
ENEMIES_COUNT = 15

class Delorean(arcade.Sprite):
    def __init__(self, path_or_texture, scale):
        super().__init__(path_or_texture, scale)
        self.angle_change = 0

    def update(self, delta_time = 1/60, *args, **kwargs):
        self.center_y += self.change_y
        self.center_x += self.change_x
        self.angle += self.change_angle
        if self.angle > 360:
            self.angle -= 360


        if self.top > WINDOW_HEIGHT:
            self.top = WINDOW_HEIGHT
        if self.bottom < 0:
            self.bottom = 0
        if self.left < 0:
            self.left = 0
        if self.right > WINDOW_WIDTH:
            self.right = WINDOW_WIDTH

class Battery(arcade.Sprite):
    def __init__(self, path_or_texture, scale):
        super().__init__(path_or_texture, scale)

class Octopus(arcade.Sprite):
    pass

class MyGame(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.WHITE)
        self.delorean_sprite = None
        self.delorean_list = None

        self.batteries_list = None
        self.batteries_count = 0

        self.enemies_list = None
        self.enemies_count = 0

        self.score = 0

        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

        self.engine_sound = None
        self.engine_sound_player = None

        self.battery_sound = None

    def setup(self):
        self.delorean_list = arcade.SpriteList()

        self.delorean_sprite = Delorean("delorean.png", SPRITE_SCALING)
        self.delorean_sprite.center_x = WINDOW_WIDTH // 2
        self.delorean_sprite.center_y = WINDOW_HEIGHT // 2
        self.delorean_list.append(self.delorean_sprite)

        self.score = 0

        self.batteries_count = BATTERIES_COUNT
        self.batteries_list = arcade.SpriteList()
        for i in range(self.batteries_count):
            battery = Battery("battery.png", SPRITE_SCALING)
            battery.center_x = random.randrange(int(battery.width), WINDOW_WIDTH - int(battery.width))
            battery.center_y = random.randrange(int(battery.width), WINDOW_HEIGHT - int(battery.width))
            self.batteries_list.append(battery)

        self.enemies_list = arcade.SpriteList()
        self.enemies_count = ENEMIES_COUNT
        for i in range(self.enemies_count):
            octopus = Octopus("octopus.gif", SPRITE_SCALING)
            octopus.center_x = random.randrange(int(battery.width), WINDOW_WIDTH - int(battery.width))
            octopus.center_y = random.randrange(int(battery.width), WINDOW_HEIGHT - int(battery.width))
            self.enemies_list.append(octopus)

        self.engine_sound = arcade.load_sound("sounds/warp_engine.wav")

        self.battery_sound = arcade.load_sound("sounds/zap1.mp3")

    def draw_score(self):
        arcade.draw_text(self.score,20, WINDOW_HEIGHT - 40, arcade.color.BLACK, font_size=20, font_name="Chava")

    def on_draw(self):
        self.clear()
        self.batteries_list.draw()
        self.enemies_list.draw()
        self.delorean_list.draw()
        self.draw_score()


    def update_delorean_speed(self):
        self.delorean_sprite.change_y = 0
        self.delorean_sprite.change_x = 0
        self.delorean_sprite.change_angle = 0

        if self.up_pressed and not self.down_pressed:
            self.delorean_sprite.change_y = BASIC_SPEED * cos(math.radians(self.delorean_sprite.angle))
            self.delorean_sprite.change_x = BASIC_SPEED * sin(math.radians(self.delorean_sprite.angle))
        elif self.down_pressed and not self.up_pressed:
            self.delorean_sprite.change_y = -BASIC_SPEED * cos(math.radians(self.delorean_sprite.angle))
            self.delorean_sprite.change_x = -BASIC_SPEED * sin(math.radians(self.delorean_sprite.angle))
        if self.left_pressed and not self.right_pressed:
            self.delorean_sprite.change_angle = -BASIC_ANGLE
        elif self.right_pressed and not self.left_pressed:
            self.delorean_sprite.change_angle = BASIC_ANGLE

    def play_sound(self):
        if self.up_pressed or self.down_pressed:
            if self.engine_sound_player is not None and self.engine_sound_player.playing:
                self.engine_sound.stop(self.engine_sound_player)
            self.engine_sound_player = self.engine_sound.play(loop=True)
        else:
            self.engine_sound.stop(self.engine_sound_player)

    def stop_sound(self):
        if not self.up_pressed and not self.down_pressed:
            self.engine_sound.stop(self.engine_sound_player)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = True
            self.update_delorean_speed()
        elif key == arcade.key.DOWN:
            self.down_pressed = True
            self.update_delorean_speed()
        elif key == arcade.key.LEFT:
            self.left_pressed = True
            self.update_delorean_speed()
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
            self.update_delorean_speed()

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.play_sound()

        if key == arcade.key.R:
            self.setup()


    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.up_pressed = False
            self.update_delorean_speed()
        elif key == arcade.key.DOWN:
            self.down_pressed = False
            self.update_delorean_speed()
        elif key == arcade.key.LEFT:
            self.left_pressed = False
            self.update_delorean_speed()
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
            self.update_delorean_speed()

        if key == arcade.key.UP or key == arcade.key.DOWN:
            sleep(0.1)
            self.stop_sound()

    def on_update(self, delta_time):
        self.delorean_list.update(delta_time)

        hit_list = arcade.check_for_collision_with_list(self.delorean_sprite, self.batteries_list)

        for battery in hit_list:
            self.battery_sound.play()
            battery.remove_from_sprite_lists()
            self.batteries_count -= 1
            self.score += 1

def main():
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    game = MyGame()
    game.setup()
    window.show_view(game)
    arcade.run()

if __name__ == '__main__':
    main()