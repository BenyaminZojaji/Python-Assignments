import random
import arcade
WIN_HEIGHT = 700
WIN_WIDTH = 750
DEFAULT_FONT_SIZE = 5
class Dynamite(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.img = 'img/dynamite.png'
        self.dynamite = arcade.Sprite(self.img, 0.02)
        self.dynamite.center_x = random.randint(10, w-10)
        self.dynamite.center_y = random.randint(10, h-10)
    def draw(self):
        self.dynamite.draw()
class Pear(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.img = 'img/pear.png'
        self.pear = arcade.Sprite(self.img, 0.1)
        self.pear.center_x = random.randint(10, w-10)
        self.pear.center_y = random.randint(10, h-10)
    def draw(self):
        self.pear.draw()
class Apple(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.img = 'img/apple.png'
        self.apple = arcade.Sprite(self.img, 0.03)
        self.apple.center_x = random.randint(10, w-10)
        self.apple.center_y = random.randint(10, h-10)
    def draw(self):
        self.apple.draw()
class Snake(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color_manual = [arcade.color.GREEN, arcade.color.RED, arcade.color.BLACK, arcade.color.CYBER_YELLOW, arcade.color.ORANGE, arcade.color.PINK, arcade.color.BROWN]
        self.speed = 4
        self.width = 16
        self.height = 16
        self.center_x = w//2
        self.center_y = h//2
        self.r = 8
        self.change_x = 0
        self.change_y = 0
        self.score = 1
        self.body = []
        self.body.append([self.center_x,self.center_y])
    def draw(self):
        for index, item in enumerate(self.body):
            arcade.draw_circle_filled(item[0], item[1], self.r, self.color_manual[index%(len(self.color_manual))])
    def move(self):
            for i in range(len(self.body)-1, 0, -1):
                self.body[i][0] = self.body[i-1][0]
                self.body[i][1] = self.body[i-1][1]
            self.center_x += self.speed * self.change_x
            self.center_y += self.speed * self.change_y
            if self.body:
                self.body[0][0] += self.speed * self.change_x
                self.body[0][1] += self.speed * self.change_y
    def eat(self, food):
        if food == 'apple':
            self.score += 1
            self.body.append([self.body[len(self.body)-1][0]+3000, self.body[len(self.body)-1][1]])
        elif food == 'pear':
            self.score += 2
            self.body.append([self.body[len(self.body)-1][0]+3000, self.body[len(self.body)-1][1]])
            self.body.append([self.body[len(self.body)-1][0]+3000, self.body[len(self.body)-1][1]])
        elif food == 'dynamite':
            self.score -= 1
            self.body.pop()
class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self, WIN_WIDTH, WIN_HEIGHT,"Super Snake by Benyamin Zojaji")
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake(WIN_WIDTH, WIN_HEIGHT)
        self.apple = Apple(WIN_WIDTH, WIN_HEIGHT)
        self.pear = Pear(WIN_WIDTH, WIN_HEIGHT)
        self.dynamite = Dynamite(WIN_WIDTH, WIN_HEIGHT)
    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.dynamite.draw()
        start_x = 10
        start_y = WIN_HEIGHT - 20
        arcade.draw_text('Score: %i'%self.snake.score,
                         start_x, start_y,
                         arcade.color.BLACK, DEFAULT_FONT_SIZE * 2, width=WIN_WIDTH, align='left')
        if self.snake.score <= 0 or self.snake.center_x<0 or self.snake.center_x>WIN_WIDTH or self.snake.center_y<0 or self.snake.center_y>WIN_HEIGHT:
            arcade.draw_text('GAME OVER',
                         WIN_WIDTH//2, WIN_HEIGHT//2,
                         arcade.color.BLACK, DEFAULT_FONT_SIZE * 5, width=WIN_WIDTH, align='left')
            arcade.exit()
    def on_update(self, delta_time: float):
        self.snake.move()
        if arcade.check_for_collision(self.snake, self.apple.apple):
            self.snake.eat('apple')
            self.apple = Apple(WIN_WIDTH, WIN_HEIGHT)
        elif arcade.check_for_collision(self.snake, self.pear.pear):
            self.snake.eat('pear')
            self.pear = Pear(WIN_WIDTH, WIN_HEIGHT)
        elif arcade.check_for_collision(self.snake, self.dynamite.dynamite):
            self.snake.eat('dynamite')
            self.dynamite = Dynamite(WIN_WIDTH, WIN_HEIGHT)
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
if __name__=="__main__":
    game = Game()
    arcade.run()