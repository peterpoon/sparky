import os
import time
import pygame

class Head(object):

    os.environ["DISPLAY"] = ":0"
    pygame.init()

    def __init__(self):
        print("Head process started")
        
        # Initialize head screen
        self. screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN or pygame.SCALED)
        # Hide mouse
        pygame.mouse.set_visible(False)
        # Start head loop
        self.main()

    def main(self):
        running = True
        while running:
            #RGB Background
            self.screen.fill((255, 0, 0))
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Stop loop when QUIT signal received
                    running = False

            pygame.display.update()
            time.sleep(1.0)
            print("Head loop...")

if __name__ == "__main__":
    Head()