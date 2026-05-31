import random
import spritePro as s

class GameScreen(s.Scene):
    def __init__(self):
        super().__init__()
        self.bg = s.Sprite('фон Flappy Bird.jpg', pos=s.WH_C, size=s.WH, scene=self)
        self.player = s.Sprite('птичкак Flappy Bird.jfif', pos=(100, 300), size=(50, 50), scene=self)
        self.player_body = s.add_physics(self.player, s.PhysicsConfig(bounce=0.8))
        self.pipes = []
        self.spawn_timer = s.Timer(2.0, self.spawn_pipes, repeat=True, scene=self)
        self.spawn_pipes()
        self.is_game_over = False
        s.physics.set_gravity(980)
        s.physics.set_bounds(s.pygame.Rect(0,0, 400, 600))
    def update(self, dt):
        if s.input.was_pressed(s.pygame.K_SPACE) or s.input.was_mouse_pressed(1):
            self.player_body.velocity.y = -400
            for pipe in self.pipes:
                pipe.x -= 200 * s.dt
                if self.player.collides_with(pipe):
                    self.trigger_game_over()

    def spawn_pipes(self):
        gap_y = random.randint(200, 400)
        gap_size = 150
        pipe_x = 450
        top = s.Sprite('pipe.png', pos=(pipe_x, gap_y - gap_size/2 - 300), size=(80, 600), scene=self, sorting_order=5)
        top.angle = 180
        bottom = s.Sprite('pipe.png', pos=(pipe_x, gap_y + gap_size/2 - 300), size=(80, 600), scene=self, sorting_order=5)
        self.pipes.extend([top, bottom])


if __name__ == '__main__':
    s.run(scene=GameScreen, size=(400, 600), title='фон Flappy Bird.jpg', fps=60)   


#s.run(scene=GameScreen, size=(400, 600), title='фон Flappy Bird.jpg')
