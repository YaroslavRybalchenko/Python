import sys 
import os
from PyQt5 import QtWidgets
import Interface

class Calculator(QtWidgets.QMainWindow, Interface.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.calculation)
        
    def calculation(self):
        expression=self.textEdit.toPlainText()
        expression=expression.replace('^','**')
        result=eval(expression)
        self.textEdit_2.setText(str(result))
        
if __name__=='__main__':    
    app=QtWidgets.QApplication(sys.argv)
    calc=Calculator()
    calc.show()
    sys.exit(app.exec_())
