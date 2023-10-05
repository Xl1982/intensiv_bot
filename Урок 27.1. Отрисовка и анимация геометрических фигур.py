import arcade
import random
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def create_cloud(x, y):
    arcade.draw_circle_filled(
        center_x=x,
        center_y=y,
        color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
        radius=60
    )

class Game(arcade.Window):
    def __init__(self):
        super().__init__(
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            title='Рисование фигур')
        self.background_color = (255, 255, 255)

    def on_draw(self):
        self.clear()
        for i in range(1, 7):
            create_cloud(random.randint(0, 500) * i, random.randint(0, 500))
        for j in range(1,7):
            create_cloud(random.randint(0, 500) *j + 90, random.randint(0, 500))


if __name__ == '__main__':
    game = Game()
    arcade.run()


























"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Game(arcade.Window):
   def __init__(self):
       super().__init__(
           width=SCREEN_WIDTH,
           height=SCREEN_HEIGHT,
           title="Геометрические фигуры и их анимация",
       )
       self.x = 100
       self.y = 100
       self.radius = 30
       self.color = arcade.color.YELLOW
       self.change_x = 3
       self.change_y = 4

   def setup(self):
       pass

   def on_draw(self):
       self.clear()
       arcade.draw_circle_outline(self.x, self.y, self.radius, self.color)

   def update(self, delta_time: float):
       self.x += self.change_x
       self.y += self.change_y
       if self.x + self.radius / 2 > SCREEN_WIDTH or self.x - self.radius / 2 < 0:
           self.change_x = -self.change_x
       if self.y + self.radius / 2 > SCREEN_HEIGHT or self.y - self.radius / 2 < 0:
           self.change_y = -self.change_y


if __name__ == "__main__":
   game = Game()
   game.setup()
   arcade.run()
"""