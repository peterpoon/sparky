import os
import time
from xml.etree.ElementTree import PI
import pygame

# Colors definition
BACKGROUND_DARK_BLUE = (0, 8, 24)
LIGHT_BLUE = (222, 235, 247)
BLUE = (91, 155, 213)

class Head(object):

    os.environ["DISPLAY"] = ":0"
    pygame.init()

    def __init__(self):
        print("Head process started")
        
        # Initialize head screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN or pygame.SCALED)
        
        # Hide mouse
        pygame.mouse.set_visible(False)

        #RGB Background
        self.screen.fill(BACKGROUND_DARK_BLUE)

        # Start head loop
        self.run()

    def run(self):
        running = True
        while running:   
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Stop loop when QUIT signal received
                    running = False
                    
            #pygame.draw.circle(self.screen, BLUE, (400, 240), 30)
            #pygame.draw.circle(self.screen, LIGHT_BLUE, (400, 240), 20)
            
            pygame.draw.rect(self.screen, BLUE, pygame.Rect(110, 40, 580, 400), 10, border_radius=75)
            pygame.draw.circle(self.screen, BLUE, (290, 150), 40)
            pygame.draw.circle(self.screen, BLUE, (510, 150), 40)
            pygame.draw.circle(self.screen, LIGHT_BLUE, (290, 150), 20)
            pygame.draw.circle(self.screen, LIGHT_BLUE, (510, 150), 20)
            pygame.draw.circle(self.screen, BLUE, (110, 240), 80, draw_top_left=True, draw_bottom_left=True)
            pygame.draw.circle(self.screen, BLUE, (690, 240), 80, draw_top_right=True, draw_bottom_right=True)
            self.draw_outlined_circle(self.screen, BLUE, (400, 280), 100, 10)
            pygame.draw.rect(self.screen, (0, 8, 24), pygame.Rect(250, 200, 300, 130))


            pygame.display.update()
            time.sleep(1.0)
            #print("Head loop...")
    
    def draw_outlined_circle(self, surf, color, origin, radius, thickness):
        width = radius * 2 + thickness * 2
        background = (0, 0, 0, 0)
        circle = pygame.Surface((width, width)).convert_alpha()
        rect = circle.get_rect()
        circle.fill(background)
        pygame.draw.circle(circle, color, rect.center, radius, draw_bottom_left=True, draw_bottom_right=True)
        pygame.draw.circle(circle, background, rect.center, radius - thickness, draw_bottom_left=True, draw_bottom_right=True)
        surf.blit(circle, (origin[0] - (rect.w / 2), origin[1] - (rect.w / 2)))

if __name__ == "__main__":
    Head()