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
x1 = -0.05
y1 = 0.05
x2 = -0.05
y2 = -0.05
x3 = 0.05
y3 = -0.05
x4 = 0.05
y4 = 0.05
angle = 0.0

class Cuad(Wanimation):
    def AnimationStep(self):
        global y
        global x, angle
        frameRate = 5
        x = 0.8 * np.cos(angle)
        y = 0.8 * np.sin(angle)
        angle += 0.1
        sleep(1 / float(frameRate))
        glutPostRedisplay()

    def traslate(self, xt, yt):
        I = np.identity(4)
        v = np.matrix([[xt], [yt], [0], [1]])
        I[0][3] = x
        I[1][3] = y
        r = I * v
        xf = r.item(0)
        yf = r.item(1)
        return xf, yf

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glColor3f(1, 1, 1)
        #glTranslatef(x,y,1.0)
        global x1, y1, x2, y2, x3, y3, x4, y4
        glBegin(GL_QUADS)
        xf1, yf1 = self.traslate(x1, y1)
        glVertex3f(xf1, yf1, 0)
        xf2, yf2 = self.traslate(x2, y2)
        glVertex3f(xf2, yf2, 0)
        xf3, yf3 = self.traslate(x3, y3)
        glVertex3f(xf3, yf3, 0)
        xf4, yf4 = self.traslate(x4, y4)
        glVertex3f(xf4, yf4, 0)
        glEnd()
        glutSwapBuffers()

if __name__ == '__main__':
    win = Cuad()
    win.run('Cuad', 520, 520)