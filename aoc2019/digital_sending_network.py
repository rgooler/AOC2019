import sys
import logging

class DigitalSendingNetwork:
    data = ""
    width = 0
    height = 0
    layers = []

    def __init__(self, enable_logs=True):
        if enable_logs :
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(level=logging.CRITICAL)
        self.amplifiers = []

    def load(self, data):
        self.data = data
        self.layers = []

    def split_into_layers(self, width, height):
        res = width * height
        self.width = width
        self.height = height
        for offset in range(int(len(self.data)/res)):
            shard = self.data[(offset * res) + 0:(offset * res) + res ]
            self.layers.append(DSN_layer(width, height, shard))

    def least_zeros(self):
        m = 0xffffffff
        smallest = None
        for layer in self.layers:
            if layer.count[0] < m:
                smallest = layer
                m = layer.count[0]
        return smallest

    def render(self):
        shard = "9" * (self.width * self.height)
        out = DSN_layer(self.width, self.height, shard)
        for x in range(self.width):
            for y in range(self.height):
                color = self.get_pixel(x, y)
                out.set_pixel(x,y,color)
        return out

    def get_pixel(self, x, y):
        for layer in self.layers:
            color = int(layer.get_pixel(x,y))
            if color != 2:
                return color


class DSN_layer():
    width = 0
    height = 0
    data = []
    count = {0:0, 1:0, 2:0}

    def __init__(self, width, height, data):
        self.width = width
        self.height = height
        self.data = []
        for o in range(int(len(data)/width)):
            self.data.append(data[(o * width) + 0:(o * width) + width])
        
        data = sorted(data)
        self.count = {0:0, 1:0, 2:0}
        self.count[0] = data.count('0')
        self.count[1] = data.count('1')
        self.count[2] = data.count('2')

    def __str__(self):
        return str(self.data)

    def set_pixel(self, y, x, color):
        ##print(f"set_pixel({x},{y},{color})")
        s = list(self.data[x])
        ##print(f"~>{s}")
        s[y] = str(color)
        ##print(f"~>{s}")
        self.data[x] = ''.join(s)

    def get_pixel(self, y, x):
        try:
            return self.data[x][y]
        except:
            print(f"ERR: {x},{y}")
    
    def draw(self):
        for line in self.data:
            print(line.replace('0',' ').replace('1','*'))