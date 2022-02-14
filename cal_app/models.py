from django.db import models
from math import pi, sqrt, tan, cos, sin
import io
import urllib, base64
from random import choice
import matplotlib.pylab as plt
from matplotlib.patches import Rectangle, Polygon

import numpy as np
from itertools import combinations


class Shape(models.Model):
    a = models.FloatField()

    class Meta:
        abstract = True

    def area(self):
        pass

    @classmethod
    def get_png(cls, fig):
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        return uri

    @staticmethod
    def get_color():
        color = ['b', 'g', 'r', 'b']
        return choice(color)

    def draw_shape(self):
        pass


class Square(Shape):

    def area(self):
        return round(self.a ** 2, 2)

    def perimeter(self):
        return round(self.a * 4, 2)

    def draw_shape(self):
        fig, ax = plt.subplots()
        ax.plot([0])
        square = Rectangle((0, 0), self.a, self.a, fill=False, color=self.get_color())
        ax.add_patch(square)

        return fig

    def diagonal(self):
        return round(sqrt(2) * self.a, 2)


class RectangleShape(Shape):
    b = models.FloatField()

    def area(self):
        return round(self.a * self.b, 2)

    def perimeter(self):
        return round((2 * (self.a + self.b)), 2)

    def draw_shape(self):
        fig, ax = plt.subplots()
        ax.plot([0])
        rect = Rectangle((0, 0), self.b, self.a, fill=False, color=self.get_color())
        ax.add_patch(rect)

        return fig

    def diagonal(self):
        return round(sqrt(self.a ** 2 + self.b ** 2), 2)


class CircleShape(Shape):

    def area(self):
        return round((pi * self.a ** 2), 2)

    def perimeter(self):
        return round((2 * self.a * pi), 2)

    def draw_shape(self):
        fig, ax = plt.subplots()
        ax.plot([0])
        circ = plt.Circle((0, 0), self.a, fill=False, color=self.get_color())
        ax.add_patch(circ)
        return fig


class Rhombus(RectangleShape):

    def perimeter(self):
        return round(self.a * 4, 2)

    def draw_shape(self):
        fig, ax = plt.subplots()
        ax.plot([0])
        h = sqrt(self.a ** 2 - self.b ** 2)
        x = [0, self.a, self.a + h, h]
        y = [0, 0, self.b, self.b]

        shape = Polygon(xy=list(zip(x, y)), fill=False, color=self.get_color())
        ax.add_patch(shape)

        return fig


class Triangle(RectangleShape):
    c = models.FloatField()

    def perimeter(self):
        return round(self.a + self.b + self.c, 2)

    def area(self):
        p = self.perimeter() / 2
        return round(sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 2)

    def height(self):
        p = self.perimeter() / 2
        return round(2 * sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)) / self.c, 2)

    def draw_shape(self):
        h = self.height()
        n = sqrt(self.b ** 2 - h ** 2)
        m = self.c - n
        x = [0, self.c, m]
        y = [0, 0, h]

        fig, ax = plt.subplots()
        ax.plot([0])
        shape = Polygon(xy=list(zip(x, y)), fill=False, color=self.get_color())
        ax.add_patch(shape)

        return fig


class Trapezoid(Triangle):
    d = models.FloatField()

    def perimeter(self):
        return round(self.a + self.b + self.c + self.d, 2)

    def area(self):
        x = (self.b + self.d) / 2
        y = (self.d - self.b) ** 2 + self.a ** 2 - self.c ** 2
        z = 2 * (self.d - self.b)
        return round(x * sqrt(self.a ** 2 - (y / z) ** 2), 2)

    def height(self):
        return round(2 * self.area() / (self.b + self.d), 2)

    def middle_line(self):
        return round((self.d + self.b) / 2, 2)

    def draw_shape(self):
        h = self.height()
        g = sqrt(self.a ** 2 - h ** 2)
        x = [0, self.d, self.b + g, g]
        y = [0, 0, h, h]

        fig, ax = plt.subplots()
        ax.plot([0])
        shape = Polygon(xy=list(zip(x, y)), fill=False, color=self.get_color())
        ax.add_patch(shape)

        return fig


class Sphere(CircleShape):
    def area(self):
        return round(4 * pi * self.a ** 2, 2)

    def volume(self):
        return round(4 / 3 * pi * self.a ** 3, 2)

    def draw_shape(self):
        r = self.a
        u = np.linspace(0, 3 * np.pi, 50)
        v = np.linspace(0, np.pi, 50)
        x = r * np.outer(np.cos(u), np.sin(v))
        y = r * np.outer(np.sin(u), np.sin(v))
        z = r * np.outer(np.ones(np.size(u)), np.cos(v))
        fig = plt.figure(figsize=(6, 6))
        ax = plt.axes(projection='3d')
        ax.plot_wireframe(x, y, z, alpha=0.5, color=self.get_color())

        return fig


class Cube(Shape):
    def area(self):
        return round(6 * self.a ** 2, 2)

    def volume(self):
        return round(self.a ** 3, 2)

    def perimeter(self):
        return round(12 * self.a, 2)

    def draw_shape(self):
        axes = [int(self.a), int(self.a), int(self.a)]
        data = np.ones(axes, dtype=np.bool)
        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.voxels(data, color=(1, 1, 1, .75), edgecolor=self.get_color())

        return fig


class Cylinder(Sphere):
    b = models.FloatField()

    def area(self):
        return round(2 * pi * self.a * (self.a + self.b), 2)

    def volume(self):
        return round(pi * self.b * self.a ** 2, 2)

    def draw_shape(self):
        r = self.a
        h = self.b
        u = np.linspace(0, 2 * np.pi, 50)
        v = np.linspace(0, h, 50)
        theta, z = np.meshgrid(u, v)
        x = r * np.cos(theta)
        y = r * np.sin(theta)

        fig = plt.figure(figsize=(6, 6))
        ax = plt.axes(projection='3d')

        ax.plot_wireframe(x, y, z, alpha=0.5, color=self.get_color())
        return fig


class Parallelepiped(Cylinder):
    c = models.FloatField()

    def area(self):
        return round(2 * (self.a * self.b + self.b * self.c + self.a * self.c), 2)

    def volume(self):
        return round(self.b * self.a * self.c, 2)

    def draw_shape(self):
        axes = [int(self.a), int(self.b), int(self.c)]

        data = np.ones(axes, dtype=np.bool)
        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(111, projection='3d')

        ax.voxels(data, color=(1, 1, 1, .75), edgecolor=self.get_color())
        return fig

    def perimeter(self):
        return round(4 * (self.a + self.b + self.c), 2)


class Pyramid(Parallelepiped):

    def area(self):
        x = self.a / (2 * tan(pi / self.b))
        y = self.b * self.a / 2
        return round(y * (x + sqrt(self.c ** 2 + x ** 2)), 2)

    def volume(self):
        x = self.c * self.a ** 2 * self.b
        y = 12 * tan(pi / self.b)
        return round(x / y, 2)

    def apothem(self):
        x = self.a / (2 * tan(pi / self.b))
        return round(sqrt(self.c ** 2 + x ** 2), 2)

    def draw_shape(self):
        fig = plt.figure(figsize=(7, 7))
        ax = fig.add_subplot(111, projection='3d')

        angle = sin(pi / self.b)
        r = self.a / (2 * angle)
        n = int(self.b)
        x1 = [r * cos(2 * pi * i / n) if i != n else 0 for i in range(n + 1)]
        y1 = [r * sin(2 * pi * i / n) if i != n else 0 for i in range(n + 1)]
        z1 = [n if i == n else 0 for i in range(n + 1)]
        xyz = list(zip(x1, y1, z1))

        lines = combinations(xyz, 2)
        for x in lines:
            line = np.transpose(np.array(x))
            ax.plot3D(line[0], line[1], line[2], c='0')

        return fig


class Cone(Cylinder):
    def area(self):
        return round(pi * self.a * (sqrt(self.a ** 2 + self.b ** 2) + self.a), 2)

    def volume(self):
        return round(1 / 3 * pi * self.b * self.a ** 2, 2)

    def draw_shape(self):
        r = self.a
        h = self.b
        u = np.linspace(0, 2 * np.pi, 50)
        v = np.linspace(0, h, 50)
        theta, z = np.meshgrid(u, v)
        x = r * np.cos(theta) / h * z
        y = r * np.sin(theta) / h * z

        fig = plt.figure(figsize=(6, 6))
        ax = plt.axes(projection='3d')

        ax.plot_wireframe(x, y, z, alpha=0.5, color=self.get_color())
        ax.invert_zaxis()
        return fig

    def apothem(self):
        return round(sqrt(self.a ** 2 + self.b ** 2), 2)