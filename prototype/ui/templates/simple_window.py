from PySide6.QtWidgets import QWidget

class SimpleWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        

        self.windowTitle('New window title')