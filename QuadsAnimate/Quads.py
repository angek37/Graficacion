import sys
from Window import Wanimation
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import numpy as np
from time import sleep

x = 0.0
y = 0.0
x1 = 0.25
y1 = 0.0
x2 = 0.0
y2 = 0.0

flag = 0
flag2 = 0

class Cuad(Wanimation):
    def AnimationStep(self):
        global y
        global x
        global y1
        global x1
        global x2
        global y2

        global flag
        global flag2

        frameRate = 50

        if y1 == y and x1 == x:
            flag = not flag

        if x < 0.95 and flag == 0:
            x += 0.01
            y = x
        else:
            flag = 1

        if x > -0.95 and flag == 1:
            x -= 0.01
            y = x
        else:
            flag = 0

        if y1 < 0.95 and flag == 0:      #Segundo cuadrito :)
            y1 += 0.01
        else:
            flag = 1

        if y1 > -0.95 and flag == 1:
            y1 -= 0.01
        else:
            flag = 0

        if x2 < 0.95 and flag2 == 0:
            x2 += 0.01
            y2 = x
        else:
            flag2 = 1

        if x2 > -0.95 and flag2 == 1:
            x2 -= 0.01
            y2 = x2
        else:
            flag2 = 0

        sleep(1 / float(frameRate))
        glutPostRedisplay()


    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glColor3f(1, 1, 0)
        glTranslatef(x, y, 1.0)
        glBegin(GL_QUADS)
        glVertex3f(-0.05, 0.05, 0)
        glVertex3f(-0.05, -0.05, 0)
        glVertex3f(0.05, -0.05, 0)
        glVertex3f(0.05, 0.05, 0)
        glEnd()
        glutSwapBuffers()

        glLoadIdentity()
        glColor3f(1, 1, 1)
        glTranslatef(x1, y1, 1.0)
        glBegin(GL_QUADS)
        glVertex3f(-0.05, 0.05, 0)
        glVertex3f(-0.05, -0.05, 0)
        glVertex3f(0.05, -0.05, 0)
        glVertex3f(0.05, 0.05, 0)
        glEnd()
        glutSwapBuffers()

        glLoadIdentity()
        glColor3f(1, 1, 1)
        glTranslatef(-x2, y2, 1.0)
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