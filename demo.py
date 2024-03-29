#codine=utf-8

import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0

def InitGL(Width,Height):
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glClearDepth(1.0)
	glDepthFunc(GL_LESS)
	glEnable(GL_DEPTH_TEST)
	glShadeModel(GL_SMOOTH)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
	glMatrixMode(GL_MODELVIEW)

def ReSizeGLScence(Width,Height):
	if Height == 0:
		Height = 1
	glViewport(0, 0, Width, Height)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
	glMatrixMode(GL_MODELVIEW)

# The main drawing function. 
def DrawGLScence():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()					# Reset The View 

	glTranslatef(0.0, 0.0, -6.0)

	# # Draw a triangle
	# glBegin(GL_POLYGON)                 # Start drawing a polygon
	# glVertex3f(0.0, 1.0, 0.0)           # Top
	# glVertex3f(1.0, -1.0, 0.0)          # Bottom Right
	# glVertex3f(-1.0, -1.0, 0.0)         # Bottom Left
	# glEnd() 

	glutWireCube(2.0)

	glutSwapBuffers()

def KeyPressed(*args):
	if args[0] == '\033':
		sys.exit()

def MousePressed(button, state, x, y):
	pass

def main():
	global window
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	glutInitWindowSize(640,480)
	glutInitWindowPosition(0,0)
	window = glutCreateWindow("demo")

	glutDisplayFunc(DrawGLScence)
	glutIdleFunc(DrawGLScence)

	glutReshapeFunc(ReSizeGLScence)
	glutKeyboardFunc(KeyPressed)
	glutMouseFunc(MousePressed)

	InitGL(640,480)

	glutMainLoop()

main()
