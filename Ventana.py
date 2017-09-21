import OpenGL
import Funcion

OpenGL.ERROR_ON_COPY = True

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

points = Funcion.P

def init2D(r, g, b):
    glClearColor(r, g, b, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0.0, 200.0, 0.0, 150.0)


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(255.0, 255.0, 255.0)

    # draw two points
    glBegin(GL_POINTS)
    print("Puntos (x, y)")
    for i in range(0, len(points)):
        print(int((points[i][0])), int((points[i][1])))
        glVertex2i(int((points[i][0])), int((points[i][1])))
    glEnd()

    # draw a line
    # glBegin(GL_LINES)
    # glVertex2i(0, 0)
    # glVertex2i(500, 250)
    # glEnd()

    glFlush()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow('Grafica')
init2D(0.0, 0.0, 0.0)
glutDisplayFunc(display)
glutMainLoop()


