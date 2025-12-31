from PyQt6.QtWidgets import QApplication, QStyleFactory


class AppTemplate(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        self.setup_application()

    def setup_application(self):
        self.setStyle(QStyleFactory.create("Fusion"))
        self.setApplicationName("Excel Assistant")
        self.setOrganizationName("")
