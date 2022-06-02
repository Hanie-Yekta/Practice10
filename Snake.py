import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

class Snake(arcade.Sprite):
    #tabe vizhegi ha
    def __init__(self):
        #erth bari vizhegi haye pedar
        super().__init__()

        #vizhegi haye khod tabe
        self.color=arcade.color.YELLOW
        self.width=10
        self.height=10
        self.change_x=0
        self.change_y=0
        self.speed=3
        self.score=0
        self.center_x=SCREEN_WIDTH // 2
        self.center_y=SCREEN_HEIGHT // 2

    #namayesh dar safheye bazi
    def draw(self):
        #mostatil tu por ba abaad moshakhas shode
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)
    
    #tabe tasir taqiraat harkat mar bar roye mokhtasatash
    def move(self):
        if self.change_x >0:
            self.center_x+=self.speed

        elif self.change_x < 0:
            self.center_x-=self.speed

        if self.change_y >0:
            self.center_y+=self.speed

        elif self.change_y < 0:
            self.center_y-=self.speed


    def eat(self):
        self.score +=1



class Apple(arcade.Sprite):
    #tabe vizhegi ha
    def __init__(self):
        #erth bari vizhegi haye pedar
        super().__init__()
        
        #vizhegi haye khod tabe
        self.width=10
        self.height=10
        self.color=arcade.color.RED
        self.r=5
        self.center_x=random.randint(0,SCREEN_WIDTH)
        self.center_y=random.randint(0,SCREEN_HEIGHT)

    #namayesh dar safheye bazi   
    def draw(self):
        #dayereye tu por ba abaad moshakhas shode
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)


class Game(arcade.Window):
    #tabe vizhegi ha
    def __init__(self):
        #erth bari vizhegi haye pedar
        super().__init__(width=SCREEN_WIDTH,height=SCREEN_HEIGHT,title="Snake Game")

        #tanzim rang background
        self.background_color=arcade.color.MEDIUM_JUNGLE_GREEN

        #sakht shei class apple
        self.food=Apple()

        #sakht shei class snake
        self.snake=Snake()

        
    #namayesh dar safheye bazi 
    def on_draw(self):
        #render giriW
        arcade.start_render()

        #namayesh apple dar zman ejraye safheye bazi
        self.food.draw()

        #namayesh mar dar zman ejraye safheye bazi
        self.snake.draw()

    #tamam manteq bazi(etefaqat drun bazi)
    def on_update(self, delta_time: float):
        self.snake.move()
        
        #check kardan baekhord sib va mar
        if arcade.check_for_collision(self.snake,self.food):
            self.snake.eat()
            
            #bad az khordan sib yek sib jadid ejaad shavad
            self.food=Apple()

    #pas az bardashtan angosht az roy dokme ejra mishavad
    def on_key_release(self, key: int, modifiers: int):

        #taein dokme va noe taqiraat harkat mar
        if key==arcade.key.LEFT:
            self.snake.change_x = -1

            #jologiri az orib harekat kardan mar
            self.snake.change_y= 0

        if key==arcade.key.RIGHT:
            self.snake.change_x= 1

            #jologiri az orib harekat kardan mar
            self.snake.change_y=0

        if key==arcade.key.UP:
            self.snake.change_y = 1

            #jologiri az orib harekat kardan mar
            self.snake.change_x=0

        if key==arcade.key.DOWN:
            self.snake.change_y = -1

            #jologiri az orib harekat kardan mar
            self.snake.change_x=0

    

#####################################

Sgame=Game()

#baraye baste nashodan barname
arcade.run()
