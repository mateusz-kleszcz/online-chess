from GUI.Button import Button


def change_time(engine, value):
    engine.time_white = value * 60 * 1000
    engine.time_black = value * 60 * 1000


def start_game(engine, value):
    engine.start_game()


class Controls:
    def __init__(self, screen):
        self.buttons = [
            Button(200, 40, 1000, 200, "3 minuty", 3, change_time),
            Button(200, 40, 1000, 300, "10 minut", 10, change_time),
            Button(200, 40, 1000, 400, "Graj", None, start_game),
        ]
        for button in self.buttons:
            button.add_to_scene(screen)

    def handle_button_click(self, location, engine):
        x, y = location
        for button in self.buttons:
            if button.x <= x <= button.x + button.x + button.size_x and button.y <= y <= button.y + button.size_y:
                button.handle_click(engine)

    def hide_buttons(self):
        for button in self.buttons:
            button.hide_button()