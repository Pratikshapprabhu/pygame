import object 
import pygame

class Game:
    def __init__(self):
        ok,fail=pygame.init()
        print(f"Initialization passed = {ok} failed = {fail} ")
        self.screen = pygame.display.set_mode((800,600))
        self.clock  = pygame.time.Clock()
        self.run = True
        self.objects = []

    def init(self):
        self.player=object.Player()

    def handl_events(self):
        delay = self.clock.tick(60)
        events = pygame.event.get()
        for eve in events:
            if eve.type == pygame.QUIT:
                self.run = False
            elif eve.type == pygame.KEYDOWN:
                if eve.key == pygame.K_w:
                    self.player.vel[1] = -100*delay/1000
                elif eve.key == pygame.K_a:
                    self.player.vel[0] = -100*delay/1000
                elif eve.key == pygame.K_s:
                    self.player.vel[1] = 100*delay/1000
                elif eve.key == pygame.K_d:
                    self.player.vel[0] = 100*delay/1000
            elif eve.type == pygame.KEYUP:
                if eve.key == pygame.K_w or eve.key == pygame.K_s:
                    self.player.vel[1] = 0
                elif eve.key == pygame.K_a or eve.key == pygame.K_d:
                    self.player.vel[0] = 0

    def update(self):
        self.player.update()
        for object in self.objects:
            object.update()

    def render(self):
        self.screen.fill((0,0,0))
        self.player.draw(self.screen)
        for object in self.objects:
            object.render()
        pygame.display.update()

    def quit(self):
        print ("Exiting now")
        pygame.quit()


