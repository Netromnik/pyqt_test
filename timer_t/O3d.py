from OpenGL.raw.GLUT import glutPostRedisplay
from PyQt5.QtWidgets import QOpenGLWidget
from OpenGL.GL import *
class GLWidget(QOpenGLWidget):

    def resssizeGL(self, w, h):
        self._rot = self._rot + 12
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def initializeGL(self, parent=None):
        glClearColor(0, 0, 0, 1)
        glEnable(GL_DEPTH_TEST);
        glShadeModel(GL_FLAT);
        glEnable(GL_CULL_FACE);
        self._rot = [0] * 3

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        glLoadIdentity()
        glRotate(-self._rot[2],0,1,0)
        glRotate(self._rot[1],1,0,0)
        glRotate(-self._rot[0],0,0,1)

        self.box()

        glFlush()

    def box(self):
        #сторона - ЗАДНЯЯ
        glBegin(GL_POLYGON);
        glColor3f(1.0, 1.0, 1.0);
        glVertex3f(0.5, -0.1, 0.5);
        glVertex3f(0.5, 0.1, 0.5);
        glVertex3f(-0.5, 0.1, 0.5);
        glVertex3f(-0.5, -0.1, 0.5);
        glEnd();

        #сторона - ПРАВАЯ
        glBegin(GL_POLYGON);
        glColor3f(1.0, 0.0, 1.0);
        glVertex3f(0.5, -0.1, -0.5);
        glVertex3f(0.5, 0.1, -0.5);
        glVertex3f(0.5, 0.1, 0.5);
        glVertex3f(0.5, -0.1, 0.5);
        glEnd();

        #сторона - ЛЕВАЯ
        glBegin(GL_POLYGON);
        glColor3f(0.0, 1.0, 0.0);
        glVertex3f(-0.5, -0.1, 0.5);
        glVertex3f(-0.5, 0.1, 0.5);
        glVertex3f(-0.5, 0.1, -0.5);
        glVertex3f(-0.5, -0.1, -0.5);
        glEnd();

        #сторона - ВЕРХНЯЯ
        glBegin(GL_POLYGON);
        glColor3f(0.0, 0.0, 1.0);
        glVertex3f(0.5, 0.1, 0.5);
        glVertex3f(0.5, 0.1, -0.5);
        glVertex3f(-0.5, 0.1, -0.5);
        glVertex3f(-0.5, 0.1, 0.5);
        glEnd();

        #сторона - НИЖНЯЯ
        glBegin(GL_POLYGON);
        glColor3f(1.0, 0.0, 0.0);
        glVertex3f(0.5, -0.1, -0.5);
        glVertex3f(0.5, -0.1, 0.5);
        glVertex3f(-0.5, -0.1, 0.5);
        glVertex3f(-0.5, -0.1, -0.5);
        glEnd();

    def setXRotation(self, angle):
        angle = self.normalizeAngle(angle)
        self._rot[0]= angle

    def setYRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self._rot[1]:
            self._rot[1]= angle

    def setZRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self._rot[2]:
            self._rot[2] = angle

    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle


    def update(self):
        QOpenGLWidget.update(self)