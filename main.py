import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui import MainWindow
from core import AppTemplate

def main():
    app = AppTemplate(sys.argv)

    main_win = MainWindow()
    main_win.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()