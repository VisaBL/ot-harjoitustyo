import pygame

class Snake(pygame.sprite.Sprite):
    def __init__(self, size, x_pos, y_pos, life):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([size,size])
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos,y_pos)
        self.life = life
       
    def update(self):
        self.life = self.life-1
        if self.life < 1:
            self.kill()






    
    
if __name__ == "__main__":
    pass
