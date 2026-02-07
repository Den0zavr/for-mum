import sys; import os
from core import AppTemplate
from ui import MainWindow

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    app = AppTemplate([])
    main_win = MainWindow()
    main_win.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()