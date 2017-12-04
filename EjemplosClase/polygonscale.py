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


class Cuad(Wanimation):
    def AnimationStep(self):
        global y
        global x
        frameRate = 10
        x += 0.01
        y = x
        sleep(1 / float(frameRate))
        glutPostRedisplay()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glColor3f(1, 1, 1)
        glTranslatef(x, y, 1.0)
        theta=np.range (0,2*np.pi,0.01)
        glBegin(GL_POLYGON)
        for i in theta:
            glvertex2f,0.5*np.cos(1),0.5*np.sin(i)
        glEnd( )
        glutSwapBuffers()


if __name__ == '__main__':
    win = Cuad()
win.run('Cuad', 520, 520)