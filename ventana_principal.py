from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setWindowTitle("Administración Vivero")

        # Fuente personalizada
        font = QtGui.QFont()
        font.setPointSize(10)

        # Widget central
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Grupo de Propietario
        self.groupBoxPropietario = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxPropietario.setGeometry(QtCore.QRect(20, 20, 460, 150))
        self.groupBoxPropietario.setTitle("Propietario")
        self.groupBoxPropietario.setFont(font)

        # Campo de Documento de Identidad
        self.labelDocumento = QtWidgets.QLabel(self.groupBoxPropietario)
        self.labelDocumento.setText("Documento Identidad")
        self.labelDocumento.setGeometry(QtCore.QRect(20, 30, 130, 20))

        self.lineEditDocumento = QtWidgets.QLineEdit(self.groupBoxPropietario)
        self.lineEditDocumento.setGeometry(QtCore.QRect(160, 30, 120, 20))

        # Campos de Nombre y Apellido
        self.labelNombre = QtWidgets.QLabel(self.groupBoxPropietario)
        self.labelNombre.setText("Nombre")
        self.labelNombre.setGeometry(QtCore.QRect(20, 60, 50, 20))

        self.lineEditNombre = QtWidgets.QLineEdit(self.groupBoxPropietario)
        self.lineEditNombre.setGeometry(QtCore.QRect(80, 60, 120, 20))

        self.labelApellido = QtWidgets.QLabel(self.groupBoxPropietario)
        self.labelApellido.setText("Apellido")
        self.labelApellido.setGeometry(QtCore.QRect(220, 60, 50, 20))

        self.lineEditApellido = QtWidgets.QLineEdit(self.groupBoxPropietario)
        self.lineEditApellido.setGeometry(QtCore.QRect(280, 60, 120, 20))

        # Campos de Teléfono y Correo
        self.labelTelefono = QtWidgets.QLabel(self.groupBoxPropietario)
        self.labelTelefono.setText("Tel/Cel")
        self.labelTelefono.setGeometry(QtCore.QRect(20, 90, 50, 20))

        self.lineEditTelefono = QtWidgets.QLineEdit(self.groupBoxPropietario)
        self.lineEditTelefono.setGeometry(QtCore.QRect(80, 90, 120, 20))

        self.labelCorreo = QtWidgets.QLabel(self.groupBoxPropietario)
        self.labelCorreo.setText("Correo")
        self.labelCorreo.setGeometry(QtCore.QRect(220, 90, 50, 20))

        self.lineEditCorreo = QtWidgets.QLineEdit(self.groupBoxPropietario)
        self.lineEditCorreo.setGeometry(QtCore.QRect(280, 90, 120, 20))

        # Botón para agregar propietario
        self.btnAgregarPropietario = QtWidgets.QPushButton(self.groupBoxPropietario)
        self.btnAgregarPropietario.setText("Agregar Propietario")
        self.btnAgregarPropietario.setGeometry(QtCore.QRect(160, 120, 140, 30))

        # Grupo de Finca
        self.groupBoxFinca = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxFinca.setGeometry(QtCore.QRect(20, 190, 460, 150))
        self.groupBoxFinca.setTitle("Finca")
        self.groupBoxFinca.setFont(font)

        # Campos de Cultivo y Registro Castral
        self.labelCultivo = QtWidgets.QLabel(self.groupBoxFinca)
        self.labelCultivo.setText("Cultivo")
        self.labelCultivo.setGeometry(QtCore.QRect(20, 30, 50, 20))

        self.comboBoxCultivo = QtWidgets.QComboBox(self.groupBoxFinca)
        self.comboBoxCultivo.setGeometry(QtCore.QRect(80, 30, 150, 20))
        self.comboBoxCultivo.addItems(["Seleccione el cultivo", "Café", "Plátano", "Cacao", "Maíz"])

        self.labelRegistroCastral = QtWidgets.QLabel(self.groupBoxFinca)
        self.labelRegistroCastral.setText("Registro Castral")
        self.labelRegistroCastral.setGeometry(QtCore.QRect(240, 30, 100, 20))

        self.lineEditRegistroCastral = QtWidgets.QLineEdit(self.groupBoxFinca)
        self.lineEditRegistroCastral.setGeometry(QtCore.QRect(340, 30, 100, 20))

        # Campo de Municipio
        self.labelMunicipio = QtWidgets.QLabel(self.groupBoxFinca)
        self.labelMunicipio.setText("Municipio")
        self.labelMunicipio.setGeometry(QtCore.QRect(20, 70, 60, 20))

        self.lineEditMunicipio = QtWidgets.QLineEdit(self.groupBoxFinca)
        self.lineEditMunicipio.setGeometry(QtCore.QRect(80, 70, 150, 20))

        # Botón para agregar finca
        self.btnAgregarFinca = QtWidgets.QPushButton(self.groupBoxFinca)
        self.btnAgregarFinca.setText("Agregar Finca")
        self.btnAgregarFinca.setGeometry(QtCore.QRect(160, 110, 140, 30))

        MainWindow.setCentralWidget(self.centralwidget)

        # Configuración de traducción
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
