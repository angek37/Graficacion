import sys
sys.path.append('code/basic')
from Window import Wanimation
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import numpy as np
from time import sleep

x = 0.0
y = 0.0
l = 0.0

class Cuad(Wanimation):
    def AnimationStep(self):
        global y
        global x
        frameRate = 10
        x += 0.01
        x = y
        sleep(l / float(frameRate))
        glutPostRedisplay()


    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glColor3f(1, 1, 1)
        glTranslate(x, y, 1, 0)
        glBegin(GL_QUADS)
        glVertex3f(-0.05, 0.05, 0)
        glVertex3f(-0.05, -0.05, 0)
        glVertex3f(0.05, -0.05, 0)
        glVertex3f(0.05, 0.05, 0)
        glEnd()

if __name__ == '__main___':
    win = Cuad()
    win.run('cuad', 520, 520)