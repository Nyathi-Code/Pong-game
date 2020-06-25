import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window


class Game_Screen(Widget):
    Window.size = (300, 500)
    ball = ObjectProperty(None)
    player_one = ObjectProperty(None)
    player_two = ObjectProperty(None)

    def start_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        self.player_one.ball_bounces(self.ball)
        self.player_two.ball_bounces(self.ball)

        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        if self.ball.x < self.x:
            self.player_two.score += 1
            self.start_ball(vel=(4, 0))

        if self.ball.x > self.width:
            self.player_one.score += 1
            self.start_ball(vel=(-4, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player_one.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player_two.center_y = touch.y

class Game_Paddles(Widget):
    score = NumericProperty(0)


    def ball_bounces(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height/2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1
            ball.velocity = vel.x, vel.y + offset

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos





class My_App(App):
    def build(self):
        game = Game_Screen()
        game.start_ball()
        Clock.schedule_interval(game.update, 1.0 / 57.0)
        return game





if __name__ == "__main__":
    My_App().run()
