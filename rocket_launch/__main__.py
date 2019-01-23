import sys

from rocket_launch import app
from rocket_launch.forms.impl.main_window import MainWindow


main_window = MainWindow()
main_window.setup()
main_window.show()

sys.exit(app.exec_())
