from rocket_launch.abc import Window
from rocket_launch.forms.stubs.main_window import MainWindowStub
from rocket_launch.ui import main_window


class MainWindow(Window):
    def __init__(self):
        self._window: MainWindowStub = main_window
        self._remaining_button_presses = 3

    def setup(self):
        self._window.launch_button.clicked.connect(self.button_clicked)
        self._window.password_input.textChanged.connect(self.text_input)
        self._window.pilot_input.textChanged.connect(self.text_input)

    def show(self):
        self._window.show()

    def button_clicked(self):
        if self._remaining_button_presses:
            self._window.launch_button.setText(str(self._remaining_button_presses))
            self._remaining_button_presses -= 1
        else:
            self._window.launch_button.setText("LIFTOFF!")

    def text_input(self):
        if not self._window.pilot_input.text() or not self._window.password_input.text():
            self._window.launch_button.setDisabled(True)
        else:
            self._window.launch_button.setDisabled(False)
