import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication
from interface.mainUi import MainWindow

class Window(QMainWindow, MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        super().setupUi(self)

        self.buttonGroup.buttonClicked.connect(self.changeText) 
        self.btnDelete.clicked.connect(self.deleteText)
        self.btnResult.clicked.connect(self.calculate)
        self.btnClear.clicked.connect(lambda: self.Res.setText(""))

        self.lastResult = None
    
    def changeText(self, button):
        operators = ("+", "-", "*", "÷")

        if self.lastResult == None:
            clickedText = self.Res.text() + button.text()
        
            self.Res.setText(clickedText)
        else:
            if button.text() not in operators:
                self.Res.setText("")
                clickedText = self.Res.text() + button.text()
        
                self.Res.setText(clickedText)
                self.lastResult = None
            else:
                clickedText = self.Res.text() + button.text()
        
                self.Res.setText(clickedText)
                self.lastResult = None

    def deleteText(self):
        text = self.Res.text()

        self.Res.setText(text[:-1])
    
    def calculate(self):
        expression = self.Res.text().replace("÷", "/")

        try:
            result = eval(expression)
        except:
            result = 0
            self.Res.setText("")
        
        self.lastResult = result
        self.Res.setText(f"{result}")

if __name__ == "__main__":
    QApplication.setDesktopSettingsAware(False)
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setWindowIcon(QIcon("src/icon.png"))
    window = Window()
    window.show()
    app.exec_()