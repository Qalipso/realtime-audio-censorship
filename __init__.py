from epydoc.docwriter.dotgraph import SELECTED_BG
from pyqt_ui import *

def main():
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

