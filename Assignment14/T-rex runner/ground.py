import random
import arcade
class Ground(arcade.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.pic_path = random.choice(['images/ground0.png','images/ground1.png', 'images/ground2.png', 'images/ground3.png', 'images/ground4.png'])
        self.texture = arcade.load_texture(self.pic_path)
        self.center_x = width
        self.center_y = height
        self.change_x = -4
        self.change_y = 0
        self.width = 64
        self.height = 64