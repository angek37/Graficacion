import sys
from Window import Wanimation
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import numpy as np
from time import sleep

x = 0.0
y = 0.0
flag = 0

class Cuad(Wanimation):
    def AnimationStep(self):
        global y
        global x
        global flag
        frameRate = 50

        if x < 1 and flag == 0:
            x += 0.01
            y = x
        else:
            flag = 1

        if x > -1 and flag == 1:
            x -= 0.01
            y = x
        else:
            flag = 0

        sleep(1 / float(frameRate))
        glutPostRedisplay( )


    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glColor3f(1, 1, 1)
        glTranslatef(x, y, 1.0)
        glBegin(GL_QUADS)
        glVertex3f(-0.05, 0.05, 0)
        glVertex3f(-0.05, -0.05, 0)
        glVertex3f(0.05, -0.05, 0)
        glVertex3f(0.05, 0.05, 0)
        glEnd()
        glutSwapBuffers()

if __name__ == '__main__':
	win = Cuad()
	win.run('Cuad' ,520,520)