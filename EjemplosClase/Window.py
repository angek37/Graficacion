import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Window(object):
    def display(self):
        pass
    def run(self, name, high, width, pos):
        glutInit([])
        glutCreateWindow(name)
        glutInitWindowSize(high, width)
        glutInitWindowPosition(pos, pos)
        glutDisplayFunc(self.display())

class window2(object):
    def display(self):
        pass

    def run(self, name, width, high):
        glutInit([])
        glutInitWindowSize(width, high)
        glutCreateWindow(name)
        glutDisplayFunc(self.display())
        glutMainLoop()

class Wanimation(object):
    def display(self):
        pass

    def AnimationStep(self):
        pass

    def run(self, name, width, high):
        glutInit([])
        glutInitWindowSize(width, high)
        glutCreateWindow(name)
        glutDisplayFunc(self.display())
        glutIdleFunc(self.AnimationStep())
        glutMainLoop()
