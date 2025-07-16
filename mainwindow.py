import sys
import cv2
import time

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QTimer, Qt

from ui_form import Ui_MainWindow  # generado con pyside6-uic camara_ui.ui -o ui_form.py

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Cámara y temporizador
        self.cap = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        # Conexión de botones
        #self.ui.start.clicked.connect(self.iniciar_camara)
        #self.ui.stop.clicked.connect(self.detener_camara)
        self.ui.captura.clicked.connect(self.capturar_imagen)

        self.iniciar_camara()

    def iniciar_camara(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        #print(f"Resolución real de cámara: {w} x {h}")
        if self.cap.isOpened():
            self.timer.start(60)
        else:
            print("No se pudo acceder a la cámara.")

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            pix = QPixmap.fromImage(img)
            #self.ui.video.setPixmap(pix)
            self.ui.video.setPixmap(pix.scaled(
                self.ui.video.width(),
                self.ui.video.height(),
                Qt.KeepAspectRatio
            ))

    def detener_camara(self):
        self.timer.stop()
        if self.cap:
            self.cap.release()
            self.cap = None
        self.ui.video.clear()

    def capturar_imagen(self):
        if self.cap:
            ret, frame = self.cap.read()
            if ret:
                nombre = f"captura_{int(time.time())}.png"
                cv2.imwrite(nombre, frame)
                print(f"Imagen guardada: {nombre}")

                # Mostrar en QLabel secundaria
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = frame_rgb.shape
                bytes_per_line = ch * w
                img = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
                pix = QPixmap.fromImage(img)
                pix_resized = pix.scaled(self.ui.ultima_captura.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.ui.ultima_captura.setPixmap(pix_resized)

    def closeEvent(self, event):
        self.detener_camara()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

