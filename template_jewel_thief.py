import pygame
import sys

class Hurdle:
    def __init__(self, x, y, h, w):
        self.rect = pygame.Rect(x, y, h, w)
    
    def draw_hurdle(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)
    
    def paste_image(self, image):
        screen.blit(image, (self.rect.x, self.rect.y-14))

class Thief:
    def __init__(self, x, y, h, w):
        self.rect = pygame.Rect(x, y, h, w)
    
    def draw_thief(self, surface):
        pygame.draw.rect(surface, (109,23,230), self.rect)
    
    def paste_image(self, image):
        screen.blit(image, self.rect)
        
pygame.init()
screen = pygame.display.set_mode((400, 400))
font = pygame.font.Font("freesansbold.ttf", 16)

hurdle_1 = Hurdle(0, 200, 200, 2)
hurdle_2 = Hurdle(200, 198, 200, 2)
hurdle_change = 1

hurdle_img = pygame.image.load("hurdle.png")
hurdle_img = pygame.transform.scale(hurdle_img, (200,25))

thief = Thief(10, 380, 15, 15)
thief_x_change = 0
thief_y_change = 0

jewel = pygame.Rect(350, 10, 40, 40)
jewel_image = pygame.image.load("jewel.png")
jewel_image = pygame.transform.scale(jewel_image, (50,50))

while True:
    screen.fill((100,255,255))
    # Checking if 'quit' event occurs and handle it by calling 'pygame.quit()'
    
    
    
        if event.type == pygame.KEYDOWN:
                # Check if left arrow key is pressed
                
                    # Make 'thief_x_change' value to -1
                # Check if right arrow key is pressed    
                
                    # Make 'thief_x_change' value to 1 
                # Check if down arrow key is pressed   
                
                    # Make 'thief_y_change' value to 1
                # Check if up arrow key is pressed    
                
                    # Make 'thief_y_change' value to -1
                 
        if event.type == pygame.KEYUP:
            thief_x_change = 0
            thief_y_change = 0
                    
    # Update the x,y values of the thief
    # Increment 'thief.rect.x' with the 'thief_x_change' value
    
    # Increment 'thief.rect.y' with the 'thief_y_change' value
    
    
    if hurdle_1.rect.y > 398:
        hurdle_change = -1
    elif hurdle_1.rect.y < 0:
        hurdle_change = 1
    
    hurdle_1.rect.y += hurdle_change
    hurdle_2.rect.y -= hurdle_change
    
    hurdle_1.paste_image(hurdle_img)
    hurdle_2.paste_image(hurdle_img)
    thief.draw_thief(screen)
    screen.blit(jewel_image, jewel)
    
    # Check if 'hurdle_1.rect' or 'hurdle_2.rect' collides with 'thief.rect' 
    # Use 'or' to combine the 2 conditions
    
        text = font.render("Failed, you lost", True, (0,0,0))
        screen.blit(text, (125,175))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
    
    # Check if 'thief.rect' collides with 'jewel'
    
        text = font.render("Congratulations, you won", True, (0,0,0))
        screen.blit(text, (125,175))
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
    
    pygame.display.update()
    pygame.time.delay(10)
