#!/usr/bin/env python 

from graph_tool.all import *

class challenge:
    data = []

    def load(self, data):
        data = [x.strip() for x in data]
        # Create a new undirectedgraph
        self.graph = Graph(directed=False)

        # Label everything so I'm not going back and forth between hashes
        v_name = self.graph.new_vertex_property('string')
        self.graph.vertex_properties["name"] = v_name

        self.planets = dict()
        # Create all the vertexes first, so that creating the edges (orbits)
        # is easier 
        for item in data:
            # Add vertexes, as needed
            src, dest = item.split(")")
            if src not in self.planets:
                v_src = self.graph.add_vertex()
                v_name[v_src] = src
                self.planets[src] = v_src
            if dest not in self.planets:
                v_dest = self.graph.add_vertex()
                v_name[v_dest] = dest
                self.planets[dest] = v_dest
            # Add edge
            self.graph.add_edge(self.planets[src],self.planets[dest])
               
    def part1(self):
        total = 0
        for planet in self.planets:
            total += self.to_COM(planet)
        return total

    def part2(self):
        return self.calc_distance('YOU', 'SAN')

    def to_COM(self, src):
        return self.calc_distance(src, 'COM') - 2

    def calc_distance(self, src, dest):
        return shortest_distance(
            self.graph,
            self.planets[src],
            self.planets[dest]
            )

def main():
    chall = challenge()
    with open('input') as fh:
        lines = fh.readlines()
        chall.load(lines)
    print(f"Part 1: {chall.part1()}")
    print(f"Part 1: {chall.part2()}")

if __name__ == "__main__":
    main()