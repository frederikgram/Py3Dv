import pygame
import sys
import math

# Initialize pygame

pygame.init()
w, h = 400, 400
screen = pygame.display.set_mode((w, h))



def load_obj(path_to_obj):
    """ Returns a list of vertices from a given .obj file """

    with open(path_to_obj, 'r') as f:
        lines = [line for line in f.readlines() if '#' not in line]
        vertices = [line.split()[1:4] for line in lines if line[0] == 'v']

    return vertices


def find_edges(vertices):
    """ Returns a list of edges in a given list of vertices """
    edges = []
    return edges


if __name__ == "__main__":
    """ Py3Dv startup script """

    obj = load_obj("./test.obj")