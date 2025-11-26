
import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()  

def main():
    app =qtw.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("My App")
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()