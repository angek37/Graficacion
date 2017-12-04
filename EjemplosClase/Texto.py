import sys
sys.path.append('code/basic')
from Window import Wanimation
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np
from time import sleep

x = 0
y = 0

class Text(Wanimation):
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
        glColor3f(1,1,1)
        glTranslatef(x,y,1.0)
        text = 'Hola OpenGL'
        glRasterPos2f(0, 0)
        for i in range(0,len(text)):
            glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(text[i]))
        glutSwapBuffers()

if __name__ == '__main__':
    win = Text()
    win.run('Text',520,520)
