# importing required libraries
import random
import pygame
import os
import pygame_widgets
from NextButton import NextButton

def openImage():
    image_path = 'questions/'
    # get random image
    image_file = random.choice(images)
    
    # create the display surface object
    # of specific dimension..e(X, Y).
    scrn = pygame.display.set_mode((700, 700))

    # set the pygame window name
    pygame.display.set_caption('question')

    # create a surface object, image is drawn on it.
    imp = pygame.image.load(image_path + image_file).convert()

    # Using blit to copy content from one surface to other
    scrn.blit(imp, (0, 0))

    # paint screen one time
    pygame.display.flip()
    status = True
    while (status):

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
        for i in pygame.event.get():

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if i.type == pygame.QUIT:
                status = False
    
    # remove the used image from the list
    images.remove(image_file)

# activate the pygame library .
pygame.init()

# pull list of question images
images = os.listdir('questions')

scrn = pygame.display.set_mode((600, 600))
font = pygame.font.SysFont("Arial", 36)

run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()
    
    scrn.fill((0, 159, 181))

    if len(images) > 0:
        btn = NextButton(scrn, openImage)
    else:
        btn = None
        txt = font.render("No more questions", True, (0,0,0))
        scrn.blit(txt, (300 - txt.get_width() // 2, 280 - txt.get_height() // 2)) 

    pygame_widgets.update(events)  # Call once every loop to allow widgets to render and listen
    pygame.display.update()

# deactivates the pygame library
pygame.quit()