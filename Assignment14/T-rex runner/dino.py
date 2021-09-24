import arcade
class Dino(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()
        self.stand_right_textures = [arcade.load_texture('images/dino.png')]
        self.walk_right_textures = [arcade.load_texture('images/walk0.png'), arcade.load_texture('images/walk1.png')]
        self.walk_down_textures = [arcade.load_texture('images/down0.png'), arcade.load_texture('images/down0.png')]
        self.walk_up_textures = [arcade.load_texture('images/dino.png')]
        self.center_x = 150
        self.center_y = 250
        self.width = 10
        self.height = 20
        self.scale = 1
        self.change_x = 0.5
        self.change_y = 0
        self.down_frame = 0
        try:
            myFile = open('db/high_score.txt', 'r')
            self.highScore = int(myFile.read())
            myFile.close()
        except:
            self.highScore = 0
        self.score = 0
        self.score_speed = 0
        self.down = False
    def set_x(self):
        self.center_x = 150
    def write_highScore(self):
        myFile = open('db/high_score.txt', 'w')
        myFile.write('%s' %self.score)
        myFile.close()
    def jump_sound(self):
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/phaseJump1.wav'), 1.0, 0.0,False)
    def manual_walkDown_animation(self):
        if self.down_frame <= 10:
            self.texture = arcade.load_texture('images/down0.png')
        elif self.down_frame <= 20:
            self.texture = arcade.load_texture('images/down1.png')
        else:
            self.down_frame = 0
