from fbs_runtime.application_context.PyQt5 import ApplicationContext, cached_property

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QFont

import sys

from bibmend import BibmendMainWindow

class BibmendApplicationContext(ApplicationContext):
    def run(self):
        # self.window.resize(800, 600)
        self.window.showMaximized()
        return appctxt.app.exec_()

    def get_design(self):
        qtCreatorFile = self.get_resource("mainwindow.ui")
        return qtCreatorFile
    
    @cached_property
    def window(self):
        # Load font
        raleway = QFont("Raleway", 10)

        # Load Window
        window = BibmendMainWindow(self.get_design())
        version = self.build_settings['version']
        window.setWindowTitle(f"Bibmend {version}")
        window.setFont(raleway)
        return window

if __name__ == '__main__':
    appctxt = BibmendApplicationContext()       # 1. Instantiate ApplicationContext
    exit_code = appctxt.run()
    # Load font
    # raleway = QFont("Raleway", 10)

    # window = QMainWindow()
    # window.setFont(raleway)
    # window.resize(250, 150)
    # window.show()
    #       # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)