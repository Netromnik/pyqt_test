"""
#include <Qt3DCore/QEntity>
#include <Qt3DRender/QCamera>
#include <Qt3DRender/QCameraLens>
#include <Qt3DCore/QTransform>
#include <Qt3DCore/QAspectEngine>

#include <Qt3DInput/QInputAspect>

#include <Qt3DRender/QRenderAspect>
#include <Qt3DExtras/QForwardRenderer>
#include <Qt3DExtras/QPhongMaterial>
#include <Qt3DExtras/QCylinderMesh>
#include <Qt3DExtras/QSphereMesh>
#include <Qt3DExtras/QTorusMesh>
"""
from PyQt5.Qt3DCore import QEntity,QTransform,QAspectEngine
from PyQt5.Qt3DRender import QCamera,QCameraLens
from PyQt5.Qt3DInput import QInputAspect
from PyQt5.Qt3DExtras import QForwardRenderer ,QPhongMaterial ,QCylinderMesh,QSphereMesh,QTorusMesh

from PyQt5.QtCore import (pyqtProperty, QEasingCurve, QObject, QPoint, QPointF,
        QPropertyAnimation, QRect, QRectF, QSize, Qt)
from PyQt5.QtGui import (QBrush, QColor, QIcon, QLinearGradient, QPainter,
        QPainterPath, QPixmap)
from PyQt5.QtWidgets import (QApplication, QGraphicsPixmapItem, QGraphicsScene,
        QListWidgetItem, QWidget)
"""""
{
    QGuiApplication app(argc, argv);
    Qt3DExtras::Qt3DWindow view;

    Qt3DCore::QEntity *scene = createScene();

    // Camera
    Qt3DRender::QCamera *camera = view.camera();
    camera->lens()->setPerspectiveProjection(45.0f, 16.0f/9.0f, 0.1f, 1000.0f);
    camera->setPosition(QVector3D(0, 0, 40.0f));
    camera->setViewCenter(QVector3D(0, 0, 0));

    // For camera controls
    Qt3DExtras::QOrbitCameraController *camController = new Qt3DExtras::QOrbitCameraController(scene);
    camController->setLinearSpeed( 50.0f );
    camController->setLookSpeed( 180.0f );
    camController->setCamera(camera);

    view.setRootEntity(scene);
    view.show();

    return app.exec();
}
"""
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
     view=Qt3DWindow()
    w = Window()
    w.resize(400, 400)
    w.show()
    sys.exit(app.exec_())