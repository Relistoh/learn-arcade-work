import arcade as arc

WINDOW_TITLE = "UFO"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

class Ufo:
    def __init__(self, size, color):
        self.size = size
        self.color = color
        self.x = WINDOW_WIDTH / 2
        self.y = WINDOW_HEIGHT / 2
        self.speed_x = 0
        self.speed_y = 0
        self.speed = 5

        self.laser_sound = arc.load_sound("phaserUp6.mp3")
        self.laser_sound_player = None

    def draw(self):
        arc.draw_circle_filled(self.x, self.y, self.size, self.color)
        arc.draw_circle_filled(self.x, self.y, self.size // 2 + self.size // 10, arc.color.DARK_GRAY)
        arc.draw_circle_filled(self.x, self.y, self.size // 2, arc.color.LIGHT_CYAN)
        arc.draw_circle_filled(self.x, self.y + 3 * self.size // 4, self.size // 10, arc.color.WHITE)
        arc.draw_circle_filled(self.x, self.y - 3 * self.size // 4, self.size // 10, arc.color.WHITE)
        arc.draw_circle_filled(self.x - 3 * self.size // 4, self.y, self.size // 10, arc.color.WHITE)
        arc.draw_circle_filled(self.x + 3 * self.size // 4, self.y, self.size // 10, arc.color.WHITE)
        arc.draw_ellipse_filled(self.x, self.y + self.size // 10, self.size // 1.5, self.size // 2, arc.color.UFO_GREEN)
        arc.draw_ellipse_filled(self.x, self.y, self.size // 2, self.size // 1.5, arc.color.UFO_GREEN)
        arc.draw_ellipse_filled(self.x + self.size // 6, self.y + self.size // 10, self.size // 3, self.size // 4, arc.color.BLACK, -40)
        arc.draw_ellipse_filled(self.x - self.size // 6, self.y + self.size // 10, self.size // 3, self.size // 4, arc.color.BLACK, 40)

    def play_laser(self):
        if not self.laser_sound_player or not self.laser_sound_player.playing:
            self.laser_sound_player = self.laser_sound.play()

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x + self.size >= WINDOW_WIDTH:
            self.play_laser()
            self.x = WINDOW_WIDTH - 2 * self.size
        if self.y + self.size >= WINDOW_HEIGHT:
            self.play_laser()
            self.y = WINDOW_HEIGHT - 2 * self.size
        if self.x - self.size <= 0:
            self.play_laser()
            self.x = self.size * 2
        if self.y - self.size <= 0:
            self.play_laser()
            self.y = self.size * 2

class MyGame(arc.Window):
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        self.ufo = Ufo(70, arc.color.GRAY)
        arc.set_background_color(arc.color.BLACK)

    def on_draw(self):
        self.clear()
        self.ufo.draw()

    def on_update(self, delta_time):
        self.ufo.update()

    def on_key_press(self, symbol, modifiers):
        if symbol == arc.key.W:
            self.ufo.speed_y = self.ufo.speed
        elif symbol == arc.key.A:
            self.ufo.speed_x = -self.ufo.speed
        elif symbol == arc.key.S:
            self.ufo.speed_y = -self.ufo.speed
        elif symbol == arc.key.D:
            self.ufo.speed_x = self.ufo.speed
        elif symbol == arc.key.SPACE:
            self.ufo.speed += 1
        elif symbol == arc.key.MINUS:
            self.ufo.size /= 2
        elif symbol == arc.key.EQUAL:
            self.ufo.size *= 2


    def on_key_release(self, symbol, modifiers):
        if symbol == arc.key.W and self.ufo.speed_y > 0:
            self.ufo.speed_y = 0
        elif symbol == arc.key.S and self.ufo.speed_y < 0:
            self.ufo.speed_y = 0
        elif symbol == arc.key.A and self.ufo.speed_x < 0:
            self.ufo.speed_x = 0
        elif symbol == arc.key.D and self.ufo.speed_x > 0:
            self.ufo.speed_x = 0

def main():
    window = MyGame()
    arc.run()

if __name__ == '__main__':
    main()