from PySide6.QtWidgets import QMainWindow, QPushButton, QLineEdit, QLabel
from utils import Singleton
from ui import ExtractWindow

class MainWindow(QMainWindow, Singleton):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 1024, 768)  # x, y, width, height
        #self.button = QPushButton("Text", self)
        #self.button.clicked.connect(self.myfunc)

        self.edit = QLineEdit(self)
        self.edit.setPlaceholderText("Typing...")
        self.edit.move(0, 25)

        self.menu = self.menuBar()
        file_menu = self.menu.addMenu("File")
        menu_menu = self.menu.addMenu("Menu")

        self.button = QPushButton("New window, self")
        self.button.clicked.connect(self.myfunc)
        self.button.move(100, 50)

        # self.result_tracker = ResultTracker()
        # self.orchestrator = Orchestrator()

        self.setup_connections()

    def myfunc(self):
        windw = ExtractWindow()
        # windw.show()

    def setup_connections(self):
        # self.main_window.batch_requested.connect(self.orchestrator.run_batch)
        ...

    """def open_extractor(self):
        self.extractor = ExtractWindow()
        self.extractor.show()"""

    """def open_batch_processor(self):
        self.batcher = BatchWindow()
        self.batcher.show()"""