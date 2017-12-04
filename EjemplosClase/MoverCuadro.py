import sys
sys.path.append('code/basic')
from Window import WanimationMouse
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

import numpy as np
from time import sleep

xf = 0.0
yf = 0.0
x1 = -0.05
y1 = 0.05
x2 = -0.05
y2 = -0.05
x3 = 0.05
y3 = -0.05
x4 = 0.05
y4 = 0.05
angle = 0.0
larg = 520
an = 520

class Cuad(WanimationMouse):
    def AnimationStep(self):
        frameRate = 5
        sleep(1/float(frameRate))
        glutPostRedisplay()

    def mouse(self,x,y):
        global xf, yf
        xf = (x-260.0)/260.0
        yf = (260.0-y)/260.0

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glColor3f(1,1,1)
        glTranslatef(xf,yf,1.0)
        global x1,y1,x2,y2,x3,y3,x4,y4
        glBegin(GL_QUADS)
        glVertex3f(x1, y1, 0)
        glEnd()
        glutSwapBuffers()

if __name__ == '__main__':
    win = Cuad()
    win.run('Cuad',520,520)