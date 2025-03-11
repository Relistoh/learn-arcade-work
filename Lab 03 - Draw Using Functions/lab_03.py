import arcade
import arcade as arc

WINDOW_TITLE = "I AM A WHALE"
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = arcade.color.BLACK

def draw_whale_looking_right(x, y, scale):
    arc.draw_arc_filled(x, y, scale * 50, scale * 25, arc.color.BLUE, 0, 180)
    arc.draw_arc_filled(x, y, scale * 50, scale * 15, arc.color.WHITE, 180, 360)
    arc.draw_ellipse_filled(x - scale * 15, y + scale * 5, scale * 4, scale * 2, arc.color.BLACK, tilt_angle=-40)

def draw_whale_looking_left(x, y, scale):
    arc.draw_arc_filled(x, y, scale * 50, scale * 25, arc.color.BLUE, 0, 180)
    arc.draw_arc_filled(x, y, scale * 50, scale * 15, arc.color.WHITE, 180, 360)
    arc.draw_ellipse_filled(x + scale * 15, y + scale * 5, scale * 4, scale * 2, arc.color.BLACK, tilt_angle=40)

def draw_whale_looking_forward():
    arc.draw_arc_filled(400, 220, 200, 100, color=arc.color.BLUE, start_angle=-20, end_angle=180)
    arc.draw_arc_filled(200, 220, 200, 100, color=arc.color.BLUE, start_angle=0, end_angle=200)

    arc.draw_arc_filled(300, 370, 120, 200, color=arc.color.DARK_BLUE, start_angle=0, end_angle=180)
    arc.draw_arc_outline(300, 370, 120, 200, color=arc.color.GRAY, start_angle=0, end_angle=180, border_width=10)

    arc.draw_arc_filled(300, 500, 300, 100, color=arc.color.DARK_BLUE, start_angle=180, end_angle=360)
    arc.draw_arc_outline(300, 500, 300, 100, color=arc.color.GRAY, start_angle=180, end_angle=360, border_width=10)

    arc.draw_arc_filled(300, 500, 300, 20, color=arc.color.BLACK, start_angle=180, end_angle=360)
    arc.draw_arc_outline(300, 500, 300, 20, color=arc.color.GRAY, start_angle=180, end_angle=360, border_width=10)

    arc.draw_arc_filled(300, 220, 300, 350, color=arc.color.BLUE, start_angle=0, end_angle=180)
    arc.draw_arc_outline(300, 220, 300, 350, color=arc.color.WHITE, start_angle=0, end_angle=180, border_width=10)

    arc.draw_arc_filled(300, 220, 305, 100, color=arc.color.WHITE, start_angle=180, end_angle=360)

    arc.draw_ellipse_filled(200, 250, 20, 30, color=arc.color.BLACK)
    arc.draw_ellipse_filled(400, 250, 20, 30, color=arc.color.BLACK)

    arc.draw_text("I AM A WHALE", 70, 80, color=arc.color.WHITE, font_size=50, width=100)

current_x = WINDOW_WIDTH
moving_left = True
scale = 1

def on_draw(delta_time):
    global current_x, moving_left, scale
    arc.View.clear(arc.View())
    if scale == 9 and current_x == WINDOW_WIDTH // 2:
        draw_whale_looking_forward()
        return 0
    if current_x == 0:
        moving_left = False
        scale += 2
    if current_x == WINDOW_WIDTH:
        moving_left = True
        scale += 2
    if moving_left:
        current_x -= 10
        draw_whale_looking_right(current_x, WINDOW_HEIGHT // 2, scale)
    else:
        current_x += 10
        draw_whale_looking_left(current_x, WINDOW_HEIGHT // 2, scale)


def main():
    arc.open_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    arc.set_background_color(BACKGROUND_COLOR)

    arc.schedule(on_draw, 1/60)
    arc.run()

if __name__ == "__main__":
    main()