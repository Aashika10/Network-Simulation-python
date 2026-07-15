import pygame


class Renderer:

    def __init__(self, screen):

        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 18)

    def render(self, simulation):

        self.screen.fill((255, 255, 255))

        self.draw_grid()

        self.draw_links(simulation)

        self.draw_nodes(simulation)

        self.draw_signals(simulation)

    def draw_grid(self):

        width = self.screen.get_width()
        height = self.screen.get_height()

        spacing = 40

        for x in range(0, width, spacing):
            pygame.draw.line(
                self.screen,
                (230, 230, 230),
                (x, 0),
                (x, height)
            )

        for y in range(0, height, spacing):
            pygame.draw.line(
                self.screen,
                (230, 230, 230),
                (0, y),
                (width, y)
            )

    def draw_links(self, simulation):

        for link in simulation.links:
            # print(link)
            pygame.draw.line(
                    self.screen,
                    (80, 80, 80),
                    (link.node1.x, link.node1.y),
                    (link.node2.x, link.node2.y),
                    5
                )

    def draw_nodes(self, simulation):

        for node in simulation.nodes:

            pygame.draw.circle(
                self.screen,
                (0, 102, 255),
                (int(node.x), int(node.y)),
                25
            )

            text = self.font.render(
                node.name,
                True,
                (0, 0, 0)
            )

            self.screen.blit(
                text,
                (node.x - 8, node.y - 45)
            )

    def draw_signals(self, simulation):

        for signal in simulation.signals:
                # print(signal)
                pygame.draw.circle(
                    self.screen,
                    (255, 0, 0),
                    (int(signal.x), int(signal.y)),
                    6
                )
        
                text = self.font.render(
                    str(signal.waveform.voltage),
                    True,
                    (0, 0, 0)
                )

                self.screen.blit(
                    text,
                    (signal.x + 10, signal.y - 10)
                )