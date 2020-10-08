
#import moduales
import pygame

#init
pygame.init()
win_height = 250
win_width = 550

#set window
window = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Collition")



#player.colliderect(food):
class player:
    def __init__(self):
        self.posx = 100
        self.posy = 100
        self.dim = 10
        self.hitbox = pygame.Rect(self.posx,self.posy,self.dim,self.dim)


#create rectangle
food = pygame.Rect(200,100,10,10)
posx = 100
posy = 100

#create new player
ivan = player()


#game loop
while True:

    
    if ivan.hitbox.colliderect(food):
        print("Player is Collided")


    #move player 
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a]):
        posx -= 1
    if (keys[pygame.K_w]):
        posy -= 1
    if (keys[pygame.K_d]):
        posx += 1
    if (keys[pygame.K_s]):
        posy += 1


    ivan.hitbox = pygame.Rect(posx,posy,10,10)

    #update window
    window.fill((255,255,255))
    pygame.draw.rect(window, (0,0,0),ivan.hitbox)
    pygame.draw.rect(window, (0,0,0),food)


    #if user quits
    for event in pygame.event.get() : 
        if event.type == pygame.QUIT:
            pygame.quit() 


    #update window
    pygame.display.update() 
