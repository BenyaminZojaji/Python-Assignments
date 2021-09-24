import random
import time
import arcade
from cactus import Cactus
from pterodactyl import Pterodactyl
from dino import Dino
from ground import Ground
DEFAULT_FONT_SIZE = 40
class Game(arcade.Window):
    def __init__(self):
        self.w = 800
        self.h = 600
        self.gravity = 0.3
        super().__init__(self.w , self.h ,"T-rex runner by Benyamin Zojaji")
        self.backeground_night_image = arcade.load_texture("images/background_night.png")
        self.backeground_day_image = arcade.load_texture("images/background_day.png")
        self.gameOver = False
        self.night = True
        self.cactus_speed = -4
        self.pterodactyl_speed = -5
        self.time_score = time.time()
        self.time_cactus = time.time()
        self.time_pterodactyl = time.time()
        self.time_backgroundChange = time.time()
        self.cactus_list = arcade.SpriteList()
        self.pterodactyl_list = arcade.SpriteList()
        self.dino = Dino()
        self.moon = arcade.Sprite('images/moon.png')
        self.moon.center_x = self.w
        self.moon.center_y = random.randint(400, 600)
        self.moon.change_x = -0.5
        self.moon.change_y = 0
        self.star = arcade.Sprite('images/star.png')
        self.star.center_x = self.w
        self.star.center_y = random.randint(250, 750)
        self.star.change_x = -1
        self.star.change_y = 0
        self.cloud = arcade.Sprite('images/cloud_night.png')
        self.cloud.center_x = self.w
        self.cloud.center_y = random.randint(350, 750)
        self.cloud.change_x = -1.5
        self.cloud.change_y = 0
        self.ground_list = arcade.SpriteList()
        for i in range(0, self.w, 64):
            ground = Ground(i ,100)
            self.ground_list.append(ground)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.dino, self.ground_list, self.gravity)
    def on_draw(self):
        self.time_now = time.time()
        if self.gameOver:
            if self.night:
                arcade.draw_text('YOU Lose', self.w//2-200, self.h//2, arcade.color.WHITE, DEFAULT_FONT_SIZE, width=400, font_name='Kenney Mini Square', align='center')
                arcade.draw_text('Press R for reset game', self.w//2-200, self.h//2-100, arcade.color.WHITE, DEFAULT_FONT_SIZE//2, width=400, font_name='Kenney Mini Square', align='center')
            else:
                arcade.draw_text('YOU Lose', self.w//2-200, self.h//2, arcade.color.BLACK, DEFAULT_FONT_SIZE, width=400, font_name='Kenney Mini Square', align='center')
                arcade.draw_text('Press R for reset game', self.w//2-200, self.h//2-100, arcade.color.BLACK, DEFAULT_FONT_SIZE//2, width=400, font_name='Kenney Mini Square', align='center')
        else:
            arcade.start_render()
            if self.time_now - self.time_backgroundChange > 15:
                self.time_backgroundChange = time.time()
                if self.night:
                    self.night = False
                else:
                    self.night = True
            if self.night:
                arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.backeground_night_image)
            else:
                arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.backeground_day_image)
            for ground in self.ground_list:
                ground.draw()
            for cactus in self.cactus_list:
                cactus.draw()
            for pterodactyl in self.pterodactyl_list:
                pterodactyl.draw()
            self.moon.draw()
            self.cloud.draw()
            self.star.draw()
            self.dino.draw()
            if self.night:
                arcade.draw_text('HI  %s  %s' %(str(self.dino.highScore).zfill(5), str(self.dino.score).zfill(5)), self.w-220, self.h-30, arcade.color.WHITE, DEFAULT_FONT_SIZE//2, width=400, font_name='Kenney Mini Square', align='left')
            else:
                arcade.draw_text('HI  %s  %s' %(str(self.dino.highScore).zfill(5), str(self.dino.score).zfill(5)), self.w-220, self.h-30, arcade.color.BLACK, DEFAULT_FONT_SIZE//2, width=400, font_name='Kenney Mini Square', align='left')
    def on_update(self, delta_time: float):
        self.time_now = time.time()
        if not self.gameOver:
            self.dino.score = int(self.time_now-self.time_score)
        if self.dino.score-self.dino.score_speed>15:
            self.dino.score_speed += 15
            self.cactus_speed -= 0.3
            self.pterodactyl_speed -= 0.5
        self.physics_engine.update()
        for pterodactyl in self.pterodactyl_list:
            pterodactyl.update_animation()
        if not self.dino.down:
            self.dino.update_animation()
        else:
            self.dino.manual_walkDown_animation()
            self.dino.down_frame += 1
        for ground in self.ground_list:
            if ground.center_x<0:
                self.ground_list.remove(ground)
                gr = Ground(self.w-64 ,100)
                self.ground_list.append(gr)
        if self.time_now - self.time_cactus > 4 :
            new_cactus = Cactus(self.w, 200, self.cactus_speed)
            self.cactus_list.append(new_cactus)
            self.time_cactus = time.time()
        if self.time_now - self.time_pterodactyl > 10 :
            new_pterodactyl = Pterodactyl(self.w, 200, self.pterodactyl_speed)
            self.pterodactyl_list.append(new_pterodactyl)
            self.time_pterodactyl = time.time()
        for cactus in self.cactus_list:
            cactus.update()
            if cactus.center_x < 0:
                self.cactus_list.remove(cactus)
        for pterodactyl in self.pterodactyl_list:
            pterodactyl.update()
            if pterodactyl.center_x<0:
                self.pterodactyl_list.remove(pterodactyl)
        if self.moon.center_x<0 or not self.moon:
            self.moon.center_x = self.w
            self.moon.center_y = random.randint(400, 600)
        if self.star.center_x<300 or not self.star:
            self.star.center_x = self.w
            self.star.center_y = random.randint(250, 750)
        if self.cloud.center_x<50 or not self.cloud:
            self.cloud.center_x = self.w
            self.cloud.center_y = random.randint(350, 750)
        self.moon.update()
        self.star.update()
        self.cloud.update()
        self.dino.set_x()
        for cactus in self.cactus_list:
            if arcade.check_for_collision(self.dino, cactus):
                self.gameOver = True
        for pterodactyl in self.pterodactyl_list:
            if arcade.check_for_collision(self.dino, pterodactyl):
                self.gameOver = True
    def on_key_press(self, key, modifiers):
        if key==arcade.key.UP:
            if self.physics_engine.can_jump():
                self.dino.change_y = 12
                self.dino.jump_sound()
        elif key==arcade.key.DOWN:
            self.dino.down = True
        elif key==arcade.key.R and self.gameOver:
            self.gameOver = False
            if self.dino.score > self.dino.highScore:
                self.dino.highScore = self.dino.score
            self.dino.write_highScore()
            self.dino.score = 0
            self.time_score = time.time()
            self.cactus_speed = -4
            self.pterodactyl_speed = -5
    def on_key_release(self, key, modifiers):
        if key==arcade.key.DOWN:
            self.dino.down = False
if __name__ == '__main__':
    game = Game()
    arcade.run()
