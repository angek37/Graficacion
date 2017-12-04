from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class WanimationMouse(object):
    def display(self):
        pass
    def AnimationStep(self):
        pass

    def mouse(x,y):
        pass

    def run(self,name,width,high):
        glutInit([])
        glutInitWindowSize(width,high)
        glutCreateWindow(name)
        glutDisplayFunc(self.display())
        glutIdleFunc(self.AnimationStep)
        glutPassiveMotionFunc(self.mouse())
        glutMainLoop()

