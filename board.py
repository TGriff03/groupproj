import math
import pygame
import random

from settings import *


class Board:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))
        self.tile_size = TILESIZE
        self.width = math.sqrt(3) * self.tile_size
        self.height = 2 * self.tile_size
        self.tiles = []
        self.tiles += [CLAY, ORE] * 3
        self.tiles += [WHEAT, SHEEP, WOOD] * 4
        self.tiles += [SAND]
        random.shuffle(self.tiles)

    # draws the board
    def draw(self):
        v = []
        polygonv = []
        rows = [3, 4, 5, 4, 3]
        self.screen.fill(BGCOLOUR)
        x = 170
        y = 150
        count = 0

        for row in range(5):
            x_offset = 0

            if row == 2:
                x_offset -= self.width / 2

            elif row % 2 == 0:
                x_offset = self.width / 2

            # loops x times for number of hexagons in row
            for i in range(rows[row]):
                x += self.width
                centre = (round(x + x_offset), round(y))  # stores centre of a hexagon in a tuple
                vertices = []

                # calculate vertices from centre of a hexagon
                for j in range(6):
                    angle_deg = 60 * j - 30
                    angle_rad = math.pi / 180 * angle_deg
                    vert_x = centre[0] + self.tile_size * math.cos(angle_rad)
                    vert_y = centre[1] + self.tile_size * math.sin(angle_rad)
                    vertices.append([math.floor(vert_x), math.floor(vert_y)])
                    v.append((math.floor(vert_x), math.floor(vert_y)))

                polygonv.append(vertices)
                pygame.draw.polygon(self.screen, self.tiles[count], vertices)
                pygame.draw.polygon(self.screen, BLACK, vertices, 3)
                pygame.draw.circle(self.screen, BLACK, centre, 4, 4)
                count += 1

            y += self.height * 3/4
            x -= self.width * rows[row]  # resets x back to starting position

        # creates a list of unique tuples which represent coordinates of each vertex.
        # i.e. list of the coordinates for possible settlement locations.
        uniquev = []
        for vertex in v:
            if vertex not in uniquev:
                if (vertex[0]+1, vertex[1]) not in uniquev:
                    if (vertex[0]-1, vertex[1]) not in uniquev:
                        uniquev.append(vertex)

        # creating a dictionary with each unique vertex as keys and empty lists as values.
        location_materials = {}
        for vertex in uniquev:
            location_materials[vertex] = []

        # updating the lists for each vertex with the materials in hexagons adjacent to them.
        # materials currently stored as the colour of the hexagon rather than the material name.
        polynum = 0
        for polygon in polygonv:
            for vertex in uniquev:
                if vertex in polygon or (vertex[0] + 1, vertex[1]) in polygon or (vertex[0] - 1, vertex[1]) in polygon:
                        location_materials[vertex].append(self.tiles[polynum])
            polynum += 1

        print(len(uniquev))
        print(uniquev)
        print(len(location_materials))
        print(location_materials)


"""
        seen = set()
        duplicates = set()
        for coordinate_list in v:
            for coordinate in coordinate_list:
                tuple_coord = tuple(coordinate)
                if tuple_coord in seen:
                    duplicates.add(tuple_coord)
                else:
                    seen.add(tuple_coord)
        print(len(list(duplicates)))
"""








