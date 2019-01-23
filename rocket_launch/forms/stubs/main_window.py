from PySide2.QtWidgets import QMainWindow, QWidget, QPushButton, QLineEdit


class MainWindowStub(QMainWindow):
    # verticalLayout: QVBoxLayout
    # horizontalLayout: QHBoxLayout
    # horizontalSpacer: Spacer
    # horizontalSpacer_2: Spacer

    central_widget: QWidget

    password_input: QLineEdit
    pilot_input: QLineEdit

    launch_button: QPushButton
