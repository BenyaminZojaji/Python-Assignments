import time
import arcade
from player import Player
from enemy import Enemy
from ground import Ground
DEFAULT_FONT_SIZE = 40
class Game(arcade.Window):
    def __init__(self):
        self.w = 800
        self.h = 600
        self.gravity = 0.3
        self.win = False
        super().__init__(self.w , self.h ,"Simple platform game")
        self.backeground_image = arcade.load_texture("images/snow.png")
        self.time_enterEnemy = time.time()
        self.player = Player()
        self.ground_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.key = arcade.Sprite(":resources:images/items/keyYellow.png")
        self.key.center_x=100
        self.key.center_y=350
        self.key.width = 50
        self.key.height=50
        self.lock = arcade.Sprite(":resources:images/tiles/lockYellow.png")
        self.lock.center_x = 770
        self.lock.center_y = 90
        self.lock.width = 50
        self.lock.height=50
        for i in range(0, self.w, 113):
            ground = Ground(i ,8)
            self.ground_list.append(ground)
        for i in range(90,330,113):
            ground = Ground(i ,245)
            self.ground_list.append(ground)
        for i in range(520,650,113):
            ground = Ground(i ,190)
            self.ground_list.append(ground)
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,self.ground_list,self.gravity)
        self.enemy_physics_engine_list = []
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.backeground_image)
        for ground in self.ground_list:
            ground.draw()
        self.lock.draw()
        if self.win:
            arcade.draw_text('YOU WIN', self.w//2-200, self.h//2, arcade.color.BLACK, DEFAULT_FONT_SIZE, width=400, align='center')
            arcade.draw_text('Press R for reset game', self.w//2-200, self.h//2-100, arcade.color.BLACK, DEFAULT_FONT_SIZE//2, width=400, align='center')
        else:
            try:
                self.key.draw()  
            except:
                pass
            self.player.draw()
            for enemy in self.enemy_list:
                enemy.draw()
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.change_x = -1 * self.player.speed
        elif key == arcade.key.RIGHT:
            self.player.change_x = 1 * self.player.speed
        elif key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player.change_y = 10
        elif key == arcade.key.R and self.win:
            self.win = False
            self.player.pocket.clear()
            self.player.center_x = 380
            self.player.center_y = 400
            self.key = arcade.Sprite(":resources:images/items/keyYellow.png")
            self.key.center_x=100
            self.key.center_y=350
            self.key.width = 50
            self.key.height=50
            self.lock = arcade.Sprite(":resources:images/tiles/lockYellow.png")
            self.lock.center_x = 770
            self.lock.center_y = 90
            self.lock.width = 50
            self.lock.height=50
    def on_key_release(self, key, modifiers):
        self.player.change_x = 0           
    def on_update(self, delta_time: float):
        self.physics_engine.update()
        self.player.update_animation()
        for enemy in self.enemy_list:
            enemy.update_animation()
        for enemy in self.enemy_physics_engine_list:
            enemy.update()
        self.time_now = time.time()
        if self.time_now - self.time_enterEnemy > 5 :
            new_enemy = Enemy()
            self.enemy_list.append(new_enemy)
            self.enemy_physics_engine_list.append(arcade.PhysicsEnginePlatformer(new_enemy,self.ground_list,self.gravity))
            self.time_enterEnemy = time.time()
        for enemy in self.enemy_list:
            if arcade.check_for_collision(self.player, enemy):
                self.key = arcade.Sprite(":resources:images/items/keyYellow.png")
                self.key.center_x=100
                self.key.center_y=350
                self.key.width = 50
                self.key.height=50
                self.player.pocket.clear()
        try:
            if arcade.check_for_collision(self.player,self.key):
                self.player.pocket.append(self.key)
                del self.key
        except:
            pass
        if arcade.check_for_collision(self.player,self.lock) and len(self.player.pocket)==1 :
            self.lock.texture = arcade.load_texture(":resources:images/items/flagGreen1.png")
            self.lock.width = 60
            self.lock.height = 90
            self.lock.center_y = 110
            self.win = True
if __name__=='__main__':
    game = Game()
    arcade.run()        