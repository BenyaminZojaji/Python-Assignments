import arcade
class Player(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()
        self.stand_right_textures =[arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk4.png")]
        self.stand_left_textures = [arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk4.png",mirrored = True)]
        self.walk_right_textures = [arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk0.png"),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png"),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk2.png"),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk3.png"),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk4.png"),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk5.png"),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk6.png"),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk7.png")]
        self.walk_left_textures = [arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk0.png",mirrored = True),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png",mirrored = True),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk2.png",mirrored = True),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk3.png",mirrored = True),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk4.png",mirrored = True),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk5.png",mirrored = True),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk6.png",mirrored = True),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk7.png",mirrored = True)]
        self.center_x = 380
        self.center_y = 400
        self.speed = 5
        self.width = 10
        self.height = 15
        self.pocket = []