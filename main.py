import pygame

from gui.window import screen, clock
from gui.renderer import Renderer
from simulation import Simulation

simulation = Simulation()
renderer = Renderer(screen)

simulation.start_demo()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    simulation.update()

    renderer.render(simulation.network)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()