# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTextEdit, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1500, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_camara = QFrame(self.centralwidget)
        self.frame_camara.setObjectName(u"frame_camara")
        self.frame_camara.setGeometry(QRect(300, 0, 900, 500))
        self.frame_camara.setStyleSheet(u"QFrame {\n"
"    background-color: #001233;\n"
"    border: 1px solid #CBD2D9;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_camara.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_camara.setFrameShadow(QFrame.Shadow.Raised)
        self.video = QLabel(self.frame_camara)
        self.video.setObjectName(u"video")
        self.video.setEnabled(True)
        self.video.setGeometry(QRect(0, 0, 900, 500))
        self.captura = QPushButton(self.frame_camara)
        self.captura.setObjectName(u"captura")
        self.captura.setGeometry(QRect(820, 180, 50, 50))
        self.captura.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon = QIcon()
        icon.addFile(u"fotos iconos/camara_foto.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.captura.setIcon(icon)
        self.captura.setIconSize(QSize(50, 50))
        self.grabar = QPushButton(self.frame_camara)
        self.grabar.setObjectName(u"grabar")
        self.grabar.setGeometry(QRect(820, 250, 50, 50))
        self.grabar.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"fotos iconos/camara_grabar.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.grabar.setIcon(icon1)
        self.grabar.setIconSize(QSize(50, 50))
        self.frame_opciones = QFrame(self.centralwidget)
        self.frame_opciones.setObjectName(u"frame_opciones")
        self.frame_opciones.setEnabled(True)
        self.frame_opciones.setGeometry(QRect(0, 0, 300, 480))
        self.frame_opciones.setStyleSheet(u"QFrame {\n"
"    background-color: #023047;\n"
"    border: 1px solid #CBD2D9;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_opciones.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_opciones.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_5 = QFrame(self.frame_opciones)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 0, 300, 80))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.movimiento = QPushButton(self.frame_5)
        self.movimiento.setObjectName(u"movimiento")
        self.movimiento.setGeometry(QRect(50, 15, 200, 50))
        self.movimiento.setStyleSheet(u"QPushButton {\n"
"    background-color: #eff7f6;      /* fondo claro del bot\u00f3n */\n"
"    color: #1A1A1A;                 /* color del texto del bot\u00f3n */\n"
"    border: 1px solid #CBD2D9;      /* borde suave gris */\n"
"    border-radius: 6px;             /* esquinas redondeadas */\n"
"    padding: 6px 12px;              /* espacio interno */\n"
"    font-family: \"Arial\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"fotos iconos/movimiento.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.movimiento.setIcon(icon2)
        self.movimiento.setIconSize(QSize(50, 50))
        self.frame_6 = QFrame(self.frame_opciones)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 80, 300, 80))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.configuracion = QPushButton(self.frame_6)
        self.configuracion.setObjectName(u"configuracion")
        self.configuracion.setGeometry(QRect(50, 15, 200, 50))
        self.configuracion.setStyleSheet(u"QPushButton {\n"
"    background-color: #eff7f6;      /* fondo claro del bot\u00f3n */\n"
"    color: #1A1A1A;                 /* color del texto del bot\u00f3n */\n"
"    border: 1px solid #CBD2D9;      /* borde suave gris */\n"
"    border-radius: 6px;             /* esquinas redondeadas */\n"
"    padding: 6px 12px;              /* espacio interno */\n"
"    font-family: \"Arial\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"fotos iconos/configuracion.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.configuracion.setIcon(icon3)
        self.configuracion.setIconSize(QSize(50, 50))
        self.frame_7 = QFrame(self.frame_opciones)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 160, 300, 80))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.camaras = QPushButton(self.frame_7)
        self.camaras.setObjectName(u"camaras")
        self.camaras.setGeometry(QRect(50, 15, 200, 50))
        self.camaras.setStyleSheet(u"QPushButton {\n"
"    background-color: #eff7f6;      /* fondo claro del bot\u00f3n */\n"
"    color: #1A1A1A;                 /* color del texto del bot\u00f3n */\n"
"    border: 1px solid #CBD2D9;      /* borde suave gris */\n"
"    border-radius: 6px;             /* esquinas redondeadas */\n"
"    padding: 6px 12px;              /* espacio interno */\n"
"    font-family: \"Arial\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"fotos iconos/camara.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.camaras.setIcon(icon4)
        self.camaras.setIconSize(QSize(50, 50))
        self.frame_8 = QFrame(self.frame_opciones)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 240, 300, 80))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.calibracion = QPushButton(self.frame_8)
        self.calibracion.setObjectName(u"calibracion")
        self.calibracion.setGeometry(QRect(50, 15, 200, 50))
        self.calibracion.setStyleSheet(u"QPushButton {\n"
"    background-color: #eff7f6;      /* fondo claro del bot\u00f3n */\n"
"    color: #1A1A1A;                 /* color del texto del bot\u00f3n */\n"
"    border: 1px solid #CBD2D9;      /* borde suave gris */\n"
"    border-radius: 6px;             /* esquinas redondeadas */\n"
"    padding: 6px 12px;              /* espacio interno */\n"
"    font-family: \"Arial\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"fotos iconos/calibracion.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.calibracion.setIcon(icon5)
        self.calibracion.setIconSize(QSize(50, 50))
        self.frame_9 = QFrame(self.frame_opciones)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 320, 300, 80))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.conexion = QPushButton(self.frame_9)
        self.conexion.setObjectName(u"conexion")
        self.conexion.setGeometry(QRect(50, 15, 200, 50))
        self.conexion.setStyleSheet(u"QPushButton {\n"
"    background-color: #eff7f6;      /* fondo claro del bot\u00f3n */\n"
"    color: #1A1A1A;                 /* color del texto del bot\u00f3n */\n"
"    border: 1px solid #CBD2D9;      /* borde suave gris */\n"
"    border-radius: 6px;             /* esquinas redondeadas */\n"
"    padding: 6px 12px;              /* espacio interno */\n"
"    font-family: \"Arial\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"fotos iconos/conexion.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.conexion.setIcon(icon6)
        self.conexion.setIconSize(QSize(50, 50))
        self.frame_10 = QFrame(self.frame_opciones)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(0, 400, 300, 80))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.exportar = QPushButton(self.frame_10)
        self.exportar.setObjectName(u"exportar")
        self.exportar.setGeometry(QRect(50, 15, 200, 50))
        self.exportar.setStyleSheet(u"QPushButton {\n"
"    background-color: #eff7f6;      /* fondo claro del bot\u00f3n */\n"
"    color: #1A1A1A;                 /* color del texto del bot\u00f3n */\n"
"    border: 1px solid #CBD2D9;      /* borde suave gris */\n"
"    border-radius: 6px;             /* esquinas redondeadas */\n"
"    padding: 6px 12px;              /* espacio interno */\n"
"    font-family: \"Arial\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"fotos iconos/exportar.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exportar.setIcon(icon7)
        self.exportar.setIconSize(QSize(50, 50))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(1200, 0, 300, 180))
        self.frame.setStyleSheet(u"QFrame {\n"
"    background-color: #33415c;\n"
"    border: 1px solid #CBD2D9;\n"
"    border-radius: 6px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.ultima_captura = QLabel(self.frame)
        self.ultima_captura.setObjectName(u"ultima_captura")
        self.ultima_captura.setGeometry(QRect(0, 0, 300, 180))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(300, 500, 400, 300))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"    background-color: #33415c;\n"
"    border: 1px solid #CBD2D9;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(0, 0, 401, 30))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setHintingPreference(QFont.PreferFullHinting)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: None;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.velocidad_icono = QPushButton(self.frame_2)
        self.velocidad_icono.setObjectName(u"velocidad_icono")
        self.velocidad_icono.setGeometry(QRect(10, 40, 50, 50))
        self.velocidad_icono.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"fotos iconos/velocidad.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.velocidad_icono.setIcon(icon8)
        self.velocidad_icono.setIconSize(QSize(50, 50))
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QRect(60, 70, 91, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setHintingPreference(QFont.PreferFullHinting)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QRect(60, 50, 81, 20))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setHintingPreference(QFont.PreferFullHinting)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background: transparent;\n"
"")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.distancia_icono = QPushButton(self.frame_2)
        self.distancia_icono.setObjectName(u"distancia_icono")
        self.distancia_icono.setGeometry(QRect(10, 100, 50, 50))
        self.distancia_icono.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"fotos iconos/distancia.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.distancia_icono.setIcon(icon9)
        self.distancia_icono.setIconSize(QSize(50, 50))
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QRect(30, 140, 171, 21))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QRect(80, 120, 51, 20))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(True)
        self.label_9.setGeometry(QRect(50, 220, 231, 20))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background: transparent;")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.orientacion_icono = QPushButton(self.frame_2)
        self.orientacion_icono.setObjectName(u"orientacion_icono")
        self.orientacion_icono.setGeometry(QRect(10, 180, 50, 50))
        self.orientacion_icono.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"fotos iconos/orientacion.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.orientacion_icono.setIcon(icon10)
        self.orientacion_icono.setIconSize(QSize(50, 50))
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setEnabled(True)
        self.label_13.setGeometry(QRect(80, 190, 181, 20))
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.velocidad_icono_6 = QPushButton(self.frame_2)
        self.velocidad_icono_6.setObjectName(u"velocidad_icono_6")
        self.velocidad_icono_6.setGeometry(QRect(210, 40, 50, 50))
        self.velocidad_icono_6.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"fotos iconos/altura.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.velocidad_icono_6.setIcon(icon11)
        self.velocidad_icono_6.setIconSize(QSize(50, 50))
        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setEnabled(True)
        self.label_18.setGeometry(QRect(280, 50, 81, 20))
        self.label_18.setFont(font2)
        self.label_18.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setEnabled(True)
        self.label_19.setGeometry(QRect(270, 70, 101, 20))
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background: transparent;\n"
"")
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_22 = QLabel(self.frame_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setEnabled(True)
        self.label_22.setGeometry(QRect(260, 120, 121, 20))
        self.label_22.setFont(font2)
        self.label_22.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_23 = QLabel(self.frame_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setEnabled(True)
        self.label_23.setGeometry(QRect(270, 140, 101, 21))
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background: transparent;\n"
"")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.velocidad_icono_8 = QPushButton(self.frame_2)
        self.velocidad_icono_8.setObjectName(u"velocidad_icono_8")
        self.velocidad_icono_8.setGeometry(QRect(210, 110, 50, 50))
        self.velocidad_icono_8.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"fotos iconos/presion.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.velocidad_icono_8.setIcon(icon12)
        self.velocidad_icono_8.setIconSize(QSize(50, 50))
        self.label_33 = QLabel(self.frame_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setEnabled(True)
        self.label_33.setGeometry(QRect(330, 190, 71, 20))
        self.label_33.setFont(font2)
        self.label_33.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_34 = QLabel(self.frame_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setEnabled(True)
        self.label_34.setGeometry(QRect(330, 210, 61, 21))
        self.label_34.setFont(font1)
        self.label_34.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background: transparent;\n"
"")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.velocidad_icono_9 = QPushButton(self.frame_2)
        self.velocidad_icono_9.setObjectName(u"velocidad_icono_9")
        self.velocidad_icono_9.setGeometry(QRect(280, 180, 50, 50))
        self.velocidad_icono_9.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u"fotos iconos/lastre.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.velocidad_icono_9.setIcon(icon13)
        self.velocidad_icono_9.setIconSize(QSize(50, 50))
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(1200, 180, 300, 320))
        self.frame_3.setStyleSheet(u"QFrame {\n"
"    background-color: #5c677d;\n"
"    border: 1px solid #CBD2D9;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_45 = QLabel(self.frame_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setEnabled(True)
        self.label_45.setGeometry(QRect(0, 0, 300, 30))
        self.label_45.setFont(font)
        self.label_45.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_45.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.velocidad_icono_16 = QPushButton(self.frame_3)
        self.velocidad_icono_16.setObjectName(u"velocidad_icono_16")
        self.velocidad_icono_16.setGeometry(QRect(20, 60, 50, 50))
        self.velocidad_icono_16.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"fotos iconos/control.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.velocidad_icono_16.setIcon(icon14)
        self.velocidad_icono_16.setIconSize(QSize(50, 50))
        self.label_46 = QLabel(self.frame_3)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setEnabled(True)
        self.label_46.setGeometry(QRect(140, 100, 81, 20))
        self.label_46.setFont(font1)
        self.label_46.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background: transparent;")
        self.label_46.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.toolButton_9 = QToolButton(self.frame_3)
        self.toolButton_9.setObjectName(u"toolButton_9")
        self.toolButton_9.setGeometry(QRect(90, 70, 81, 30))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        self.toolButton_9.setFont(font3)
        self.toolButton_10 = QToolButton(self.frame_3)
        self.toolButton_10.setObjectName(u"toolButton_10")
        self.toolButton_10.setGeometry(QRect(170, 70, 101, 30))
        self.toolButton_10.setFont(font3)
        self.toolButton_10.setStyleSheet(u"QToolButton {\n"
"    background-color: rgb(255, 162, 0);\n"
"}")
        self.velocidad_icono_17 = QPushButton(self.frame_3)
        self.velocidad_icono_17.setObjectName(u"velocidad_icono_17")
        self.velocidad_icono_17.setGeometry(QRect(70, 240, 50, 50))
        self.velocidad_icono_17.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u"fotos iconos/abajo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.velocidad_icono_17.setIcon(icon15)
        self.velocidad_icono_17.setIconSize(QSize(50, 50))
        self.velocidad_icono_18 = QPushButton(self.frame_3)
        self.velocidad_icono_18.setObjectName(u"velocidad_icono_18")
        self.velocidad_icono_18.setGeometry(QRect(70, 160, 50, 50))
        self.velocidad_icono_18.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u"fotos iconos/arriba.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.velocidad_icono_18.setIcon(icon16)
        self.velocidad_icono_18.setIconSize(QSize(50, 50))
        self.velocidad_icono_19 = QPushButton(self.frame_3)
        self.velocidad_icono_19.setObjectName(u"velocidad_icono_19")
        self.velocidad_icono_19.setGeometry(QRect(30, 200, 50, 50))
        self.velocidad_icono_19.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u"fotos iconos/izquierda.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.velocidad_icono_19.setIcon(icon17)
        self.velocidad_icono_19.setIconSize(QSize(50, 50))
        self.velocidad_icono_20 = QPushButton(self.frame_3)
        self.velocidad_icono_20.setObjectName(u"velocidad_icono_20")
        self.velocidad_icono_20.setGeometry(QRect(110, 200, 50, 50))
        self.velocidad_icono_20.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u"fotos iconos/derecha.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.velocidad_icono_20.setIcon(icon18)
        self.velocidad_icono_20.setIconSize(QSize(50, 50))
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 480, 300, 320))
        self.frame_4.setStyleSheet(u"QFrame {\n"
"    background-color: #7d8597;\n"
"    border: 1px solid #CBD2D9;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_47 = QLabel(self.frame_4)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setEnabled(True)
        self.label_47.setGeometry(QRect(0, 0, 300, 30))
        self.label_47.setFont(font)
        self.label_47.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border: None;\n"
"font-weight: bold;")
        self.label_47.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textEdit = QTextEdit(self.frame_4)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 40, 280, 220))
        self.textEdit.setFont(font3)
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"background-color: rgb(255, 249, 206);\n"
"color: black;\n"
"}")
        self.lineEdit = QLineEdit(self.frame_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 260, 280, 25))
        self.frame_11 = QFrame(self.centralwidget)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(700, 500, 220, 300))
        self.frame_11.setStyleSheet(u"QFrame {\n"
"    background-color: #33415c;\n"
"    border: 1px solid #CBD2D9;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.label_10 = QLabel(self.frame_11)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(True)
        self.label_10.setGeometry(QRect(0, 0, 221, 30))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temperatura_icono = QPushButton(self.frame_11)
        self.temperatura_icono.setObjectName(u"temperatura_icono")
        self.temperatura_icono.setGeometry(QRect(30, 110, 50, 50))
        self.temperatura_icono.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u"fotos iconos/temperatura.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.temperatura_icono.setIcon(icon19)
        self.temperatura_icono.setIconSize(QSize(50, 50))
        self.label_14 = QLabel(self.frame_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setEnabled(True)
        self.label_14.setGeometry(QRect(110, 120, 91, 20))
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QRect(110, 50, 81, 20))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.velocidad_icono_3 = QPushButton(self.frame_11)
        self.velocidad_icono_3.setObjectName(u"velocidad_icono_3")
        self.velocidad_icono_3.setGeometry(QRect(30, 40, 50, 50))
        self.velocidad_icono_3.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u"fotos iconos/bater\u00eda.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.velocidad_icono_3.setIcon(icon20)
        self.velocidad_icono_3.setIconSize(QSize(50, 50))
        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QRect(100, 70, 91, 20))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background: transparent;\n"
"")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_15 = QLabel(self.frame_11)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setEnabled(True)
        self.label_15.setGeometry(QRect(100, 140, 101, 20))
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background: transparent;\n"
"")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temperatura_icono_4 = QPushButton(self.frame_11)
        self.temperatura_icono_4.setObjectName(u"temperatura_icono_4")
        self.temperatura_icono_4.setGeometry(QRect(30, 180, 50, 50))
        self.temperatura_icono_4.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u"fotos iconos/propulsor.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.temperatura_icono_4.setIcon(icon21)
        self.temperatura_icono_4.setIconSize(QSize(50, 50))
        self.label_32 = QLabel(self.frame_11)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setEnabled(True)
        self.label_32.setGeometry(QRect(100, 220, 101, 20))
        self.label_32.setFont(font1)
        self.label_32.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background: transparent;\n"
"")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(self.frame_11)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 200, 20, 20))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 162, 0);\n"
"}")
        self.pushButton_2 = QPushButton(self.frame_11)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(130, 200, 20, 20))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 162, 0);\n"
"}")
        self.pushButton_5 = QPushButton(self.frame_11)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(160, 200, 20, 20))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(104, 93, 93);\n"
"}")
        self.pushButton_6 = QPushButton(self.frame_11)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(190, 200, 20, 20))
        self.pushButton_6.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 162, 0);\n"
"}")
        self.frame_sensores = QFrame(self.centralwidget)
        self.frame_sensores.setObjectName(u"frame_sensores")
        self.frame_sensores.setGeometry(QRect(920, 500, 400, 300))
        self.frame_sensores.setStyleSheet(u"QFrame {\n"
"    background-color: #33415c;\n"
"    border: 1px solid #CBD2D9;\n"
"    border-radius: 6px;\n"
"}")
        self.frame_sensores.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_sensores.setFrameShadow(QFrame.Shadow.Raised)
        self.label_11 = QLabel(self.frame_sensores)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QRect(0, 0, 400, 30))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_21 = QLabel(self.frame_sensores)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setEnabled(True)
        self.label_21.setGeometry(QRect(50, 140, 151, 20))
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background: transparent;\n"
"")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.velocidad_icono_5 = QPushButton(self.frame_sensores)
        self.velocidad_icono_5.setObjectName(u"velocidad_icono_5")
        self.velocidad_icono_5.setGeometry(QRect(10, 40, 50, 50))
        self.velocidad_icono_5.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon22 = QIcon()
        icon22.addFile(u"fotos iconos/diametro.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.velocidad_icono_5.setIcon(icon22)
        self.velocidad_icono_5.setIconSize(QSize(50, 50))
        self.label_20 = QLabel(self.frame_sensores)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setEnabled(True)
        self.label_20.setGeometry(QRect(80, 120, 81, 20))
        self.label_20.setFont(font2)
        self.label_20.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_17 = QLabel(self.frame_sensores)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setEnabled(True)
        self.label_17.setGeometry(QRect(80, 50, 81, 20))
        self.label_17.setFont(font2)
        self.label_17.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.velocidad_icono_7 = QPushButton(self.frame_sensores)
        self.velocidad_icono_7.setObjectName(u"velocidad_icono_7")
        self.velocidad_icono_7.setGeometry(QRect(10, 110, 50, 50))
        self.velocidad_icono_7.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.velocidad_icono_7.setIcon(icon22)
        self.velocidad_icono_7.setIconSize(QSize(50, 50))
        self.label_16 = QLabel(self.frame_sensores)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setEnabled(True)
        self.label_16.setGeometry(QRect(50, 70, 151, 20))
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background: transparent;\n"
"")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_24 = QLabel(self.frame_sensores)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setEnabled(True)
        self.label_24.setGeometry(QRect(80, 190, 81, 20))
        self.label_24.setFont(font2)
        self.label_24.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_25 = QLabel(self.frame_sensores)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setEnabled(True)
        self.label_25.setGeometry(QRect(50, 210, 151, 20))
        self.label_25.setFont(font1)
        self.label_25.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background: transparent;\n"
"")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.velocidad_icono_10 = QPushButton(self.frame_sensores)
        self.velocidad_icono_10.setObjectName(u"velocidad_icono_10")
        self.velocidad_icono_10.setGeometry(QRect(10, 180, 50, 50))
        self.velocidad_icono_10.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.velocidad_icono_10.setIcon(icon11)
        self.velocidad_icono_10.setIconSize(QSize(50, 50))
        self.label_26 = QLabel(self.frame_sensores)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setEnabled(True)
        self.label_26.setGeometry(QRect(290, 50, 91, 20))
        self.label_26.setFont(font2)
        self.label_26.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temperatura_icono_2 = QPushButton(self.frame_sensores)
        self.temperatura_icono_2.setObjectName(u"temperatura_icono_2")
        self.temperatura_icono_2.setGeometry(QRect(230, 40, 50, 50))
        self.temperatura_icono_2.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.temperatura_icono_2.setIcon(icon19)
        self.temperatura_icono_2.setIconSize(QSize(50, 50))
        self.label_27 = QLabel(self.frame_sensores)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setEnabled(True)
        self.label_27.setGeometry(QRect(280, 70, 101, 20))
        self.label_27.setFont(font1)
        self.label_27.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background: transparent;\n"
"")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_28 = QLabel(self.frame_sensores)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setEnabled(True)
        self.label_28.setGeometry(QRect(290, 110, 91, 31))
        self.label_28.setFont(font2)
        self.label_28.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temperatura_icono_3 = QPushButton(self.frame_sensores)
        self.temperatura_icono_3.setObjectName(u"temperatura_icono_3")
        self.temperatura_icono_3.setGeometry(QRect(220, 110, 50, 50))
        self.temperatura_icono_3.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon23 = QIcon()
        icon23.addFile(u"fotos iconos/salinidad.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.temperatura_icono_3.setIcon(icon23)
        self.temperatura_icono_3.setIconSize(QSize(50, 50))
        self.label_29 = QLabel(self.frame_sensores)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setEnabled(True)
        self.label_29.setGeometry(QRect(280, 140, 101, 20))
        self.label_29.setFont(font1)
        self.label_29.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background: transparent;\n"
"")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_30 = QLabel(self.frame_sensores)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setEnabled(True)
        self.label_30.setGeometry(QRect(290, 190, 81, 20))
        self.label_30.setFont(font2)
        self.label_30.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_31 = QLabel(self.frame_sensores)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setEnabled(True)
        self.label_31.setGeometry(QRect(270, 210, 131, 20))
        self.label_31.setFont(font1)
        self.label_31.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background: transparent;\n"
"")
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.velocidad_icono_11 = QPushButton(self.frame_sensores)
        self.velocidad_icono_11.setObjectName(u"velocidad_icono_11")
        self.velocidad_icono_11.setGeometry(QRect(230, 180, 50, 50))
        self.velocidad_icono_11.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.velocidad_icono_11.setIcon(icon11)
        self.velocidad_icono_11.setIconSize(QSize(50, 50))
        self.frame_13 = QFrame(self.centralwidget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(1320, 500, 180, 300))
        self.frame_13.setStyleSheet(u"QFrame {\n"
"    background-color: #33415c;\n"
"    border: None;\n"
"}")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.label_12 = QLabel(self.frame_13)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setEnabled(True)
        self.label_12.setGeometry(QRect(0, 0, 180, 30))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background-color: transparent;\n"
"")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.velocidad_icono_4 = QPushButton(self.frame_13)
        self.velocidad_icono_4.setObjectName(u"velocidad_icono_4")
        self.velocidad_icono_4.setGeometry(QRect(20, 50, 50, 50))
        self.velocidad_icono_4.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon24 = QIcon()
        icon24.addFile(u"fotos iconos/luces.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.velocidad_icono_4.setIcon(icon24)
        self.velocidad_icono_4.setIconSize(QSize(50, 50))
        self.label_8 = QLabel(self.frame_13)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QRect(80, 80, 81, 20))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background: transparent;")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.toolButton_7 = QToolButton(self.frame_13)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setGeometry(QRect(90, 50, 30, 30))
        self.toolButton_7.setStyleSheet(u"QToolButton {\n"
"    background-color: rgb(255, 162, 0);\n"
"}")
        self.toolButton_8 = QToolButton(self.frame_13)
        self.toolButton_8.setObjectName(u"toolButton_8")
        self.toolButton_8.setGeometry(QRect(120, 50, 30, 30))
        self.label_41 = QLabel(self.frame_13)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setEnabled(True)
        self.label_41.setGeometry(QRect(90, 180, 61, 21))
        self.label_41.setFont(font1)
        self.label_41.setStyleSheet(u"color: black;\n"
"border: None;\n"
"font-weight: bold;\n"
"background: transparent;\n"
"")
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.velocidad_icono_13 = QPushButton(self.frame_13)
        self.velocidad_icono_13.setObjectName(u"velocidad_icono_13")
        self.velocidad_icono_13.setGeometry(QRect(20, 140, 50, 50))
        self.velocidad_icono_13.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon25 = QIcon()
        icon25.addFile(u"fotos iconos/activar_lastre.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.velocidad_icono_13.setIcon(icon25)
        self.velocidad_icono_13.setIconSize(QSize(50, 50))
        self.spinBox = QSpinBox(self.frame_13)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(80, 140, 81, 41))
        font4 = QFont()
        font4.setPointSize(15)
        self.spinBox.setFont(font4)
        self.spinBox.setValue(30)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1500, 25))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema de visi\u00f3n", None))
        self.video.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.captura.setText("")
        self.grabar.setText("")
        self.movimiento.setText(QCoreApplication.translate("MainWindow", u"Movimiento", None))
        self.configuracion.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.camaras.setText(QCoreApplication.translate("MainWindow", u"C\u00e1maras", None))
        self.calibracion.setText(QCoreApplication.translate("MainWindow", u"Calibraci\u00f3n", None))
        self.conexion.setText(QCoreApplication.translate("MainWindow", u"Conexi\u00f3n", None))
        self.exportar.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.ultima_captura.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Navegaci\u00f3n", None))
        self.velocidad_icono.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"5 m/s", None))
        self.distancia_icono.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Distancia recorrida", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"10 m", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Orientaci\u00f3n(yaw,pitch,roll)", None))
        self.orientacion_icono.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"10.0\u00b0 | 0.1\u00b0 | -0.2\u00b0", None))
        self.velocidad_icono_6.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"102.4 m", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Profundidad", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"10.02 bar", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Presi\u00f3n", None))
        self.velocidad_icono_8.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"30%", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Lastre", None))
        self.velocidad_icono_9.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Teleoperaci\u00f3n", None))
        self.velocidad_icono_16.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Control", None))
        self.toolButton_9.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.toolButton_10.setText(QCoreApplication.translate("MainWindow", u"Aut\u00f3matico", None))
        self.velocidad_icono_17.setText("")
        self.velocidad_icono_18.setText("")
        self.velocidad_icono_19.setText("")
        self.velocidad_icono_20.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Log Info", None))
        self.textEdit.setDocumentTitle("")
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">&gt;&gt;Inicializando...</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">&gt;&gt;Sistema inicializado.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"
                        "\"><span style=\" font-family:'Segoe UI';\">&gt;&gt;Conexi\u00f3n exitosa.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">&gt;&gt;C\u00e1maras encendidas.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI';\">&gt;&gt;Luces encendidas.</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Estado del robot", None))
        self.temperatura_icono.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"20 \u00b0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"60 %", None))
        self.velocidad_icono_3.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Bater\u00eda", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Temperatura", None))
        self.temperatura_icono_4.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Propulsores", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Sensores y entorno", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Espesor tuber\u00eda", None))
        self.velocidad_icono_5.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"5 mm", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"200 mm", None))
        self.velocidad_icono_7.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Di\u00e1metro tuber\u00eda", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"2.2m", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Distancia del suelo", None))
        self.velocidad_icono_10.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"15 \u00b0", None))
        self.temperatura_icono_2.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Temperatura", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"35 g/L", None))
        self.temperatura_icono_3.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Salinidad", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"1.0m", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Distancia objeto", None))
        self.velocidad_icono_11.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Actuadores", None))
        self.velocidad_icono_4.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Luces", None))
        self.toolButton_7.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.toolButton_8.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Lastre", None))
        self.velocidad_icono_13.setText("")
    # retranslateUi

