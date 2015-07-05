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

	# Draw a Icosahedron
	X = 0.525731112119133606
	Y = 0.0
	Z = 0.850650808352039932 
	vdata = ((-X,Y,Z),(X,Y,Z),(-X,Y,-Z),(X,Y,-Z),\
		(Y,Z,X),(Y,Z,-X),(Y,-Z,X),(Y,-Z,-X),\
		(Z,X,Y),(-Z,X,Y),(Z,-X,Y),(-Z,-X,Y))
	tindices = ((1,4,0),(4,9,0),(4,9,5),(8,5,4),(1,8,4),\
		(1,10,8),(10,3,8),(8,3,5),(3,2,5),(3,7,2),\
		(3,10,7),(10,6,7),(6,11,7),(6,0,11),(6,1,0),\
		(10,1,6),(11,0,9),(2,11,9),(5,2,9),(11,2,7))

	glBegin(GL_TRIANGLES)
	for i in range(20):
		glVertex3f(vdata[tindices[i][0]][0],vdata[tindices[i][0]][1],vdata[tindices[i][0]][2])
		glVertex3f(vdata[tindices[i][1]][0],vdata[tindices[i][1]][1],vdata[tindices[i][1]][2])
		glVertex3f(vdata[tindices[i][2]][0],vdata[tindices[i][2]][1],vdata[tindices[i][2]][2])
	glEnd()

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
