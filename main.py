# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ventana_principal import Ui_MainWindow  # Asegúrate de que el archivo se llame ventana_principal.py

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Conectar botones a funciones
        self.btnAgregarPropietario.clicked.connect(self.agregar_propietario)
        self.btnAgregarFinca.clicked.connect(self.agregar_finca)

    def agregar_propietario(self):
        # Verificar que los campos no estén vacíos
        if not self.lineEditNombre.text() or not self.lineEditDocumento.text():
            QMessageBox.critical(self, "Error", "Debe llenar todos los campos para agregar un propietario.")
            return

        # Mostrar mensaje de confirmación
        QMessageBox.information(self, "Éxito", "Propietario agregado con éxito.")

    def agregar_finca(self):
        # Verificar que los campos no estén vacíos
        if not self.lineEditMunicipio.text() or not self.lineEditRegistroCastral.text():
            QMessageBox.critical(self, "Error", "Debe llenar todos los campos para agregar una finca.")
            return

        # Limpiar campos de texto especificados
        self.lineEditMunicipio.clear()
        self.lineEditRegistroCastral.clear()
        QMessageBox.information(self, "Éxito", "Finca agregada con éxito.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
