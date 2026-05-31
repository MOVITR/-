import spritePro as s
import random
class GameScene(s.Scene):
    def __init__(self):
        super().__init__()
        self.bg = s.Sprite('fon.png', pos=s.WH_C, size=s.WH, scene=self)
        self.player = s.Sprite('BIRD.png', pos=(100,300), size=(50,50), scene=self)
        self.player_body = s.add_physics(self.player, s.PhysicsConfig(bounce=0.8))
        self.pipes = []
        self.spawn_timer = s.Timer(2.0, self.spawn_pipes, repeat=True, scene = self)
        self.spawn_pipes()
        self.is_game_over = False
        s.physics.set_gravity(980)
        s.physics.set_bounds(s.pygame.Rect(0,0,400,600))
    def spawn_pipes(self):
        gap_y = random.randint(200, 400)
        gap_size = 150
        pipe_x=450
        top = s.Sprite('images.jpg', pos=(pipe_x, gap_y - gap_size/2 - 300), size=(80, 600), scene=self, sorting_order=5)
        top.angle = 180
        bottom = s.Sprite('images.jpg', pos=(pipe_x, gap_y +gap_size/2 + 300), size=(80, 600), scene=self, sorting_order=5)
        self.pipes.extend([top, bottom])
    def update(self, dt):
        if self.is_game_over:
            if s.input.was_pressed(s.pygame.K_SPACE) or s.input.was_mouse_pressed(1):
                 s.restart_scene()
            return
        if s.input.was_pressed(s.pygame.K_SPACE) or s.input.was_mouse_pressed(1):
            self.player_body.velocity.y = -400
        for pipe in self.pipes:
            pipe.x -= 200 * s.dt
            if self.player.collides_with(pipe):
                self.trigger_game_over()
            if self.player.y > s.WH[1] or self.player.y < 0:
                self.trigger_game_over()
            if pipe.x < -100:
                pipe.kill()
                self.pipes.remove(pipe) 
    def trigger_game_over(self):
        if self.is_game_over:
            return   
        self.is_game_over = True
        self.player_body.velocity.y = 0
        s.TextSprite('ИГРА ОКОНЧЕНА', pos=s.WH_C, font_size=40, color=(255, 0, 0), scene=self, sorting_order=30)
        s.TextSprite('Нажмите ПРОБЕЛ для рестарта', pos=(s.WH_C[0], s.WH_C[1] + 50), font_size=20, color=(0, 0, 0), scene=self, sorting_order=30)
if __name__ == '__main__':
    s.run(scene=GameScene, size=(400,600), title='Flappy Bird: Урок 2', fps=60)