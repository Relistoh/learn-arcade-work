import arcade as arc

arc.open_window(600, 600, "Whale")
arc.set_background_color(arc.color.BLACK)

arc.start_render()

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

arc.finish_render()

arc.run()