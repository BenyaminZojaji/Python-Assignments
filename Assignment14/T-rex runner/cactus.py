import random
import arcade
class Cactus(arcade.Sprite):
    def __init__(self, width, height, speed):
        super().__init__()
        self.pic_path = random.choice(['images/cactus1_night.png','images/cactus4_night.png'])
        self.texture = arcade.load_texture(self.pic_path)
        self.center_x = width
        self.center_y = 164
        self.change_x = speed #-4
        self.change_y = 0
        self.width = 100
        self.height = 100