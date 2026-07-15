from network.network import Network
from network.node import Node
import pygame
from simulation_clock import SimulationClock


class Simulation:

    def __init__(self):

        self.clock = pygame.time.Clock()
        self.simulation_clock = SimulationClock()
        self.network = Network()
        self.network.clock = self.simulation_clock
        
        A = Node("A", 100, 300)
        B = Node("B", 450, 120)
        C = Node("C", 800, 300)

        self.network.add_node(A)
        self.network.add_node(B)
        self.network.add_node(C)

        self.network.connect(A, B)
        self.network.connect(B, C)
        self.network.connect(A, C)


    def start_demo(self):
        self.network.nodes[0].send("00001111")
        # self.network.nodes[1].send("01010101")
       

    def update(self):
        delta_time = self.clock.tick(60) / 1000.0

        self.simulation_clock.update(delta_time)

        self.network.update()